"""Command line study interface. JSON results are suitable for pipelines."""
import argparse
import json
import sys
from pathlib import Path
from .catalog import calculate, calculators

def main(argv=None):
    parser=argparse.ArgumentParser(prog='powercalcs',description='Traceable power engineering calculations')
    commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('list',help='List calculators as JSON')
    calc=commands.add_parser('calculate',help='Evaluate a calculator with explicit inputs')
    calc.add_argument('calculator')
    source=calc.add_mutually_exclusive_group(required=True)
    source.add_argument('--inputs',help='JSON object; use shell-appropriate quoting')
    source.add_argument('--file',help='Path to a JSON input object, or - for stdin')
    serve=commands.add_parser('serve',help='Open the local workbench at http://127.0.0.1:8765')
    serve.add_argument('--port',type=int,default=8765)
    args=parser.parse_args(argv)
    try:
        if args.command=='serve':
            from .server import serve
            serve(args.port)
            return 0
        if args.command=='list':
            result=[c.metadata() for c in calculators().values()]
        else:
            raw=args.inputs if args.inputs is not None else (sys.stdin.read() if args.file=='-' else Path(args.file).read_text(encoding='utf-8'))
            result=calculate(args.calculator,json.loads(raw))
        print(json.dumps(result,indent=2,allow_nan=False))
        return 0
    except (ValueError,OSError) as exc:
        print(json.dumps({'error':str(exc)}),file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(main())
