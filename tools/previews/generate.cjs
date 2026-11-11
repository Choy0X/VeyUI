// Regenerates the preview images from previews.html with headless Chrome.
// Usage: node tools/previews/generate.cjs
// Needs puppeteer-core (npm i puppeteer-core in a scratch folder, then set PUPPETEER_CORE to its path)
// and Chrome, Edge or Chromium (set CHROME_PATH if it is not found).
// Output goes to site/assets/: og-image.png (1200x630), social-preview.png (1280x640),
// preview-concepts.png (1600x800), preview-workflow.png (1600x640), plus the hero teaser frames
// hero-before.webp, hero-after.webp and their compact crops (-m.webp).
// The Slackwater before and after frames are captured from the real site first
// (reduced-motion static layout, which shows both designs full size) into tools/previews/.cache/.
const fs = require('fs');
const http = require('http');
const path = require('path');

const root = path.resolve(__dirname, '..', '..');
const puppeteer = require(process.env.PUPPETEER_CORE || 'puppeteer-core');
const candidates = [
  process.env.CHROME_PATH,
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].filter(Boolean);
const chrome = candidates.find((p) => fs.existsSync(p));
if (!chrome) { console.error('No Chrome, Edge or Chromium found. Set CHROME_PATH.'); process.exit(1); }

const types = { '.html': 'text/html', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png', '.css': 'text/css', '.js': 'text/javascript' };
const server = http.createServer((req, res) => {
  const file = path.join(root, decodeURIComponent(req.url.split('?')[0]));
  if (!file.startsWith(root) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': types[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});

const jobs = [
  ['og', 1200, 630, 'og-image.png'],
  ['social', 1280, 640, 'social-preview.png'],
  ['concepts', 1600, 800, 'preview-concepts.png'],
  ['workflow', 1600, 640, 'preview-workflow.png'],
];

server.listen(0, '127.0.0.1', async () => {
  const port = server.address().port;
  const browser = await puppeteer.launch({ executablePath: chrome, headless: 'new', args: ['--no-sandbox'] });
  try {
    const cache = path.join(__dirname, '.cache');
    fs.mkdirSync(cache, { recursive: true });
    const site = await browser.newPage();
    await site.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
    await site.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
    await site.goto('http://127.0.0.1:' + port + '/site/index.html', { waitUntil: 'networkidle0' });
    await site.evaluate(() => document.fonts.ready);
    const figs = await site.$$('#choice .ba__fig .pg');
    if (figs.length !== 2) throw new Error('expected 2 before/after frames in #choice, found ' + figs.length);
    for (const [i, name] of ['before', 'after'].entries()) {
      await figs[i].scrollIntoView();
      await new Promise((r) => setTimeout(r, 400));
      await figs[i].screenshot({ path: path.join(cache, name + '.png') });
    }
    await site.close();

    // hero teaser frames: full frames and compact crops as WebP at 2x (the hero shows them)
    const hero = await browser.newPage();
    await hero.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
    await hero.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
    await hero.goto('http://127.0.0.1:' + port + '/site/index.html', { waitUntil: 'networkidle0' });
    await hero.evaluate(() => document.fonts.ready);
    const hfigs = await hero.$$('#choice .ba__fig .pg');
    const assets = path.join(root, 'site', 'assets');
    for (const [i, name, q] of [[0, 'before', 80], [1, 'after', 70]]) {
      await hfigs[i].scrollIntoView();
      await new Promise((r) => setTimeout(r, 500));
      await hfigs[i].screenshot({ path: path.join(assets, 'hero-' + name + '.webp'), type: 'webp', quality: q });
      const o = await hfigs[i].evaluate((e) => { const r = e.getBoundingClientRect(); return { x: r.x + scrollX, y: r.y + scrollY }; });
      // compact crop: x 165 to 835 and y 0 to 590 of the 1000x660 frame
      await hero.screenshot({ path: path.join(assets, 'hero-' + name + '-m.webp'), type: 'webp', quality: q, clip: { x: o.x + 165, y: o.y, width: 670, height: 590 } });
      console.log('wrote hero-' + name + '.webp and hero-' + name + '-m.webp');
    }
    await hero.close();
    for (const [v, w, h, out] of jobs) {
      const page = await browser.newPage();
      await page.setViewport({ width: w, height: h, deviceScaleFactor: 1 });
      await page.goto('http://127.0.0.1:' + port + '/tools/previews/previews.html?v=' + v, { waitUntil: 'networkidle0' });
      await page.evaluate(() => document.fonts.ready);
      const file = path.join(root, 'site', 'assets', out);
      await page.screenshot({ path: file, type: 'png' });
      console.log('wrote', path.relative(root, file), fs.statSync(file).size + ' bytes');
      await page.close();
    }
  } finally {
    await browser.close();
    server.close();
  }
});
