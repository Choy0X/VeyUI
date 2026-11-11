/* veyUI landing. Plain ES module, GSAP + ScrollTrigger + Flip from assets/vendor/. ASCII only. */
const root = document.documentElement;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const reduce = root.classList.contains('rm') || matchMedia('(prefers-reduced-motion: reduce)').matches;
const finePointer = matchMedia('(pointer: fine)').matches;
const mqPin = matchMedia('(min-width: 900px) and (min-height: 600px)');
const G = window.gsap, ST = window.ScrollTrigger, FL = window.Flip;
const canAnimate = !reduce && !!G && !!ST;
if (canAnimate) { G.registerPlugin(ST); if (FL) G.registerPlugin(FL); ST.config({ ignoreMobileResize: true }); }

/* ============ always-on features (work without animation) ============ */

/* chips and mode chips get an inner span so a magnet offset never fights positioning transforms */
$$('.chip').forEach((b) => { if (!b.firstElementChild) { const s = document.createElement('span'); s.textContent = b.textContent; b.textContent = ''; b.appendChild(s); } });

/* copy buttons */
const status = document.createElement('div');
status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
status.style.cssText = 'position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap';
document.body.appendChild(status);
async function copyText(text) {
  try { await navigator.clipboard.writeText(text); return true; } catch (e) {
    const ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly', ''); ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
    document.body.appendChild(ta); ta.select(); ta.setSelectionRange(0, text.length);
    let ok = false; try { ok = document.execCommand('copy'); } catch (_) { ok = false; }
    ta.remove(); return ok;
  }
}
$$('.copy').forEach((btn) => {
  const label = $('span', btn); const orig = label.textContent; let t;
  btn.addEventListener('click', async () => {
    const ok = await copyText(btn.dataset.copy);
    label.textContent = ok ? 'Copied' : 'Press Ctrl+C';
    btn.classList.toggle('is-ok', ok);
    status.textContent = ok ? 'Copied to clipboard: ' + btn.dataset.copy : 'Copy failed. Select the command and copy it manually.';
    clearTimeout(t); t = setTimeout(() => { label.textContent = orig; btn.classList.remove('is-ok'); }, 1800);
  });
});

/* install tabs (arrow keys, home, end) */
(() => {
  const tabs = $$('[role="tab"]'); if (!tabs.length) return;
  const select = (tab, focus) => {
    tabs.forEach((t) => {
      const on = t === tab; t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
      $('#' + t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => select(t));
    t.addEventListener('keydown', (e) => {
      let n = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = tabs[(i + 1) % tabs.length];
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = tabs[(i - 1 + tabs.length) % tabs.length];
      else if (e.key === 'Home') n = tabs[0]; else if (e.key === 'End') n = tabs[tabs.length - 1];
      if (n) { e.preventDefault(); select(n, true); }
    });
  });
})();

/* FAQ accordion */
$$('.acc__btn').forEach((b) => {
  b.addEventListener('click', () => {
    const open = b.getAttribute('aria-expanded') === 'true';
    b.setAttribute('aria-expanded', String(!open));
    $('#' + b.getAttribute('aria-controls')).classList.toggle('is-open', !open);
    if (window.ScrollTrigger) setTimeout(() => ScrollTrigger.refresh(), 450);
  });
});

/* nav: sliding marker, active section, mobile drawer */
(() => {
  const nav = $('#nav'), links = $$('.nav__links a'), marker = $('.nav__marker'), ul = $('.nav__links');
  let active = null;
  const place = (a) => {
    if (!a || !marker) { if (marker) marker.classList.remove('on'); return; }
    marker.classList.add('on');
    marker.style.transform = 'translateX(' + a.offsetLeft + 'px) scaleX(' + (a.offsetWidth / 100).toFixed(3) + ')';
  };
  const setActive = (id) => {
    active = links.find((a) => a.getAttribute('href') === '#' + id) || null;
    links.forEach((a) => a === active ? a.setAttribute('aria-current', 'true') : a.removeAttribute('aria-current'));
    place(active);
  };
  if (ul) {
    links.forEach((a) => a.addEventListener('pointerenter', () => place(a)));
    links.forEach((a) => a.addEventListener('focus', () => place(a)));
    ul.addEventListener('pointerleave', () => place(active));
    ul.addEventListener('focusout', () => place(active));
    addEventListener('resize', () => place(active));
    marker.style.transition = 'opacity .2s, transform .4s cubic-bezier(.34,1.5,.5,1)';
  }
  const ids = ['run', 'choice', 'evidence', 'modes', 'install', 'faq'];
  const vis = new Map();
  const io = new IntersectionObserver((es) => {
    es.forEach((e) => vis.set(e.target.id, e.isIntersecting));
    const cur = ids.find((id) => vis.get(id));
    setActive(cur || null);
  }, { rootMargin: '-45% 0px -50% 0px' });
  ids.forEach((id) => { const el = document.getElementById(id); if (el) io.observe(el); });
  const menu = $('.nav__menu'), drawer = $('#drawer');
  if (menu) {
    const close = () => { drawer.hidden = true; menu.setAttribute('aria-expanded', 'false'); $('.nav__menu-t').textContent = 'Menu'; };
    menu.addEventListener('click', () => {
      const open = drawer.hidden; drawer.hidden = !open; menu.setAttribute('aria-expanded', String(open));
      $('.nav__menu-t').textContent = open ? 'Close' : 'Menu';
    });
    drawer.addEventListener('click', (e) => { if (e.target.closest('a')) close(); });
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && !drawer.hidden) { close(); menu.focus(); } });
  }
})();

