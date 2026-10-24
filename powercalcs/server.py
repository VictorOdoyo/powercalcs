"""Loopback-only HTTP adapter; no database or external service dependency."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from importlib.resources import files
import json
from urllib.parse import urlsplit
from .catalog import calculate, calculators
from .units import catalog

class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):
        pass

    def reply(self,status,payload,kind='application/json; charset=utf-8'):
        data=json.dumps(payload,allow_nan=False).encode() if kind.startswith('application/json') else payload
        self.send_response(status)
        self.send_header('Content-Type',kind)
        self.send_header('Content-Length',str(len(data)))
        self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path=urlsplit(self.path).path
        if path=='/api/catalog':
            return self.reply(200,{'calculators':[c.metadata() for c in calculators().values()],
                                   'units':{key:{'dimension':dim,'scale':scale} for key,(dim,scale) in catalog().items()},'version':'1.0.0'})
        assets={'/':('index.html','text/html'),'/app.js':('app.js','text/javascript'),'/style.css':('style.css','text/css')}
        if path not in assets:
            return self.reply(404,{'error':'Not found'})
        name,kind=assets[path]
        return self.reply(200,files('powercalcs').joinpath('web',name).read_bytes(),kind+'; charset=utf-8')

    def do_POST(self):
        if urlsplit(self.path).path!='/api/calculate':
            return self.reply(404,{'error':'Not found'})
        # Reject browser cross-origin submissions to this local tool.
        origin=self.headers.get('Origin')
        if origin and origin!='http://'+self.headers.get('Host',''):
            return self.reply(403,{'error':'Cross-origin requests are not accepted'})
        try:
            length=int(self.headers.get('Content-Length','0'))
            if length<=0 or length>100000:
                return self.reply(413,{'error':'Request must contain 1 to 100000 bytes'})
            if self.headers.get_content_type()!='application/json':
                return self.reply(415,{'error':'Use application/json'})
            request=json.loads(self.rfile.read(length))
            if not isinstance(request,dict) or set(request)!={'calculator','inputs'} or not isinstance(request['calculator'],str):
                raise ValueError('Expected calculator name and inputs object')
            return self.reply(200,calculate(request['calculator'],request['inputs']))
        except (ValueError,TypeError,UnicodeError) as exc:
            return self.reply(400,{'error':str(exc)})

def serve(port=8765):
    if not 0<=port<=65535:
        raise ValueError('Port must be between 0 and 65535')
    with ThreadingHTTPServer(('127.0.0.1',port),Handler) as server:
        print(f'PowerCalcs: http://127.0.0.1:{server.server_port} (Ctrl+C to stop)',flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
