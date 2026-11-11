/* The result: Slackwater before and after. One set of boxes, moved by GSAP Flip and scrubbed by scroll, the range
   input or the Before/After control. Plain ES module; gsap, ScrollTrigger and Flip are globals. ASCII only.
   The static pair in the markup is the source of truth: it is what no-JS, reduced motion and a failed init show. */
const root = document.documentElement;
const sec = document.getElementById('choice');
const G = window.gsap, ST = window.ScrollTrigger, FL = window.Flip;
const reduce = root.classList.contains('rm') || matchMedia('(prefers-reduced-motion: reduce)').matches;
if (sec && sec.classList.contains('ba') && !reduce && G && ST && FL) {
  try { boot(); } catch (e) { console.warn('ba: static fallback', e); sec.classList.remove('is-live', 'is-pin'); }
}

function boot() {
  G.registerPlugin(ST, FL);
  const $ = (s, r = sec) => r.querySelector(s);
  const $$ = (s, r = sec) => Array.from(r.querySelectorAll(s));
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const mk = (tag, cls, html) => { const n = document.createElement(tag); if (cls) n.className = cls; if (html != null) n.innerHTML = html; return n; };
  const main = $('.ba__main'), source = $('.ba__static'), ui = $('.ba__ui'), note = $('.ba__note'), runway = $('.ba__runway');
  const seg = $$('.ba__seg button'), range = $('#ba-range'), fixLis = $$('.ba__fix');
  const mqPin = matchMedia('(min-width: 1280px) and (min-height: 640px)');
  const FIX = fixLis.map((li) => ({ t: $('h3', li).textContent, was: li.dataset.was, now: li.dataset.now }));

  /* The morph, in order. Type: the old words in the new type (old colors). Layout: Flip moves the boxes. Color: one
     slanted sweep across the whole frame recolors everything it passes. Proof: cards become readings, the orb becomes
     the panel and the chart. Copy: the old words give way to the new ones.
     A stage is [out, in, mode, window]. Mode x swaps whole text nodes (out fades in the first half, in the second half,
     never both), w is a local slanted wipe, S is the frame-wide sweep. */
  const SWEEP = [.47, .60];
  const SW = (o, i) => [o, i, 'S'];
  const TYPE_COPY = (a, b, m) => [['b', '1', m || 'c', [a, b]], SW('1', '2'), ['2', 'a', 'x', [.82, .92]]];
  const PLAN = {
    nav: [['b', '1', 'c', [.04, .14]], SW('1', 'a')],
    foot: [['b', '1', 'c', [.08, .18]], ['1', 'a', 'x', [.58, .66]]],
    badge: TYPE_COPY(.04, .14), head: TYPE_COPY(.03, .17), sub: TYPE_COPY(.06, .18, 'd'), btn: TYPE_COPY(.08, .18),
    bg: [SW('b', 'a')],
    focal: [SW('b', '1'), ['1', 'a', 'w', [.56, .68]]],
    p1: [SW('b', '1'), ['1', 'a', 'x', [.56, .64]]], p2: [SW('b', '1'), ['1', 'a', 'x', [.59, .67]]], p3: [SW('b', '1'), ['1', 'a', 'x', [.62, .70]]]
  };
  const LABEL = .5;
  const TAGS = [
    { at: .20, els: ['head', 'sub', 'badge', 'btn', 'nav', 'foot'] },
    { at: .47, frame: true },
    { at: .61, els: ['btn', 'focal'] },
    { at: .79, els: ['p1', 'p2', 'p3', 'focal'] },
    { at: .93, els: ['head', 'sub', 'badge', 'btn'] }
  ];
  const SLASH = 6, END = 100 + SLASH, HID = 'polygon(0% 0%,0% 0%,0% 0%)';
  const hm = (t) => { const m = Math.round(t * 12) * 5; return String(Math.floor(m / 60) % 24).padStart(2, '0') + ':' + String(m % 60).padStart(2, '0'); };
  const win = (st) => st[2] === 'S' ? SWEEP : st[3];

  let L = null;            /* the live build */
  let p = 0;               /* displayed progress, 0..1 */
  let played = false;      /* the one-time enter animation (not pinned) */
  let touched = false;
  let width0 = 0;
  const done = new AbortController();

  function build(p0) {
    const pb = $('.pg.st-b', source), pa = $('.pg.st-a', source);
    const pin = mqPin.matches;
    const ac = new AbortController(); const sig = { signal: ac.signal };
    const wrap = mk('div', 'ba__live');
    const frame = mk('div', 'pg live st-b');
    frame.setAttribute('role', 'group');
    frame.setAttribute('aria-label', 'Slackwater landing page, before and after five fixes');
    const shells = {};
    $$('[data-el]', pb).forEach((eb) => {
      const name = eb.dataset.el, ea = $('[data-el="' + name + '"]', pa), plan = PLAN[name];
      const shell = mk('div', 'el'); shell.dataset.el = name;
      const layers = {};
      const layer = (id, kids) => {
        const ly = mk('div', 'ly ly-' + id); if (id !== 'b') ly.setAttribute('aria-hidden', 'true');
        kids.forEach((c) => ly.appendChild(c)); layers[id] = ly; shell.appendChild(ly); return ly;
      };
      const clones = (src) => Array.from(src.children).map((c) => c.cloneNode(true));
      layer('b', clones(eb));
      const ids = new Set(); plan.forEach((s) => { ids.add(s[0]); ids.add(s[1]); });
      const tw = document.createTreeWalker(layers.b, NodeFilter.SHOW_TEXT), parts = []; while (tw.nextNode()) parts.push(tw.currentNode.nodeValue.trim());
      const words = parts.filter(Boolean).join(' ');
      const mid = (old) => {   /* the new type on the old words */
        const kids = clones(ea), node = kids[0];
        node.classList.add('md'); if (old) node.classList.add('old');
        if (name === 'head') node.innerHTML = '<span>Supercharge your surf</span> <em>planning with AI</em>';
        else {
          const keep = name === 'btn' ? node.querySelector('.ar') : name === 'badge' ? node.querySelector('i') : null;
          node.textContent = words + (name === 'btn' ? ' ' : '');
          if (keep) { if (name === 'btn') node.appendChild(keep); else node.prepend(keep); }
        }
        return kids;
      };
      if (ids.has('1')) {
        if (name === 'focal') { const k = clones(ea); k[0].classList.add('empty'); k[0].innerHTML = ''; layer('1', k); }
        else if (/^p\d$/.test(name)) { const k = clones(eb); k[0].classList.add('dk'); layer('1', k); }
        else if (ids.has('2')) layer('1', mid(true));
        else { const k = clones(ea); k[0].classList.add('old'); layer('1', k); }
      }
      if (ids.has('2')) layer('2', mid(false));
      layer('a', clones(ea));
      frame.appendChild(shell);
      shells[name] = { shell, layers, plan, geo: null, vis: '', clip: {}, op: {} };
    });
    wrap.appendChild(frame);
    const tags = mk('div', 'ba__tags');
    const tagEls = FIX.map((f, i) => {
      const b = mk('button', 'ba__tag t' + (i + 1), String(i + 1)); b.type = 'button';
      b.setAttribute('aria-label', 'Fix ' + (i + 1) + ', ' + f.t + '. Outline what changed.'); b.setAttribute('aria-describedby', 'fix-' + (i + 1));
      b.setAttribute('aria-pressed', 'false'); tags.appendChild(b); return b;
    });
    wrap.appendChild(tags);
    const state = mk('div', 'ba__state');
    state.innerHTML = '<span class="s-b">Typical agent output</span><span class="s-a" aria-hidden="true">Designed with veyUI</span>';
    const cap = mk('div', 'ba__cap'); cap.id = 'ba-cap';
    /* DOM order is reading and tab order: state, controls, then the frame. On narrow screens the caption sits above the frame. */
    const steps = mk('ol', 'ba__steps'); steps.setAttribute('aria-hidden', 'true');
    steps.innerHTML = FIX.map((f, i) => '<li><b>' + (i + 1) + '</b>' + f.t + '</li>').join('');
    let rail = null;
    if (pin) { rail = mk('div', 'ba__rail'); rail.append(state, ui, cap, steps, note); main.prepend(rail); rail.after(wrap); }
    else { main.prepend(ui); main.prepend(state); ui.after(cap); cap.after(wrap); main.append(note); }
    source.remove();
    sec.classList.add('is-live'); sec.classList.toggle('is-pin', pin);
    ui.hidden = false;

    /* Flip: measure the before layout, switch to the after layout, let Flip invert and play the boxes in */
    const moving = Object.values(shells).map((s) => s.shell).filter((s) => !/^(bg|nav)$/.test(s.dataset.el));
    const st0 = FL.getState(moving);
    frame.classList.remove('st-b'); frame.classList.add('st-a');
    {
      const wr = wrap.getBoundingClientRect(), tw = tagEls[0].offsetWidth || 26;
      const tb = (name) => {   /* tight bounds of the text itself, widest over the layers this element passes through */
        let l = 1e9, t = 1e9, rr = -1e9, bt = -1e9, first = 0;
        Object.keys(shells[name].layers).filter((k) => k !== 'b').forEach((k) => {
          const root = shells[name].layers[k].firstElementChild, w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
          while (w.nextNode()) { if (!w.currentNode.nodeValue.trim()) continue; const r = document.createRange(); r.selectNodeContents(w.currentNode); Array.from(r.getClientRects()).forEach((q) => { if (!q.width) return; if (k === 'a' && !first) first = q.height; l = Math.min(l, q.left); t = Math.min(t, q.top); rr = Math.max(rr, q.right); bt = Math.max(bt, q.bottom); }); }
        });
        return l > 1e8 ? shells[name].layers.a.firstElementChild.getBoundingClientRect() : { left: l, top: t, right: rr, bottom: bt, width: rr - l, height: bt - t, first };
      };
      const put = (b, x, y) => { b.style.left = Math.round(x - wr.left) + 'px'; b.style.top = Math.round(y - wr.top) + 'px'; };
      const left = (name, i, line) => { const q = tb(name), lh = line || q.height; put(tagEls[i], q.left - tw - 12, q.top + lh / 2 - tw / 2); };
      const hq = tb('head'); left('head', 0, hq.first || hq.height / 2); left('sub', 4, tb('sub').first); left('btn', 2);
      const pq = shells.focal.layers.a.firstElementChild.getBoundingClientRect();
      put(tagEls[1], pq.left - tw - 8, pq.top + 10); put(tagEls[3], pq.right + 8, pq.top + 10);
    }
    const flip = FL.from(st0, { targets: moving, duration: .17, ease: 'power3.inOut', stagger: .011, scale: true, absolute: false });
    /* geometry of each wrapper in the settled layout, for the frame-wide sweep */
    const FW = frame.clientWidth, FH = frame.clientHeight;
    Object.values(shells).forEach((s) => { const e = s.shell; s.geo = { l: e.offsetLeft, t: e.offsetTop, w: e.offsetWidth, h: e.offsetHeight }; });
    const tl = G.timeline({ paused: true, defaults: { ease: 'none' } });
    tl.add(flip, .20);

    /* the curve draws itself, the go window is marked, then the now marker walks to now */
    const la = shells.focal.layers.a;
    const svg = $$('svg.tide', la).find((s) => s.getBoundingClientRect().width > 0) || $('svg.tide', la);
    const num = (k) => +svg.dataset[k];
    const X0 = num('x0'), X1 = num('x1'), YB = num('yb'), SC = num('s'), VW = svg.viewBox.baseVal.width, FS = num('fs');
    const cv = $('.cv', svg), wn = $('.wn', svg), nw = $('.nw', svg), ln = $('.cl', svg), dot = $('circle', nw), nc = $('.nc', nw), ncr = $('rect', nc), nct = $('text', nc);
    const len = ln.getTotalLength(), N = 300, xs = [], ys = [];
    for (let i = 0; i <= N; i++) { const q = ln.getPointAtLength(len * i / N); xs.push(q.x); ys.push(q.y); }
    const yAt = (x) => { let lo = 0, hi = N; while (hi - lo > 1) { const m = (lo + hi) >> 1; if (xs[m] < x) lo = m; else hi = m; } const f = (x - xs[lo]) / ((xs[hi] - xs[lo]) || 1); return ys[lo] + (ys[hi] - ys[lo]) * f; };
    const NOW = 13 + 40 / 60, START = 12.6; const cur = { t: START }; let lastTxt = '';
    const setCursor = (t) => {
      const x = X0 + t / 24 * (X1 - X0), y = yAt(x), y2 = yAt(x + 1.5);
      const txt = 'Now ' + hm(t) + ', ' + ((YB - y) / SC).toFixed(1) + ' m ' + (y2 <= y ? 'rising' : 'falling');
      dot.setAttribute('cy', y.toFixed(1));
      if (txt !== lastTxt) { nct.textContent = txt; lastTxt = txt; ncr.setAttribute('width', (nct.getComputedTextLength() + 18).toFixed(1)); ncr.setAttribute('x', (-(nct.getComputedTextLength() + 18) / 2).toFixed(1)); }
      const w = +ncr.getAttribute('width') / 2 + 4, cx = clamp(x, X0 + w, X1 - w);
      nw.setAttribute('transform', 'translate(' + x.toFixed(1) + ' 0)'); nc.setAttribute('transform', 'translate(' + (cx - x).toFixed(1) + ' 0)');
    };
    tl.fromTo(cv, { clipPath: 'inset(0% 100% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: .12 }, .62);
    tl.fromTo(wn, { opacity: 0 }, { opacity: 1, duration: .04 }, .72);
    tl.fromTo(nw, { opacity: 0 }, { opacity: 1, duration: .04 }, .76);
    tl.fromTo(cur, { t: START }, { t: NOW, duration: .16, onUpdate: () => setCursor(cur.t) }, .84);
    tagEls.forEach((b, i) => tl.fromTo(b, { opacity: 0, scale: .7 }, { opacity: 1, scale: 1, duration: .03, ease: 'power2.out' }, TAGS[i].at - .03));
    tl.to({}, { duration: .001 }, .999);

    /* layers: every state is computed from progress, so any layer state is reachable in any order */
    const sB = $('.s-b', state), sA = $('.s-a', state);
    const poly = (isIn, xt, xb) => isIn
      ? 'polygon(0% 0%,' + xt.toFixed(2) + '% 0%,' + xb.toFixed(2) + '% 100%,0% 100%)'
      : 'polygon(' + xt.toFixed(2) + '% 0%,100% 0%,100% 100%,' + xb.toFixed(2) + '% 100%)';
    const stageT = (st, v) => { const w = win(st); return clamp((v - w[0]) / (w[1] - w[0]), 0, 1); };
    const edge = (st, t, g) => {
      if (st[2] !== 'S') { const x = t * END; return [x, x - SLASH]; }
      const S = t * END / 100 * FW, sl = SLASH / 100 * FW;
      return [((S - sl * g.t / FH) - g.l) / g.w * 100, ((S - sl * (g.t + g.h) / FH) - g.l) / g.w * 100];
    };
    const renderLayers = (v) => {
      Object.keys(shells).forEach((n) => {
        const s = shells[n], plan = s.plan; let vis = 'b';
        Object.keys(s.layers).forEach((id) => {
          const en = plan.find((st) => st[1] === id), lv = plan.find((st) => st[0] === id);
          let clip = 'none', op = 1;
          if (lv) { const t = stageT(lv, v); if (lv[2] === 'd') op = Math.min(op, clamp(1 - t / .4, 0, 1)); else if (lv[2] === 'c' || lv[2] === 'x') op = Math.min(op, clamp(1 - t / .5, 0, 1)); else if (t >= 1) clip = HID; else if (t > 0) { const e = edge(lv, t, s.geo); clip = poly(false, e[0], e[1]); } }
          if (en && clip === 'none') { const t = stageT(en, v); if (en[2] === 'd') op = Math.min(op, clamp((t - .6) / .4, 0, 1)); else if (en[2] === 'c' || en[2] === 'x') op = Math.min(op, clamp((t - .3) / .5, 0, 1)); else if (t <= 0) clip = HID; else if (t < 1) { const e = edge(en, t, s.geo); clip = poly(true, e[0], e[1]); } }
          const ly = s.layers[id];
          if (s.clip[id] !== clip) { s.clip[id] = clip; ly.style.clipPath = clip; }
          if (s.op[id] !== op) { s.op[id] = op; ly.style.opacity = op === 1 ? '' : op.toFixed(3); }
        });
        plan.forEach((st) => { const w = win(st); if (v >= (w[0] + w[1]) / 2) vis = st[1]; });
        if (s.vis !== vis) { s.vis = vis; Object.keys(s.layers).forEach((id) => { s.layers[id].classList.toggle('on', id === vis); s.layers[id].setAttribute('aria-hidden', String(id !== vis)); }); }
      });
      const t = v >= LABEL ? 1 : 0;
      sB.style.opacity = t ? '0' : '1'; sA.style.opacity = t ? '1' : '0';
      const after = t === 1;
      if (sA.getAttribute('aria-hidden') !== String(!after)) { sA.setAttribute('aria-hidden', String(!after)); sB.setAttribute('aria-hidden', String(after)); }
    };

    L = { ac, wrap, frame, shells, tags: tagEls, state, cap, steps, rail, tl, pin, svg, setCursor, cur, NOW, renderLayers, VW, X0, X1 };
    svg.style.touchAction = 'pan-y';

    /* tag interaction: hover, focus or tap outlines what changed (outline only, no layout) and shows was and now */
    let hover = 0, lock = 0;
    const outline = (k) => {
      Object.values(shells).forEach((s) => s.shell.classList.remove('bhl')); frame.classList.remove('bhl-frame');
      tagEls.forEach((b, i) => b.classList.toggle('is-on', i + 1 === k));
      if (!k) return; const t = TAGS[k - 1];
      if (t.frame) frame.classList.add('bhl-frame'); else t.els.forEach((n) => shells[n] && shells[n].shell.classList.add('bhl'));
    };
    L.preview = () => { const k = hover || lock; outline(k); showCap(k || cur5(p)); };
    tagEls.forEach((b, i) => {
      const k = i + 1;
      b.addEventListener('pointerenter', (e) => { if (e.pointerType !== 'touch') { hover = k; L.preview(); } }, sig);
      b.addEventListener('pointerleave', () => { if (hover === k) { hover = 0; L.preview(); } }, sig);
      b.addEventListener('focus', () => { hover = k; L.preview(); }, sig);
      b.addEventListener('blur', () => { if (hover === k) { hover = 0; L.preview(); } }, sig);
      b.addEventListener('click', () => { lock = lock === k ? 0 : k; tagEls.forEach((x, j) => x.setAttribute('aria-pressed', String(lock === j + 1))); L.preview(); }, sig);
    });
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && (lock || hover)) { lock = 0; hover = 0; tagEls.forEach((x) => x.setAttribute('aria-pressed', 'false')); L.preview(); } }, sig);

    /* pointer on the chart moves the now marker once the morph has settled */
    svg.addEventListener('pointermove', (e) => {
      if (p < .985 || e.pointerType === 'touch') return;
      const r = svg.getBoundingClientRect(); const x = (e.clientX - r.left) / r.width * VW;
      G.killTweensOf(cur); cur.t = clamp((x - X0) / (X1 - X0) * 24, 0, 24); setCursor(cur.t);
    }, sig);
    svg.addEventListener('pointerleave', () => { if (p >= .985) G.to(cur, { t: NOW, duration: .5, ease: 'power2.out', overwrite: true, onUpdate: () => setCursor(cur.t) }); }, sig);

    /* scroll drives the same progress when pinned; otherwise the morph plays once when the frame enters the view */
    if (pin) {
      L.trig = ST.create({ trigger: runway, start: 'top top', end: 'bottom bottom', onUpdate: (s) => goto(s.progress), onRefresh: (s) => { if (L && L.trig === s) setProgress(s.progress); } });
    } else if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((es) => {
        if (es[0].isIntersecting && !played && !touched) { played = true; goto(1, 3.6, 'power1.inOut'); io.disconnect(); }
      }, { threshold: .55 });
      io.observe(frame); ac.signal.addEventListener('abort', () => io.disconnect());
    } else { played = true; }
    /* one quiet ring on the After button the first time the control is seen, so the At rest page hints at the result */
    if (!pinged && 'IntersectionObserver' in window) {
      const sg = $('.ba__seg'), io2 = new IntersectionObserver((es) => {
        if (es[0].isIntersecting && !pinged) { pinged = true; sg.classList.add('ping'); sg.addEventListener('animationend', () => sg.classList.remove('ping'), { once: true }); io2.disconnect(); }
      }, { threshold: 1 });
      io2.observe(sg); ac.signal.addEventListener('abort', () => io2.disconnect());
    }
    width0 = Math.round(wrap.getBoundingClientRect().width);
    reserveCap(cap);
    setProgress(L.trig ? L.trig.progress : p0);
  }
  let pinged = false;

  function teardown() {
    if (!L) return;
    L.ac.abort(); if (L.trig) L.trig.kill(); G.killTweensOf(L.tl); G.killTweensOf(L.cur); L.tl.kill();
    main.append(ui, note);
    [L.wrap, L.state, L.cap, L.steps, L.rail].forEach((n) => n && n.remove());
    L = null;
  }
  function fallback() {
    teardown(); sec.classList.remove('is-live', 'is-pin'); ui.hidden = true;
    if (!source.isConnected) main.prepend(source);
  }

  function applying(v) { for (let i = 0; i < TAGS.length; i++) if (v < TAGS[i].at) return i + 1; return 5; }
  /* one rule for the current fix: the one being applied (0 at rest before the first change). Range text, caption, list and steps all use it. */
  function cur5(v) { return v < .02 ? 0 : applying(v); }
  const capHtml = (k) => {
    if (!k) return '<span class="idle">Five fixes turn the left into the right. Scroll, or press After, to see them one by one.</span>';
    const f = FIX[k - 1];
    return '<span class="bc-n">' + k + '</span><span class="bc-t">' + f.t + '</span><span class="bc-w"><b>Was</b>' + f.was + '</span><span class="bc-s"><b>Now</b>' + f.now + '</span>';
  };
  function showCap(k) {
    if (!L) return; const key = String(k);
    if (L.cap.dataset.k === key) return; L.cap.dataset.k = key; L.cap.innerHTML = capHtml(k);
  }
  /* reserve the tallest caption so the bar never changes height while the viewer scrubs */
  function reserveCap(cap) {
    cap.style.minHeight = ''; let h = 0;
    for (let k = 0; k <= 5; k++) { cap.innerHTML = capHtml(k); h = Math.max(h, cap.offsetHeight); }
    cap.style.minHeight = h + 'px'; cap.dataset.k = '';
  }
  function sync(v) {
    if (!L) return; p = v;
    L.renderLayers(v);
    const pct = Math.round(v * 100);
    if (+range.value !== pct) range.value = pct;
    range.style.setProperty('--fill', pct + '%');
    const vt = v < .02 ? 'Before' : v > .98 ? 'After' : 'Fix ' + applying(v) + ' of 5, ' + FIX[applying(v) - 1].t;
    if (range.getAttribute('aria-valuetext') !== vt) range.setAttribute('aria-valuetext', vt);
    const after = v >= .5;
    seg.forEach((b, i) => { const on = (i === 1) === after; b.setAttribute('aria-checked', String(on)); b.tabIndex = on ? 0 : -1; });
    const k = cur5(v);
    fixLis.forEach((li, i) => li.classList.toggle('is-on', i + 1 === k));
    Array.from(L.steps.children).forEach((li, i) => li.classList.toggle('is-on', i + 1 === k));

    L.frame.classList.toggle('is-done', v >= .985);
    L.tags.forEach((b, i) => b.classList.toggle('live', v >= TAGS[i].at - .03));
    L.svg.style.pointerEvents = v >= .985 ? 'auto' : 'none';
    L.preview();
  }
  function setProgress(v) { if (!L) return; G.killTweensOf(L.tl); L.tl.progress(v); sync(v); }
  function goto(v, dur = .45, ease = 'power2.out') {
    if (!L) return; v = clamp(v, 0, 1);
    if (!dur) { setProgress(v); return; }
    G.to(L.tl, { progress: v, duration: dur, ease, overwrite: true, onUpdate: () => sync(L.tl.progress()) });
  }
  /* controls: pinned, they move the page (scroll stays the single source); otherwise they drive progress directly */
  function seek(v, smooth) {
    touched = true;
    if (L.pin && L.trig) {
      const top = L.trig.start + v * (L.trig.end - L.trig.start);
      if (!smooth) { scrollTo({ top, behavior: 'instant' }); goto(v, .2); }
      else {
        const o = { y: scrollY }, off = () => ['wheel', 'touchstart', 'keydown', 'pointerdown'].forEach((t) => removeEventListener(t, stop));
        const tw = G.to(o, { y: top, duration: clamp(Math.abs(top - scrollY) / 1400, .5, 2), ease: 'power2.inOut', onUpdate: () => scrollTo(0, o.y), onComplete: off });
        const stop = () => { tw.kill(); off(); };
        setTimeout(() => ['wheel', 'touchstart', 'keydown', 'pointerdown'].forEach((t) => addEventListener(t, stop, { passive: true })), 80);
      }
    } else goto(v, smooth ? 1.4 : .2);
  }
  range.addEventListener('input', () => seek(+range.value / 100, false), { signal: done.signal });
  seg.forEach((b, i) => {
    b.addEventListener('click', () => seek(i, true), { signal: done.signal });
    b.addEventListener('keydown', (e) => {
      let to = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') to = 1; else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') to = 0;
      else if (e.key === 'Home') to = 0; else if (e.key === 'End') to = 1;
      if (to == null) return; e.preventDefault(); seg[to].focus(); seek(to, true);
    }, { signal: done.signal });
  });

  /* rebuild when the layout class changes (pin mode, compact versus wide), keeping progress */
  let rt = 0;
  const maybeRebuild = () => {
    clearTimeout(rt);
    rt = setTimeout(() => {
      if (!L) return;
      const w = Math.round(L.wrap.getBoundingClientRect().width);
      if (mqPin.matches === L.pin && Math.abs(w - width0) < 8) { ST.refresh(); return; }
      const keep = p, ae = document.activeElement;
      const was = ae === range ? 'range' : seg.includes(ae) ? 's' + seg.indexOf(ae) : ae && ae.classList && ae.classList.contains('ba__tag') ? 't' + [...ae.parentNode.children].indexOf(ae) : '';
      teardown(); try { build(keep); } catch (e) { console.warn('ba: static fallback', e); fallback(); return; }
      if (was === 'range') range.focus({ preventScroll: true }); else if (was[0] === 's') seg[+was[1]].focus({ preventScroll: true }); else if (was[0] === 't' && L.tags[+was.slice(1)]) L.tags[+was.slice(1)].focus({ preventScroll: true });
    }, 220);
  };
  addEventListener('resize', maybeRebuild, { signal: done.signal });
  mqPin.addEventListener('change', maybeRebuild, { signal: done.signal });

  try { build(0); } catch (e) { console.warn('ba: static fallback', e); fallback(); return; }
  requestAnimationFrame(() => ST.refresh());
  /* a restored scroll position (reload, back) or another section's refresh must never leave the frame at Before */
  ST.addEventListener('refresh', () => { if (L && L.trig) setProgress(L.trig.progress); });
  addEventListener('load', () => { if (L && L.trig) setTimeout(() => setProgress(L.trig.progress), 60); }, { once: true });
}