/* nav: dark styling while the hero sits under it */
(() => {
  const nav = $('#nav'), hero = $('#top'); if (!nav || !hero) return;
  let io = null;
  const watch = () => { if (io) io.disconnect(); io = new IntersectionObserver((es) => nav.classList.toggle('on-dark', es[0].isIntersecting), { rootMargin: '-44px 0px -' + Math.max(0, innerHeight - 46) + 'px 0px' }); io.observe(hero); };
  watch(); addEventListener('resize', () => { clearTimeout(watch.t); watch.t = setTimeout(watch, 200); });
})();

/* ============ hero proof: one page twice, a slanted divider that sweeps, follows the pointer, drags and has a real range ============ */
(() => {
  const proof = $('.proof'); if (!proof) return;
  const view = $('.proof__view', proof), range = $('.proof__range', proof), pp = $('.proof__pp', proof), ppText = $('span', pp), ppUse = $('use', pp);
  const LO = 22, HI = 78, LEG = 3000, DWELL = 700;
  let p = 50, target = 50, dir = -1, from = 50, to = LO, t0 = 0, dur = LEG, dwellUntil = 0, raf = 0, last = '';
  let userPaused = false, inView = true, hover = false, drag = false, focusRange = false, focusPP = false, touch = null, holdUntil = 0, holdTimer = 0, sl = 36;
  const reduceNow = () => reduce || root.classList.contains('rm');

  const render = () => {
    proof.style.setProperty('--p', p.toFixed(2));
    const v = Math.round(p);
    if (+range.value !== v) range.value = v;
    const txt = v <= 0 ? 'Designed page only' : v >= 100 ? 'Typical page only' : (100 - v) + ' percent designed, ' + v + ' percent typical';
    if (txt !== last) { last = txt; range.setAttribute('aria-valuetext', txt); }
  };
  const fromX = (cx) => {
    const r = view.getBoundingClientRect();
    return clamp(((cx - r.left) + sl) / (r.width / 100 + sl / 50), 0, 100);
  };
  const auto = () => !reduceNow() && !userPaused && inView && !hover && !drag && !focusRange && !focusPP && !document.hidden && performance.now() >= holdUntil;
  const leg = () => { from = p; to = dir > 0 ? HI : LO; dur = Math.max(450, LEG * Math.abs(to - from) / (HI - LO)); t0 = performance.now(); };
  let wasAuto = false;
  const frame = (now) => {
    raf = 0;
    const a = auto();
    if (a) {
      if (!wasAuto) { dwellUntil = 0; leg(); }
      if (dwellUntil) { if (now >= dwellUntil) { dwellUntil = 0; leg(); } }
      else {
        const k = Math.min(1, (now - t0) / dur);
        p = from + (to - from) * (0.5 - Math.cos(Math.PI * k) / 2);
        target = p;
        if (k >= 1) { dir = -dir; dwellUntil = now + DWELL; }
      }
    } else if (Math.abs(target - p) > 0.04) {
      p += (target - p) * 0.2;
    } else { p = target; }
    wasAuto = a;
    render();
    if (a || Math.abs(target - p) > 0.04) raf = requestAnimationFrame(frame);
    else wasAuto = false;
  };
  const kick = () => { if (!raf && (auto() || Math.abs(target - p) > 0.04)) raf = requestAnimationFrame(frame); };
  const hold = (ms) => { holdUntil = performance.now() + ms; clearTimeout(holdTimer); holdTimer = setTimeout(kick, ms + 20); };
  const setNow = (v) => { p = target = clamp(v, 0, 100); wasAuto = false; render(); };

  view.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') { sl = parseFloat(getComputedStyle(view).getPropertyValue('--sl')) || 36; hover = true; } });
  view.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse') { hover = false; if (!drag) kick(); } });
  view.addEventListener('pointermove', (e) => {
    if (drag) { setNow(fromX(e.clientX)); return; }
    if (e.pointerType === 'mouse' && !reduceNow()) { target = fromX(e.clientX); kick(); }
  });

  view.addEventListener('pointerdown', (e) => {
    if (e.button > 0) return;
    sl = parseFloat(getComputedStyle(view).getPropertyValue('--sl')) || 36;
    if (e.pointerType === 'mouse') { drag = true; try { view.setPointerCapture(e.pointerId); } catch (_) {} setNow(fromX(e.clientX)); }
    else touch = { x: e.clientX, y: e.clientY, id: e.pointerId };
  });
  view.addEventListener('pointermove', (e) => {
    if (!touch || drag || e.pointerId !== touch.id) return;
    const dx = e.clientX - touch.x, dy = e.clientY - touch.y;
    if (Math.abs(dx) > 6 && Math.abs(dx) > Math.abs(dy)) { drag = true; try { view.setPointerCapture(e.pointerId); } catch (_) {} setNow(fromX(e.clientX)); }
  });
  const endDrag = (e) => {
    const was = drag, tapT = touch && !drag && e.type === 'pointerup' ? touch : null; touch = null;
    if (tapT) { setNow(fromX(e.clientX)); hold(4000); return; }
    if (!was) return; drag = false; if (e.pointerType !== 'mouse') hold(4000); else kick();
  };
  view.addEventListener('pointerup', endDrag); view.addEventListener('pointercancel', endDrag);

  range.addEventListener('input', () => { setNow(+range.value); hold(4000); });
  range.addEventListener('keydown', (e) => {
    const k = e.key; const d = (k === 'ArrowLeft' || k === 'ArrowDown') ? -5 : (k === 'ArrowRight' || k === 'ArrowUp') ? 5 : 0;
    if (d) { e.preventDefault(); setNow(Math.round(p / 5) * 5 + d); }
  });
  range.addEventListener('focus', () => { focusRange = true; });
  range.addEventListener('blur', () => { focusRange = false; hold(1200); });

  pp.addEventListener('focus', () => { focusPP = pp.matches(':focus-visible'); });
  pp.addEventListener('blur', () => { focusPP = false; });

  pp.addEventListener('click', () => {
    userPaused = !userPaused; holdUntil = 0; focusPP = false;
    ppText.textContent = userPaused ? 'Play sweep' : 'Pause sweep';
    ppUse.setAttribute('href', userPaused ? '#i-play' : '#i-pause');
    kick();
  });

  new IntersectionObserver((es) => { inView = es[0].isIntersecting; if (inView) kick(); }, { rootMargin: '0px' }).observe(proof);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) kick(); });

  render();
  proof.classList.add('is-live');
  if (!reduceNow()) { hold(1600); }
})();

