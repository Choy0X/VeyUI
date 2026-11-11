// Regenerates the raster icons from site/assets/logo.svg (the logo source) with headless Chrome.
// Usage: PUPPETEER_CORE=<path to puppeteer-core> node tools/brand/generate-icons.cjs
// Writes: site/assets/apple-touch-icon.png (180),
// .claude-plugin/icon.png (512). Also copies the logo to site/assets/favicon.svg and
// skills/veyui/assets/icon.svg so the three SVGs never drift apart.
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..', '..');
const puppeteer = require(process.env.PUPPETEER_CORE || 'puppeteer-core');
const chrome = [
  process.env.CHROME_PATH,
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].filter(Boolean).find((p) => fs.existsSync(p));
if (!chrome) { console.error('No Chrome, Edge or Chromium found. Set CHROME_PATH.'); process.exit(1); }

const svg = fs.readFileSync(path.join(root, 'site', 'assets', 'logo.svg'), 'utf8');
fs.copyFileSync(path.join(root, 'site', 'assets', 'logo.svg'), path.join(root, 'site', 'assets', 'favicon.svg'));
fs.copyFileSync(path.join(root, 'site', 'assets', 'logo.svg'), path.join(root, 'skills', 'veyui', 'assets', 'icon.svg'));

// size: output px, pad: fraction of the canvas left empty around the mark, bg: fill behind it (null = transparent)
async function render(browser, size, pad, bg) {
  const page = await browser.newPage();
  await page.setViewport({ width: size, height: size, deviceScaleFactor: 1 });
  const inner = Math.round(size * (1 - 2 * pad));
  await page.setContent('<body style="margin:0;display:grid;place-items:center;width:' + size + 'px;height:' + size + 'px;background:' + (bg || 'transparent') + '">' +
    svg.replace('width="256" height="256"', 'width="' + inner + '" height="' + inner + '"') + '</body>');
  const buf = await page.screenshot({ type: 'png', omitBackground: !bg });
  await page.close();
  return buf;
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: chrome, headless: 'new', args: ['--no-sandbox'] });
  try {
    fs.writeFileSync(path.join(root, 'site', 'assets', 'apple-touch-icon.png'), await render(browser, 180, 0.1, '#F7F1E3'));
    fs.writeFileSync(path.join(root, '.claude-plugin', 'icon.png'), await render(browser, 512, 0, null));
    console.log('wrote apple-touch-icon.png, .claude-plugin/icon.png, favicon.svg, icon.svg');
  } finally {
    await browser.close();
  }
})();
