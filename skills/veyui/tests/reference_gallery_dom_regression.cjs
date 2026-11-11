#!/usr/bin/env node
'use strict';
// Logic regression checks with a minimal DOM model. This is not browser,
// accessibility, image-legibility, layout, or native-dialog validation.
// Usage: node reference_gallery_dom_regression.cjs /path/to/skill
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { spawnSync } = require('node:child_process');
const root = process.argv[2];
assert(root, 'Pass the skill root as the first argument');
const template = fs.readFileSync(path.join(root, 'assets/reference-gallery.template.html'), 'utf8');
const source = template.split('<script>')[1].split('</script>')[0];
const generated = spawnSync('python3', ['-c', [
  'import importlib.util,json,sys',
  'from pathlib import Path',
  "p=Path(sys.argv[1]); s=importlib.util.spec_from_file_location('reference_library', p/'scripts/reference_library.py')",
  'm=importlib.util.module_from_spec(s); s.loader.exec_module(m)',
  "d=m.validate(json.loads((p/'data/reference-library.json').read_text()))",
  'print(m.gallery(d))'
].join('\n'), root], { encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
assert.equal(generated.status, 0, generated.stderr);
const generatedSource = generated.stdout.split('<script>')[1].split('</script>')[0];
const records = JSON.parse(generatedSource.match(/const records=(.*);\r?\nconst \$/)[1]);

// The public repository does not distribute reference images. Give the first record a tiny
// synthetic preview so the enlarge-dialog logic is still exercised.
if (!records.some(r => r.preview)) {
  records[0].preview = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=';
}

function harness(input) {
  const nodes = {};
  let focused = null;
  function element(tag = '') {
    return { tag, value: '', dataset: {}, style: {}, attributes: {}, children: [],
      append(...items) { this.children.push(...items); },
      setAttribute(name, value) { this.attributes[name] = value; },
      addEventListener() {},
      replaceChildren(...items) { this.children = items; },
      focus() { focused = this; },
      showModal() { this.modalCalls = (this.modalCalls || 0) + 1; }
    };
  }
  function find(node, predicate) {
    if (!node) return null;
    if (predicate(node)) return node;
    for (const child of node.children) {
      const match = find(child, predicate);
      if (match) return match;
    }
    return null;
  }
  const byRef = (node, id) => find(node, n => n.tag === 'button' && n.dataset.ref === id);
  const ctx = { document: {
    getElementById(id) { return nodes[id] ||= element(); },
    createElement: element,
    querySelector(selector) {
      const id = selector.match(/data-ref="(.*?)"/)[1];
      return byRef(nodes.comparison, id) || byRef(nodes.grid, id);
    }
  }, Blob, URL, setTimeout };
  vm.createContext(ctx);
  vm.runInContext(source.replace('/*REFERENCE_DATA*/', JSON.stringify(input)), ctx);
  return { nodes, find, byRef, draw: () => vm.runInContext('draw()', ctx), focus: () => focused };
}

const base = harness(records);
assert.equal(base.nodes.grid.children.length, records.length);
assert(base.nodes.status.textContent.includes(records.filter(r => r.preview).length + ' bundled concept images'));
assert.equal(base.find(base.nodes.grid, n => n.tag === 'img' && /^https:/.test(n.src || '')), null);
console.log('PASS: generated catalog draws; remote images initially remain unloaded');

for (const role of [undefined, null]) {
  const extended = structuredClone(records);
  extended[0].category = 'Finance';
  if (role === undefined) delete extended[0].content_role;
  else extended[0].content_role = role;
  const h = harness(extended);
  assert(h.find(h.nodes.grid, n => n.textContent === 'Finance · not classified'));
}
console.log('PASS: category with absent or null content role draws with fallback');

base.byRef(base.nodes.grid, 'R007').onclick();
base.nodes.q.value = 'calendar'; base.nodes.platform.value = 'mobile'; base.draw();
base.nodes.compare.onclick();
assert.equal(base.nodes.comparison.children.length, 1);
base.byRef(base.nodes.comparison, 'R007').onclick();
assert.equal(base.nodes.comparison.children.length, 0);
assert.equal(base.focus(), base.nodes.compare);
assert.equal(base.nodes.export.disabled, true);
console.log('PASS: removing filtered comparison item restores focus to Compare');

base.nodes.clear.onclick();
base.byRef(base.nodes.grid, 'R007').onclick();
assert.equal(base.focus(), base.byRef(base.nodes.comparison, 'R007'));
console.log('PASS: visible shortlist item retains a valid focus target');

const enlarge = base.find(base.nodes.grid, n => n.attributes['aria-label'] === 'Enlarge ' + records[0].title);
assert(enlarge); enlarge.onclick();
assert.equal(base.nodes.fullimage.src, records[0].preview);
assert.equal(base.nodes.fullimage.alt, records[0].title);
assert.equal(base.nodes.viewer.modalCalls, 1);
console.log('PASS: bundled image enlargement supplies actual pixels and title to dialog');

base.nodes.remote.onclick();
assert(base.find(base.nodes.grid, n => n.tag === 'img' && /^https:/.test(n.src || '')));
console.log('PASS: explicit preview opt-in adds linked images');
console.log('All minimal-DOM regressions passed; browser and visual review remain unperformed.');