/* ============ hero field: the CSS dot grid lights up lime around the pointer and trails it (one small canvas that follows the pointer) ============ */
(() => {
  const hero = $('#top'), glow = $('.hero__glow'); if (!hero || !glow) return;
  if (reduce || root.classList.contains('rm') || !matchMedia('(pointer: fine)').matches) { glow.hidden = true; return; }
  let g2 = null; try { g2 = glow.getContext('2d'); } catch (e) { g2 = null; }
  if (!g2) { glow.hidden = true; return; }
  const R = 190, TAU = Math.PI * 2;
  let step = 26, S = 0, dpr = 1, tx = 0, ty = 0, mx = 0, my = 0, I = 0, inside = false, activeUntil = 0, raf = 0, vis = true, rects = [], shown = false;

  const size = () => {
    dpr = Math.min(devicePixelRatio || 1, 1.5); step = innerWidth < 700 ? 22 : 26; S = Math.ceil((R + step) * 2);
    glow.width = Math.round(S * dpr); glow.height = Math.round(S * dpr); glow.style.width = S + 'px'; glow.style.height = S + 'px';
    measure();
  };

  const measure = () => {
    const hr = hero.getBoundingClientRect();
    rects = $$('.hl, .hero__sub, .hbtn, .hero .cmd, .hero__meta span').map((el) => { const r = el.getBoundingClientRect(); return [r.left - hr.left - 12, r.top - hr.top - 8, r.right - hr.left + 12, r.bottom - hr.top + 8]; });
  };
  const clearance = (x, y) => {
    let m = 1;
    for (const r of rects) { const d = Math.hypot(Math.max(r[0] - x, 0, x - r[2]), Math.max(r[1] - y, 0, y - r[3])); if (d < 34) m = Math.min(m, 0.06 + 0.94 * d / 34); }
    return m;
  };
  size();
  if (typeof ResizeObserver === 'function') { let t = 0; new ResizeObserver(() => { clearTimeout(t); t = setTimeout(size, 120); }).observe(hero); } else addEventListener('resize', size);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);

  const draw = () => {
    g2.setTransform(dpr, 0, 0, dpr, 0, 0); g2.clearRect(0, 0, S, S);
    if (I < 0.01) { if (shown) { glow.style.visibility = 'hidden'; shown = false; } return; }
    if (!shown) { glow.style.visibility = 'visible'; shown = true; }
    const ox = mx - S / 2, oy = my - S / 2, c = S / 2;
    glow.style.transform = 'translate(' + ox.toFixed(2) + 'px,' + oy.toFixed(2) + 'px)';
    g2.globalCompositeOperation = 'lighter';
    const gr = g2.createRadialGradient(c, c, 0, c, c, R * 1.15);
    gr.addColorStop(0, 'rgba(214,255,61,' + (0.13 * I).toFixed(3) + ')'); gr.addColorStop(1, 'rgba(214,255,61,0)');
    g2.fillStyle = gr; g2.fillRect(0, 0, S, S);
    const c0 = Math.floor(ox / step), c1 = Math.ceil((ox + S) / step), r0 = Math.floor(oy / step), r1 = Math.ceil((oy + S) / step);
    for (let r = r0; r < r1; r++) for (let q = c0; q < c1; q++) {
      const x = q * step + step / 2, y = r * step + step / 2, d = Math.hypot(x - mx, y - my); if (d >= R) continue;
      const k = 1 - d / R, a = (0.08 + k * k * 0.46) * I * clearance(x, y); if (a < 0.015) continue;
      g2.fillStyle = 'rgba(230,255,61,' + a.toFixed(3) + ')';
      g2.beginPath(); g2.arc(x - ox, y - oy, 1.2 + k * k * 2.2, 0, TAU); g2.fill();
    }
    g2.globalCompositeOperation = 'source-over';
  };
  const frame = (now) => {
    raf = 0;
    const on = inside && now < activeUntil;
    I += ((on ? 1 : 0) - I) * (on ? 0.2 : 0.12);
    mx += (tx - mx) * 0.17; my += (ty - my) * 0.17;
    draw();
    if (vis && !document.hidden && (I > 0.01 || (on && Math.hypot(tx - mx, ty - my) > 0.4))) raf = requestAnimationFrame(frame);
    else { I = 0; draw(); }
  };
  const wake = () => { if (!raf && vis && !document.hidden) raf = requestAnimationFrame(frame); };

  hero.addEventListener('pointerenter', measure, { passive: true });
  hero.addEventListener('pointermove', (e) => {
    if (e.pointerType === 'touch') return;
    const r = hero.getBoundingClientRect(); tx = e.clientX - r.left; ty = e.clientY - r.top;
    if (!inside || I < 0.02) { mx = tx; my = ty; }
    inside = true; activeUntil = performance.now() + 1500; wake();
  }, { passive: true });
  hero.addEventListener('pointerleave', () => { inside = false; wake(); });
  new IntersectionObserver((es) => { vis = es[0].isIntersecting; if (!vis) { if (raf) cancelAnimationFrame(raf); raf = 0; I = 0; draw(); } }).observe(hero);
  document.addEventListener('visibilitychange', () => { if (document.hidden) { if (raf) cancelAnimationFrame(raf); raf = 0; I = 0; draw(); } });
})();

