'use strict';
const $ = id => document.getElementById(id);
let catalog = [], units = {}, selected, category = 'All', latest = null, busy = false;
let history = [];
try { const saved = JSON.parse(localStorage.getItem('powercalcs.history') || '[]'); if (Array.isArray(saved)) history = saved.filter(x => x && x.result && x.inputs && typeof x.calculator === 'string').slice(0, 100); } catch (_) {}
const names = key => key.replaceAll('_', ' ').replace(/\b\w/g, c => c.toUpperCase());
const fmt = value => Number(value).toLocaleString(undefined, {maximumSignificantDigits: 7});
function el(tag, text, cls) { const item = document.createElement(tag); if (text !== undefined) item.textContent = text; if (cls) item.className = cls; return item; }
function persist() { try { localStorage.setItem('powercalcs.history', JSON.stringify(history)); } catch (_) { $('error').textContent = 'Browser storage is unavailable. Export JSON to keep this calculation.'; $('error').hidden = false; } renderHistory(); }
function renderCategories() {
  $('categories').replaceChildren();
  for (const name of ['All', ...new Set(catalog.map(c => c.category))]) {
    const count = catalog.filter(c => name === 'All' || c.category === name).length;
    const button = el('button', name === 'All' ? 'All calculations' : name, 'category' + (category === name ? ' active' : ''));
    button.setAttribute('aria-pressed', String(category === name)); button.append(el('span', String(count).padStart(2, '0')));
    button.onclick = () => { category = name; renderCategories(); renderList(); };
    $('categories').append(button);
  }
}
function renderList() {
  $('calculator-list').replaceChildren();
  const query = $('search').value.toLowerCase().trim();
  const filtered = catalog.filter(c => (category === 'All' || c.category === category) && (c.title + ' ' + c.description + ' ' + c.category).toLowerCase().includes(query));
  $('category-label').textContent = `${category} · ${filtered.length}`;
  for (const c of filtered) {
    const button = el('button', undefined, 'calc-item' + (selected?.id === c.id ? ' active' : ''));
    button.setAttribute('aria-pressed', String(selected?.id === c.id));
    button.append(el('span', String(catalog.indexOf(c) + 1).padStart(2, '0'), 'num'));
    const text = el('span', c.title); text.append(el('small', c.category)); button.append(text);
    button.onclick = () => select(c.id); $('calculator-list').append(button);
  }
  if (!filtered.length) $('calculator-list').append(el('p', 'No matching calculations.', 'calc-desc'));
}
function select(id, restoredInputs = null) {
  selected = catalog.find(c => c.id === id); if (!selected) return;
  latest = null; $('calc-title').textContent = selected.title; $('calc-category').textContent = selected.category.toUpperCase();
  $('calc-description').textContent = selected.description;
  $('input-fields').replaceChildren();
  for (const f of selected.fields) {
    const wrap = el('div', undefined, 'field'), label = el('label', f.label); label.htmlFor = `field-${f.key}`;
    const control = el('div', undefined, 'field-control'), input = document.createElement('input');
    input.id = `field-${f.key}`; input.type = 'number'; input.step = 'any'; input.required = true;
    input.value = restoredInputs?.[f.key]?.value ?? restoredInputs?.[f.key] ?? f.default;
    const selector = document.createElement('select'); selector.id = `unit-${f.key}`; selector.setAttribute('aria-label', `Unit for ${f.label}`);
    for (const [name, info] of Object.entries(units)) if (info.dimension === f.dimension) { const option = el('option', name); option.value = name; selector.append(option); }
    selector.value = restoredInputs?.[f.key]?.unit ?? f.unit;
    selector.onchange = () => { const old = selector.dataset.previous; const value = Number(input.value); if (input.value !== '' && Number.isFinite(value)) input.value = value * units[old].scale / units[selector.value].scale; selector.dataset.previous = selector.value; stale(); };
    selector.dataset.previous = selector.value; input.oninput = stale;
    control.append(input, selector); wrap.append(label, control, el('small', f.key)); $('input-fields').append(wrap);
  }
  $('equations').replaceChildren(...selected.formulas.map(eq => el('li', eq)));
  $('assumptions').replaceChildren(...selected.assumptions.map(a => el('p', a)));
  $('results').replaceChildren(el('div', 'Review inputs and run the calculation to generate a result.', 'empty-state'));
  $('result-status').textContent = 'AWAITING INPUT'; $('result-actions').hidden = true; $('phasor').hidden = true; $('error').hidden = true; $('trace').hidden = true;
  renderList(); document.title = selected.title + ' · PowerCalcs';
}
function stale() { if (latest) { latest = null; $('result-status').textContent = 'INPUTS CHANGED · RUN AGAIN'; $('result-actions').hidden = true; } }
function readInputs() {
  return Object.fromEntries(selected.fields.map(f => [f.key, {value: Number($(`field-${f.key}`).value), unit: $(`unit-${f.key}`).value}]));
}
function drawPhasors(result) {
  const entries = Object.entries(result.results).filter(([, v]) => v && typeof v === 'object' && 'real' in v);
  const canvas = $('phasor'); canvas.hidden = !entries.length; if (!entries.length) return;
  const ctx = canvas.getContext('2d'), width = canvas.width, height = canvas.height;
  const max = Math.max(...entries.map(([, v]) => v.magnitude), 1e-20), scale = 100 / max;
  ctx.fillStyle = '#142022'; ctx.fillRect(0, 0, width, height); ctx.strokeStyle = '#395053'; ctx.lineWidth = 1;
  ctx.beginPath(); ctx.moveTo(30, 150); ctx.lineTo(350, 150); ctx.moveTo(190, 25); ctx.lineTo(190, 275); ctx.stroke();
  const colors = ['#a7efce', '#e6aa6b', '#87bcf1', '#e6a4d6', '#e3de92', '#b1a7ef', '#82d6d0'];
  ctx.font = '11px monospace'; ctx.fillStyle = '#92a4aa'; ctx.fillText('Im', 197, 25); ctx.fillText('Re', 335, 168);
  entries.forEach(([key, v], index) => {
    const x = 190 + v.real * scale, y = 150 - v.imag * scale, a = Math.atan2(y - 150, x - 190);
    ctx.strokeStyle = colors[index % colors.length]; ctx.fillStyle = ctx.strokeStyle; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(190, 150); ctx.lineTo(x, y); ctx.stroke();
    if (v.magnitude > max * 1e-12) { ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x-9*Math.cos(a-.4), y-9*Math.sin(a-.4)); ctx.lineTo(x-9*Math.cos(a+.4), y-9*Math.sin(a+.4)); ctx.closePath(); ctx.fill(); }
    ctx.fillText(`${key}: ${fmt(v.magnitude)} ∠ ${fmt(v.angle_deg)}° ${result.output_units[key]}`, 365, 40 + index * 29);
  });
}
function displayResult(result) {
  latest = result; $('error').hidden = true; $('result-status').textContent = 'COMPUTED · FULL PRECISION SAVED';
  const grid = el('div', undefined, 'result-grid');
  for (const [key, value] of Object.entries(result.results)) {
    const card = el('div', undefined, 'result-card'); card.append(el('label', names(key)));
    const complex = typeof value === 'object', primary = el('div', fmt(complex ? value.magnitude : value), 'result-value');
    primary.append(el('small', result.output_units[key])); card.append(primary);
    if (complex) card.append(el('div', `${fmt(value.real)} ${value.imag < 0 ? '−' : '+'} j${fmt(Math.abs(value.imag))} · ∠ ${fmt(value.angle_deg)}°`, 'complex-detail'));
    grid.append(card);
  }
  $('results').replaceChildren(grid); $('result-actions').hidden = false; $('trace').hidden = false;
  $('trace-data').textContent = JSON.stringify({version: result.version, timestamp: result.timestamp, inputs_si: result.inputs_si, input_units: result.input_units}, null, 2);
  drawPhasors(result);
}
async function run(event) {
  event.preventDefault(); if (busy) return; busy = true;
  const button = $('calculator-form').querySelector('[type=submit]'); button.disabled = true; $('error').hidden = true;
  const calcId = selected.id, inputs = readInputs();
  try {
    const response = await fetch('/api/calculate', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({calculator: calcId, inputs})});
    const result = await response.json(); if (!response.ok) throw new Error(result.error || 'Calculation failed');
    if (selected.id !== calcId || JSON.stringify(readInputs()) !== JSON.stringify(inputs)) return;
    displayResult(result); history.unshift({calculator: calcId, inputs, result}); history = history.slice(0, 100); persist();
  } catch (error) { $('error').textContent = error.message; $('error').hidden = false; $('result-status').textContent = 'CHECK INPUTS'; latest = null; $('result-actions').hidden = true; }
  finally { busy = false; button.disabled = false; }
}
function renderHistory() {
  $('history-count').textContent = history.length; $('history-list').replaceChildren();
  for (const item of history) {
    const button = el('button', undefined, 'history-row'); button.append(el('span', item.result.title), el('small', new Date(item.result.timestamp).toLocaleString()));
    button.onclick = () => { category = 'All'; $('search').value = ''; renderCategories(); select(item.calculator, item.inputs); if (selected?.id === item.calculator) displayResult(item.result); $('calculator-form').scrollIntoView({behavior: 'smooth', block: 'start'}); };
    $('history-list').append(button);
  }
  if (!history.length) $('history-list').append(el('p', 'Completed studies will appear here.', 'calc-desc'));
}
$('calculator-form').addEventListener('submit', run);
$('search').addEventListener('input', renderList);
$('reset').onclick = () => select(selected.id);
$('history-toggle').onclick = () => { $('history-panel').hidden = !$('history-panel').hidden; if (!$('history-panel').hidden) $('history-panel').scrollIntoView({behavior: 'smooth'}); };
$('clear-history').onclick = () => { history = []; persist(); };
$('export').onclick = () => { if (!latest) return; const blob = new Blob([JSON.stringify(latest, null, 2)], {type: 'application/json'}), url = URL.createObjectURL(blob), link = el('a'); link.href = url; link.download = `study-${latest.calculator}.json`; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); };
$('print').onclick = () => { if (latest) window.print(); };
fetch('/api/catalog').then(r => { if (!r.ok) throw new Error('Engine unavailable'); return r.json(); }).then(data => { catalog = data.calculators; units = data.units; $('count').textContent = catalog.length; renderCategories(); select('three_power'); renderHistory(); }).catch(error => { $('calc-title').textContent = 'Unable to load calculation engine'; $('error').textContent = error.message; $('error').hidden = false; });