/* pressed state for keyboard activation (Space / Enter) so buttons squash for everyone */
document.addEventListener('keydown', (e) => { if ((e.key === ' ' || e.key === 'Enter') && e.target.classList && e.target.classList.contains('btn')) e.target.classList.add('is-down'); });
document.addEventListener('keyup', (e) => { if (e.target.classList && e.target.classList.contains('btn')) e.target.classList.remove('is-down'); });

/* ============ evidence: real records, port of design_library.py search ============ */
const RECORDS = [
  { id: 'E003', product: 'Proton Account', platform: 'web', name: 'Plan comparison dialog', pattern: 'pricing', tags: ['subscription', 'comparison', 'plans'], layout: 'A dialog title sits above audience tabs and billing controls. Three adjacent plan columns repeat the same hierarchy: name, short description, prominent price, selection action, and feature rows. The middle option carries a recommendation badge and stronger outline; a close control occupies the corner.', lesson: 'Keep prices and primary actions aligned across plans, and distinguish recommendations without breaking the shared comparison structure.' },
  { id: 'M012', product: 'Notion: Notes, Tasks, AI', platform: 'mobile', name: 'Notes database list', pattern: 'list', tags: ['notes', 'database', 'search', 'filters'], layout: 'The page title and database controls occupy the top area. A dense list of note titles uses small leading icons and quiet row separators; creation, search and view options stay in the same toolbar.', lesson: 'Preserve room for real titles by keeping database chrome compact.' },
  { id: 'M005', product: 'Todoist: To Do List & Calendar', platform: 'mobile', name: 'Task display configuration', pattern: 'settings', tags: ['tasks', 'layout', 'settings', 'filters'], layout: 'A top-level layout choice uses three visual options. Below it, completion settings and sorting/grouping values occupy distinct row groups. Cancel and confirm flank the sheet title.', lesson: 'Give representation choices a visual preview while keeping secondary display controls compact.' },
  { id: 'F031', product: 'GitHub Desktop', platform: 'desktop', name: 'Repository clean-state guidance', pattern: 'empty', tags: ['git', 'empty-state', 'pull-request'], layout: 'A large clean-state heading and one explanatory sentence lead the panel, with a small illustration at the right. A broad recommendation box below pairs a task heading, explanatory text, and shortcut hints on the left with a prominent split action button on the right.', lesson: 'Explain what an empty state means, then offer one relevant next step with its action placed beside the supporting rationale.' },
  { id: 'W042', product: 'Linear', platform: 'web', name: 'New automation starting state', pattern: 'empty', tags: ['automation', 'onboarding', 'prompt'], layout: 'A stable workspace sidebar leads to a spacious creation area. The main prompt field is centered below the page heading, followed by a small grid of suggested use cases. The suggestions are secondary starting points rather than competing primary actions.', lesson: 'Offer concrete starting examples without obscuring the user\'s own input path.' },
  { id: 'E076', product: 'Bitwarden', platform: 'web', name: 'Shared item email verification error', pattern: 'form', tags: ['sharing', 'verification', 'error'], layout: 'A centered illustration and verification heading lead into a single-field form card. The required email input shows a visible validation message beneath it, followed by a subdued send-code button. A short product explanation with links sits outside the card below the form.', lesson: 'Place field errors directly beside the affected input, and distinguish task completion controls from secondary explanatory or promotional links.' }
];
(() => {
  const ALIASES = { signin: 'authentication', login: 'authentication', signup: 'onboarding', billing: 'payment', checkout: 'payment', preferences: 'settings', inbox: 'messages', dashboard: 'overview', todos: 'tasks', todo: 'tasks', kanban: 'board', profile: 'account', filtering: 'filter', searching: 'search', editor: 'editing', notifications: 'notification', permission: 'permissions', errors: 'error', validation: 'error', validate: 'error', paywall: 'pricing', tiers: 'pricing', plans: 'pricing', onboard: 'onboarding', edit: 'editing', filters: 'filter', failed: 'error', failure: 'error', invalid: 'error' };
  const STOP = new Set(['a', 'an', 'the', 'for', 'of', 'and', 'or', 'with', 'to', 'in', 'ui', 'screen', 'design', 'app', 'please', 'me', 'create', 'build', 'implement', 'new']);
  const PURPOSES = new Set(['authentication', 'onboarding', 'pricing', 'error', 'permissions']);
  const words = (v) => new Set((v.toLowerCase().replace(/sign in/g, 'signin').replace(/sign up/g, 'signup').replace(/log in/g, 'login').match(/[a-z0-9]+/g) || []).filter((t) => !STOP.has(t)).map((t) => ALIASES[t] || t));
  const inter = (a, b) => { const r = new Set(); a.forEach((x) => { if (b.has(x)) r.add(x); }); return r; };
  const union = (...sets) => { const r = new Set(); sets.forEach((s) => s.forEach((x) => r.add(x))); return r; };
  function search(query) {
    const terms = words(query); const out = []; if (!terms.size) return out;
    const purposes = inter(terms, PURPOSES);
    RECORDS.forEach((s) => {
      const tags = words(s.tags.join(' ') + ' ' + s.pattern);
      let ok = true; purposes.forEach((p) => { if (!tags.has(p)) ok = false; });
      if (!ok) return;
      if (terms.has('error') && terms.has('payment') && !tags.has('payment')) return;
      const f = [words(s.tags.join(' ') + ' ' + s.name), words(s.layout), words(s.product), words(s.pattern)];
      const matches = inter(union(...f), terms); if (!matches.size) return;
      const score = 30 * matches.size + 12 * inter(terms, f[0]).size + 5 * inter(terms, f[3]).size + 2 * inter(terms, f[1]).size + inter(terms, f[2]).size;
      out.push({ score, s, matches });
    });
    return out.sort((a, b) => b.score - a.score || (a.s.id < b.s.id ? -1 : 1)).slice(0, 3);
  }
  const list = $('#results'), meta = $('#qmeta'), input = $('#q'), form = $('#qform'); if (!list) return;
  const esc = (t) => t.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const cards = new Map();
  RECORDS.forEach((r) => {
    const li = document.createElement('li'); li.className = 'rcard'; li.dataset.id = r.id; li.hidden = true;
    const pc = r.platform === 'mobile' ? 'tag--m' : r.platform === 'desktop' ? 'tag--d' : 'tag--w';
    li.innerHTML = '<div class="rcard__top"><span class="tag">' + r.id + '</span><span class="tag ' + pc + '">' + r.platform + '</span><span class="tag tag--p">' + esc(r.pattern) + '</span><span class="rcard__m"></span></div>' +
      '<h3>' + esc(r.name) + '</h3><p class="rcard__prod">' + esc(r.product) + '</p><p class="rcard__lay">' + esc(r.layout) + '</p>' +
      '<p class="rcard__les"><b>Lesson</b>' + esc(r.lesson) + '</p>';
    list.appendChild(li); cards.set(r.id, li);
  });
  function run(query, animate) {
    const hits = search(query); const ids = new Set(hits.map((h) => h.s.id));
    const state = animate && FL && canAnimate ? FL.getState(Array.from(cards.values()).filter((c) => !c.hidden)) : null;
    cards.forEach((c, id) => {
      const h = hits.find((x) => x.s.id === id);
      c.hidden = !ids.has(id);
      if (h) $('.rcard__m', c).textContent = 'matched: ' + Array.from(h.matches).join(', ');
    });
    // keep ranked order: append in rank order
    hits.forEach((h) => list.appendChild(cards.get(h.s.id)));
    if (!query.trim()) meta.textContent = 'Type a task or pick a chip. Example: empty state, pricing, settings.';
    else if (!hits.length) meta.textContent = 'No matching reviewed screen among the 6 loaded records. The real tool says: "No matching reviewed screen; use labeled guidance and record the gap. No automatic source browsing."';
    else meta.textContent = hits.length + ' of 6 loaded records match "' + query.trim() + '". The full library holds 583.';
    if (state) {
      FL.from(state, { duration: .5, ease: 'power3.out', absolute: false, nested: true,
        onEnter: (els) => G.fromTo(els, { opacity: 0, y: 24, scale: .96 }, { opacity: 1, y: 0, scale: 1, duration: .45, ease: 'power3.out', stagger: .06 }),
        onLeave: (els) => G.to(els, { opacity: 0, duration: .2 }) });
    }
  }
  form.addEventListener('submit', (e) => { e.preventDefault(); run(input.value, true); });
  input.addEventListener('input', () => run(input.value, true));
  $$('.q__chips .chip').forEach((c) => c.addEventListener('click', () => { input.value = c.dataset.q; run(c.dataset.q, true); }));
  input.value = 'empty state'; run(input.value, false);
})();

/* ============ modes: eight cards, press, drag onto another to swap, shuffle ============ */
(() => {
  const board = $('#board'); if (!board) return;
  const chips = $$('.mchip', board), line = $('#mline'), shuffleBtn = $('#shuffle'), sr = $('#mode-sr');
  let typing = null;
  const order = () => $$('.mchip', board);
  const type = (text) => {
    clearInterval(typing);
    if (!canAnimate) { line.textContent = text; return; }
    let i = 0; line.textContent = '';
    typing = setInterval(() => { i += 2; line.textContent = text.slice(0, i); if (i >= text.length) clearInterval(typing); }, 16);
  };
  const choose = (chip, speak = true) => {
    order().forEach((c) => { const on = c === chip; c.setAttribute('aria-checked', String(on)); c.tabIndex = on ? 0 : -1; });
    if (speak) { type(chip.dataset.s); sr.textContent = ''; setTimeout(() => { sr.textContent = chip.dataset.s; }, 30); } else line.textContent = chip.dataset.s;
    if (canAnimate) G.fromTo(chip, { scale: 1.06 }, { scale: 1, duration: .6, ease: 'elastic.out(1,.5)' });
  };
  chips.forEach((c, i) => { c.tabIndex = i === 0 ? 0 : -1; });
  const rots = [-1.4, 1, -.8, 1.3, .9, -1.2, 1.1, -.9];
  if (canAnimate) chips.forEach((c, i) => G.set(c, { rotation: rots[i] }));
  board.addEventListener('keydown', (e) => {
    const cs = order(); const cur = cs.indexOf(document.activeElement); if (cur < 0) return;
    let n = null;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = cs[(cur + 1) % cs.length];
    else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = cs[(cur - 1 + cs.length) % cs.length];
    else if (e.key === 'Home') n = cs[0]; else if (e.key === 'End') n = cs[cs.length - 1];
    if (n) { e.preventDefault(); n.focus(); choose(n); }
  });
  const swap = (a, b) => {
    const st = FL && canAnimate ? FL.getState(order()) : null;
    const ph = document.createElement('span'); a.before(ph); b.before(a); ph.replaceWith(b);
    if (canAnimate) G.set(a, { x: 0, y: 0 });
    if (st) FL.from(st, { duration: .55, ease: 'power3.inOut', absolute: false });
  };
  let drag = null;
  board.addEventListener('pointerdown', (e) => {
    if (!canAnimate || e.button > 0 || e.pointerType === 'touch') return;
    const c = e.target.closest('.mchip'); if (!c) return;
    drag = { c, sx: e.clientX, sy: e.clientY, moved: false, id: e.pointerId, rot: G.getProperty(c, 'rotation') };
    c.setPointerCapture(e.pointerId);
  });
  board.addEventListener('pointermove', (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    const dx = e.clientX - drag.sx, dy = e.clientY - drag.sy;
    if (!drag.moved && Math.hypot(dx, dy) > 6) { drag.moved = true; drag.c.classList.add('drag'); G.to(drag.c, { scale: 1.05, duration: .2 }); }
    if (drag.moved) G.set(drag.c, { x: dx, y: dy, rotation: drag.rot + clamp(dx / 40, -6, 6) });
  });
  const end = (e) => {
    if (!drag || (e && e.pointerId !== drag.id)) return;
    const { c, moved, rot } = drag; drag = null; c.classList.remove('drag');
    if (!moved) return;
    c.dataset.dragged = '1'; setTimeout(() => delete c.dataset.dragged, 80);
    const px = e.clientX, py = e.clientY;
    const t = order().find((o) => { if (o === c) return false; const r = o.getBoundingClientRect(); return px > r.left && px < r.right && py > r.top && py < r.bottom; });
    if (t) { G.set(c, { scale: 1, rotation: rot }); swap(c, t); }
    else G.to(c, { x: 0, y: 0, scale: 1, rotation: rot, duration: .7, ease: 'elastic.out(1,.55)' });
  };
  board.addEventListener('pointerup', end); board.addEventListener('pointercancel', end);
  chips.forEach((c) => c.addEventListener('click', (e) => { if (c.dataset.dragged) { e.preventDefault(); return; } choose(c); }));
  shuffleBtn.addEventListener('click', () => {
    const frag = order().sort(() => Math.random() - .5);
    const st = FL && canAnimate ? FL.getState(order()) : null;
    frag.forEach((c) => board.appendChild(c));
    if (st) FL.from(st, { duration: .65, ease: 'power3.inOut', stagger: .03 });
    choose(frag[Math.floor(Math.random() * frag.length)]);
  });
  choose(chips[0], false);
})();

/* ============ stakes tiles (built always) ============ */
const TILE_SPEC = [
  ['poster', 'yellow', 'cobalt', 'Poster'], ['edit', 'cream', 'tomato', 'Editorial'], ['app', 'mint', 'yellow', 'Dashboard'], ['split', 'cream', 'cobalt', 'Split hero'],
  ['num', 'tomato', 'yellow', 'Scoreboard'], ['stripe', 'yellow', 'tomato', 'Banded'], ['edit', 'mint', 'cobalt', 'Ledger'], ['poster', 'cream', 'tomato', 'Specimen'],
  ['split', 'yellow', 'mint', 'Catalog'], ['app', 'cream', 'cobalt', 'Terminal'], ['num', 'mint', 'tomato', 'Timeline'], ['stripe', 'cream', 'cobalt', 'Marquee']
];
function tileNew(kind, bg, cc, word) {
  const st = ' style="--bgc:var(--' + bg + ');--cc:var(--' + cc + ')"';
  const c = '<div class="t-new tv tv--' + kind + '"' + st + '>';
  if (kind === 'poster') return c + '<u></u><em></em><b>' + word + '</b></div>';
  if (kind === 'edit') return c + '<b>' + word + '</b><s><i></i><i></i><i></i></s></div>';
  if (kind === 'app') return c + '<i></i><div><b></b><span></span><span></span><b class="tl">' + word + '</b></div></div>';
  if (kind === 'split') return c + '<i></i><div><b>' + word + '</b><span></span><span></span></div></div>';
  if (kind === 'num') return c + '<span><i></i><i></i></span><b>' + word + '</b></div>';
  return c + '<i style="top:14%"></i><i style="top:46%;height:10%"></i><b>' + word + '</b></div>';
}
(() => {
  const host = $('.tiles'); if (!host) return;
  host.innerHTML = TILE_SPEC.map((t) =>
    '<div class="tile"><div class="t-gen tg"><div class="tg__nav"><i></i><i></i><i></i></div><div class="tg__h"></div><div class="tg__h s"></div><div class="tg__p"></div><div class="tg__b"></div><div class="tg__c"><i></i><i></i><i></i></div></div>' + tileNew(t[0], t[1], t[2], t[3]) + '</div>').join('');
})();

if (!canAnimate) { $$('[data-count]').forEach((n) => { n.textContent = n.dataset.count; }); }

/* run steps: pinned layout scrolls the runway; static layout scrolls to the scene */
$$('.step__btn').forEach((b) => b.addEventListener('click', () => {
  const i = +b.dataset.step; const smooth = canAnimate ? 'smooth' : 'auto';
  if (root.classList.contains('runx')) {
    const runway = $('.run__runway'); const total = runway.offsetHeight - innerHeight;
    scrollTo({ top: runway.getBoundingClientRect().top + scrollY + ((i + .5) / 6) * total, behavior: smooth });
  } else { const sc = $$('.scene')[i]; if (sc) sc.scrollIntoView({ behavior: smooth, block: 'center' }); }
}));

/* ============ animated enhancements ============ */
if (canAnimate) {
  let ctx = null, cleanups = [], built = false, lastW = 0, lastH = 0;
  const on = (t, ev, fn, o) => { t.addEventListener(ev, fn, o); cleanups.push(() => t.removeEventListener(ev, fn, o)); };

  /* persistent (size independent): velocity type, magnets */
  const stretchEls = $$('.stretch, .stretch2');
  const visible = new Set();
  const vio = new IntersectionObserver((es) => es.forEach((e) => e.isIntersecting ? visible.add(e.target) : visible.delete(e.target)), { rootMargin: '10% 0px' });
  stretchEls.forEach((el) => vio.observe(el));
  let lastY = scrollY, vel = 0, shown = 0;
  G.ticker.add(() => {
    const y = scrollY, dy = y - lastY; lastY = y;
    vel += (clamp(dy / 38, -1, 1) - vel) * .12;
    if (Math.abs(vel) < .002) vel = 0;
    if (Math.abs(vel - shown) > .003 || (vel === 0 && shown !== 0)) {
      shown = vel; const v = vel.toFixed(3), a = Math.abs(vel).toFixed(3);
      visible.forEach((el) => { el.style.setProperty('--vel', v); el.style.setProperty('--vabs', a); });
    }
  });

  /* magnets: chips and mode chips lean toward a nearby cursor */
  if (finePointer) {
    const mags = $$('.mchip, .chip'); let px = -999, py = -999, raf = 0;
    const tick = () => {
      raf = 0;
      mags.forEach((m) => {
        const s = m.firstElementChild; if (!s) return;
        const r = m.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return;
        const cx = r.left + r.width / 2, cy = r.top + r.height / 2, dx = px - cx, dy = py - cy, d = Math.hypot(dx, dy), R = 110;
        const k = d < R ? (1 - d / R) : 0;
        const tx = dx * k * .12, ty = dy * k * .12;
        s.style.setProperty('--mx', tx.toFixed(1) + 'px'); s.style.setProperty('--my', ty.toFixed(1) + 'px');
      });
    };
    addEventListener('pointermove', (e) => { px = e.clientX; py = e.clientY; if (!raf) raf = requestAnimationFrame(tick); }, { passive: true });
    addEventListener('pointerleave', () => { px = py = -999; tick(); });
  }

  /* count-up numerals */
  $$('[data-count]').forEach((n) => {
    const end = +n.dataset.count; const o = { v: 0 };
    ST.create({ trigger: n, start: 'top 88%', once: true, onEnter: () => G.to(o, { v: end, duration: 1.4, ease: 'power2.out', onUpdate: () => { n.textContent = Math.round(o.v); } }) });
    n.textContent = '0';
  });

  const pinned = () => mqPin.matches;

  function build() {
    root.classList.add('go'); root.classList.toggle('pin', pinned());
    root.classList.toggle('runx', pinned() || innerWidth < 900);
    built = true; lastW = innerWidth; lastH = innerHeight;
    ctx = G.context(() => {
      initWipes();
      initStakes();
      initRun();
      initMarquee();
    });
    requestAnimationFrame(() => ST.refresh());
  }
  function teardown() {
    cleanups.forEach((f) => f()); cleanups = [];
    if (ctx) ctx.revert(); ctx = null;
    $$('.field').forEach((f) => { f.style.background = ''; const b = $('.field__bg', f); if (b) b.style.clipPath = ''; $$(':scope > .wrap, :scope > div[class$="runway"]', f).forEach((k) => { k.style.opacity = ''; }); });
  }

  /* ---------- section colour wipes ---------- */
  function initWipes() {
    const plan = { stakes: 'circleL', run: 'down', choice: 'left', evidence: 'circleR', modes: 'down', install: 'right', agents: 'circleL', limits: 'down', credits: 'circleR', faq: 'left', close: 'down' };
    const shapes = {
      circleL: (W, H, vh) => ['circle(0px at 10% 0px)', 'circle(' + Math.round(Math.hypot(W, vh) * 1.25) + 'px at 10% 0px)'],
      circleR: (W, H, vh) => ['circle(0px at 90% 0px)', 'circle(' + Math.round(Math.hypot(W, vh) * 1.25) + 'px at 90% 0px)'],
      down: (W, H, vh) => ['inset(0px 0px ' + Math.round(H) + 'px 0px)', 'inset(0px 0px ' + Math.round(Math.max(0, H - vh * 1.25)) + 'px 0px)'],
      left: (W) => ['inset(0px ' + Math.round(W) + 'px 0px 0px)', 'inset(0px 0px 0px 0px)'],
      right: (W) => ['inset(0px 0px 0px ' + Math.round(W) + 'px)', 'inset(0px 0px 0px 0px)']
    };
    $$('.field').forEach((f) => {
      const bg = $('.field__bg', f); const shape = shapes[plan[f.id]]; if (!bg || !shape) return;
      f.style.background = 'var(--prev-c)';
      const kids = $$(':scope > .wrap, :scope > div[class$="runway"]', f);
      const rect = () => ({ W: f.offsetWidth, H: f.offsetHeight, vh: innerHeight });
      const compact = innerWidth < 900;
      const late = f.id === 'stakes'; /* the hero is a full dark screen: start this reveal later */
      const sh = compact ? shapes.down : shape;
      G.fromTo(bg, { clipPath: () => { const r = rect(); return sh(r.W, r.H, r.vh)[0]; } }, {
        clipPath: () => { const r = rect(); return sh(r.W, r.H, r.vh)[1]; }, ease: 'none', immediateRender: true,
        scrollTrigger: { trigger: f, start: compact ? (late ? 'top 92%' : 'top 99%') : (late ? 'top 84%' : 'top 96%'), end: compact ? (late ? 'top 74%' : 'top 78%') : (late ? 'top 36%' : 'top 38%'), scrub: true, invalidateOnRefresh: true, onLeave: () => { bg.style.clipPath = 'none'; } }
      });
      /* these sections show their content only once the wipe fully covers it, so no word is cut across the seam */
      const gate = ['stakes', 'choice', 'install', 'agents', 'credits', 'faq'].includes(f.id);
      const kidsAt = gate ? (compact ? [late ? 'top 74%' : 'top 78%', late ? 'top 64%' : 'top 68%'] : [late ? 'top 36%' : 'top 38%', late ? 'top 24%' : 'top 26%']) : (compact ? [late ? 'top 88%' : 'top 94%', late ? 'top 78%' : 'top 82%'] : [late ? 'top 78%' : 'top 88%', late ? 'top 52%' : 'top 56%']);
      G.fromTo(kids, { opacity: 0 }, { opacity: 1, ease: 'none', scrollTrigger: { trigger: f, start: kidsAt[0], end: kidsAt[1], scrub: true } });
    });
  }

  /* ---------- stakes: the cliche, repeated then broken ---------- */
  function initStakes() {
    const tiles = $$('.tile'); if (!tiles.length) return;
    const wipes = ['inset(0% 100% 0% 0%)', 'inset(100% 0% 0% 0%)', 'inset(0% 0% 0% 100%)', 'inset(0% 0% 100% 0%)', 'circle(0% at 50% 50%)', 'inset(50% 50% 50% 50%)'];
    const rots = [-3, 2, -2, 3, -1.5, 2.5, -3.5, 1.5, 2, -2.5, 3, -1];
    const order = [7, 2, 10, 4, 0, 9, 5, 11, 1, 8, 3, 6];
    const tl = G.timeline({ defaults: { ease: 'none' }, scrollTrigger: pinned()
      ? { trigger: '.stakes__runway', start: 'top top', end: 'bottom bottom', scrub: .5 }
      : { trigger: '.tiles', start: 'top 85%', end: 'bottom 40%', scrub: .5 } });
    tiles.forEach((t, i) => {
      const nw = $('.t-new', t), at = order[i] * .05;
      tl.fromTo(nw, { clipPath: wipes[i % wipes.length] }, { clipPath: wipes[i % wipes.length].startsWith('circle') ? 'circle(75% at 50% 50%)' : 'inset(0% 0% 0% 0%)', duration: .24, ease: 'power2.inOut' }, at);
      tl.fromTo(t, { rotation: 0, y: 0 }, { rotation: rots[i], y: (i % 2 ? 10 : -8), duration: .26, ease: 'back.out(2.2)' }, at);
    });
    tl.to({}, { duration: .001 }, .999);
  }

  /* ---------- the run: sticky stepper, scene swaps ---------- */
  function initRun() {
    if (!root.classList.contains('runx')) return;
    const steps = $$('.step'), scenes = $$('.scene'), rail = $('.run__rail span'), num = $('.run__n'), runway = $('.run__runway');
    let cur = 0;
    scenes.forEach((s) => $$('.s1 .tree li, .inv__row, .dir, .host, .diff li, .report li, .review, .stack, .s6__line, .pick__out', s).forEach((el, i) => { el.classList.add('anim'); el.style.setProperty('--d', i); }));
    const setStep = (i) => {
      if (i === cur) return;
      scenes.forEach((s) => s.classList.remove('is-prev'));
      scenes[cur].classList.remove('is-on'); scenes[cur].classList.add('is-prev');
      scenes[i].classList.add('is-on');
      steps.forEach((s, k) => { s.classList.toggle('is-on', k === i); const b = $('.step__btn', s); if (k === i) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current'); });
      num.textContent = String(i + 1).padStart(2, '0'); cur = i;
      const keep = i; setTimeout(() => { if (cur === keep) scenes.forEach((s) => s.classList.remove('is-prev')); }, 720);
    };
    ST.create({ trigger: runway, start: 'top top', end: 'bottom bottom', onUpdate: (self) => { setStep(clamp(Math.floor(self.progress * 6), 0, 5)); G.set(rail, { scaleX: self.progress }); } });
    /* the pickable choose scene */
    const picks = $$('.pick'), out = $('.pick__out span'), pg = $('.picks');
    const names = { A: 'Poster', B: 'Editorial', C: 'Product' };
    picks.forEach((p) => on(p, 'click', () => {
      picks.forEach((x) => x.setAttribute('aria-checked', String(x === p)));
      pg.classList.add('has');
      out.textContent = 'You chose ' + p.dataset.pick + ', the ' + names[p.dataset.pick].toLowerCase() + ' layout. Now the agent may integrate it, and only it.';
    }));
  }

  /* ---------- agents marquee ---------- */
  function initMarquee() {
    const marq = $('#marq'), rows = $$('.marq__row'); if (!marq) return;
    const added = [];
    rows.forEach((r) => { $$('li', r).forEach((li) => { const c = li.cloneNode(true); c.setAttribute('aria-hidden', 'true'); r.appendChild(c); added.push(c); }); });
    requestAnimationFrame(() => rows.forEach((r) => r.style.setProperty('--dur', Math.round(r.scrollWidth / 2 / 62) + 's')));
    cleanups.push(() => added.forEach((c) => c.remove()));
    const btn = $('.marq__pause'), face = $('span span', btn); let user = false;
    const apply = (off) => marq.classList.toggle('paused', user || off);
    const io = new IntersectionObserver((es) => apply(!es[0].isIntersecting)); io.observe(marq); cleanups.push(() => io.disconnect());
    on(btn, 'click', () => { user = !user; btn.setAttribute('aria-pressed', String(user)); face.textContent = user ? 'Play names' : 'Pause names'; $('use', btn).setAttribute('href', user ? '#i-play' : '#i-pause'); apply(false); });
  }

  /* kick off after fonts are ready (word fitting needs real metrics) */
  const ready = Promise.race([document.fonts ? document.fonts.ready : Promise.resolve(), new Promise((r) => setTimeout(r, 1400))]);
  ready.then(() => { build(); });
  let rt = null;
  addEventListener('resize', () => {
    clearTimeout(rt);
    rt = setTimeout(() => {
      const dw = Math.abs(innerWidth - lastW), dh = Math.abs(innerHeight - lastH);
      if (!built || dw < 24 && (dh < 140 || !finePointer)) return;
      teardown(); build();
    }, 250);
  });
}
