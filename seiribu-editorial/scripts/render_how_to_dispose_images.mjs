#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const SCRIPT_DIR = path.dirname(__filename);
const ROOT = path.resolve(SCRIPT_DIR, "..");
const PROJECT_ROOT = path.resolve(ROOT, "..");
const OUT_DIR = path.join(ROOT, "assets", "images", "how-to-dispose");
const LOGO = path.join(ROOT, "assets", "images", "brand", "seiribu-logo.png");
const MATERIAL = path.join(OUT_DIR, "how-to-dispose-eyecatch-material.png");
const FONT_DIR = "/Users/dvcong/Library/Fonts";
const BUNDLED_MODULES = path.join(
  process.env.HOME || "",
  ".cache",
  "codex-runtimes",
  "codex-primary-runtime",
  "dependencies",
  "node",
  "node_modules",
  "playwright"
);

const require = createRequire(import.meta.url);

function loadPlaywright() {
  if (fs.existsSync(BUNDLED_MODULES)) {
    return require(BUNDLED_MODULES);
  }
  return require("playwright");
}

function assetDataUri(file, mime = "image/png") {
  return `data:${mime};base64,${fs.readFileSync(file).toString("base64")}`;
}

function fontFace(name, file, weight) {
  const src = assetDataUri(path.join(FONT_DIR, file), "font/truetype");
  return `@font-face{font-family:'${name}';src:url('${src}') format('truetype');font-weight:${weight};font-style:normal;font-display:block;}`;
}

const logo = assetDataUri(LOGO);
const material = fs.existsSync(MATERIAL) ? assetDataUri(MATERIAL) : "";

const css = `
${fontFace("NotoJP", "NotoSansJP-Regular.ttf", 400)}
${fontFace("NotoJP", "NotoSansJP-Medium.ttf", 500)}
${fontFace("NotoJP", "NotoSansJP-Bold.ttf", 700)}
:root{
  --cream:#fbf4ea;
  --cream2:#f6ead8;
  --paper:#fffdf8;
  --ink:#24304a;
  --muted:#5f6675;
  --green:#6ea77b;
  --greenDeep:#2f6b61;
  --blue:#5d94b1;
  --orange:#dfa434;
  --salmon:#de6d5f;
  --burgundy:#7a3454;
  --line:#ded3c2;
}
*{box-sizing:border-box}
body{margin:0;background:#eee;font-family:"NotoJP",system-ui,sans-serif;color:var(--ink)}
.artboard{
  width:1200px;height:800px;position:relative;overflow:hidden;
  background:
    radial-gradient(circle at 10% 10%, rgba(255,255,255,.78), transparent 24%),
    linear-gradient(180deg, #fbf6ed 0%, #f9f1e4 78%, #f2e4c8 100%);
}
.eyecatch{
  height:630px;
  background-image:
    linear-gradient(90deg, rgba(251,244,234,.98) 0%, rgba(251,244,234,.9) 31%, rgba(251,244,234,.48) 54%, rgba(251,244,234,.14) 100%),
    url('${material}');
  background-size:cover;
  background-position:center;
}
.noise-dot{position:absolute;width:7px;height:7px;border-radius:50%;background:#d7c4aa;opacity:.7}
.logo{position:absolute;right:44px;bottom:32px;width:150px;height:auto;z-index:10}
.logo.top{left:48px;top:36px;right:auto;bottom:auto;width:150px}
.title{font-weight:700;letter-spacing:0;line-height:1.28;color:var(--ink);text-align:center}
.subtitle{font-weight:500;letter-spacing:0;color:var(--greenDeep);text-align:center}
.eyecatch-copy{
  position:absolute;left:102px;top:126px;width:552px;
  padding:34px 42px 32px;border-radius:0;
  background:rgba(255,249,240,.68);
  box-shadow:0 16px 42px rgba(109,83,48,.11);
}
.eyecatch-copy h1{margin:0;color:var(--burgundy);font-size:46px;line-height:1.25;text-align:center}
.eyecatch-copy p{margin:16px 0 0;font-size:24px;color:var(--ink);text-align:center}
.eyecatch-copy i{display:block;width:250px;height:8px;border-radius:999px;background:var(--orange);margin:20px auto 0}
.figure-title{position:absolute;left:72px;right:72px;top:54px;text-align:center}
.figure-title h2{margin:0;font-size:38px;line-height:1.25;letter-spacing:0;color:var(--ink);font-weight:700}
.figure-title p{margin:8px 0 0;font-size:23px;line-height:1.35;font-weight:500;color:var(--greenDeep)}
.leaf{position:absolute;right:66px;top:56px;width:72px;height:104px;opacity:.72}
.leaf span{position:absolute;width:26px;height:16px;border-radius:80% 20% 80% 20%;background:#8fb17d;transform:rotate(-25deg)}
.leaf span:nth-child(1){right:8px;top:0}.leaf span:nth-child(2){right:18px;top:18px}.leaf span:nth-child(3){right:4px;top:35px}.leaf span:nth-child(4){right:24px;top:52px}.leaf span:nth-child(5){right:10px;top:70px}
.bottom-note{
  position:absolute;left:180px;right:180px;bottom:34px;height:48px;border-radius:26px;
  background:rgba(255,253,248,.94);border:2px solid var(--line);
  display:flex;align-items:center;justify-content:center;color:var(--greenDeep);
  font-size:22px;font-weight:700;
}
.chip{border-radius:999px;padding:8px 22px;font-weight:700;display:inline-flex;align-items:center;justify-content:center}
.num{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:27px;font-weight:700;flex:0 0 auto}
.icon svg{width:76px;height:76px;display:block}

#funnel .funnel-wrap{position:absolute;left:118px;top:166px;width:964px;height:500px}
#funnel .side-label{position:absolute;left:28px;top:180px;width:120px;color:var(--muted);font-size:20px;font-weight:700;text-align:center;line-height:1.4}
#funnel .side-label.bottom{top:594px}
#funnel .arrow{position:absolute;left:85px;top:246px;width:5px;height:304px;background:linear-gradient(var(--orange),var(--blue));border-radius:999px}
#funnel .arrow:after{content:"";position:absolute;left:-10px;bottom:-8px;border-left:13px solid transparent;border-right:13px solid transparent;border-top:18px solid var(--blue)}
.funnel-band{position:absolute;left:0;height:132px;filter:drop-shadow(0 12px 0 rgba(190,162,121,.24))}
.funnel-band svg{width:100%;height:132px;display:block}
.funnel-content{position:absolute;inset:0;display:flex;align-items:center;gap:22px;padding-left:70px;padding-right:60px}
.funnel-text{flex:1;min-width:0}
.funnel-text h3{font-size:30px;line-height:1.22;margin:0 0 8px;font-weight:700;color:var(--ink)}
.funnel-text p{font-size:19px;line-height:1.42;margin:0;color:var(--muted);font-weight:500}
.mini-stack{margin-left:auto;display:grid;grid-template-columns:repeat(3,38px);gap:10px;opacity:.9}
.mini-box{width:38px;height:34px;border-radius:5px;background:#d6a56c;border:2px solid #996940;box-shadow:0 5px 0 rgba(153,105,64,.18)}
.mini-box:nth-child(2n){background:#e2ba82}.mini-box:nth-child(3n){background:#c9955d}

#matrix .matrix-card{position:absolute;left:148px;top:166px;width:912px;height:510px;border-radius:28px;background:rgba(255,253,248,.86);border:2px solid var(--line);box-shadow:0 18px 46px rgba(110,85,52,.12)}
#matrix .axis-x{position:absolute;left:80px;right:56px;bottom:70px;height:4px;background:#7f8a96}
#matrix .axis-x:after{content:"";position:absolute;right:-5px;top:-10px;border-left:24px solid #7f8a96;border-top:12px solid transparent;border-bottom:12px solid transparent}
#matrix .axis-y{position:absolute;left:80px;top:56px;bottom:70px;width:4px;background:#7f8a96}
#matrix .axis-y:after{content:"";position:absolute;left:-10px;top:-5px;border-bottom:24px solid #7f8a96;border-left:12px solid transparent;border-right:12px solid transparent}
.gridline-x,.gridline-y{position:absolute;background:#e5dbce}
.gridline-x{left:80px;right:70px;height:2px}.gridline-y{top:56px;bottom:70px;width:2px}
.axis-label{position:absolute;color:var(--muted);font-size:20px;line-height:1.35;font-weight:700}
.method{position:absolute;width:250px;height:104px;border-radius:22px;background:#fff;border:3px solid var(--orange);box-shadow:0 12px 26px rgba(98,74,41,.12);display:flex;align-items:center;gap:14px;padding:16px 20px}
.method strong{display:block;font-size:25px;line-height:1.2;color:var(--ink)}
.method span{display:block;margin-top:5px;font-size:16px;line-height:1.32;color:var(--muted);font-weight:500}
.method .badge{width:48px;height:48px;border-radius:16px;display:flex;align-items:center;justify-content:center;background:#fff2cf}
.method svg{width:34px;height:34px}
.callout{position:absolute;right:54px;top:48px;width:282px;padding:16px 20px;border-radius:20px;background:#f7fbfd;border:2px solid #c8dce6;text-align:center;font-weight:700;color:var(--ink);font-size:20px;line-height:1.4}

#boundary .cards{position:absolute;left:52px;right:52px;top:174px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.boundary-card{height:435px;border-radius:30px;background:rgba(255,253,248,.92);border:2px solid var(--line);overflow:hidden;box-shadow:0 18px 44px rgba(110,85,52,.12);position:relative}
.boundary-scene{height:190px;position:relative;background:linear-gradient(180deg,#fff8e9,#f5e1c0)}
.boundary-card:nth-child(2) .boundary-scene{background:linear-gradient(180deg,#fff2ed,#f4dacd)}
.boundary-card:nth-child(3) .boundary-scene{background:linear-gradient(180deg,#edf8ef,#dcebd6)}
.boundary-content{padding:24px 28px 26px}
.boundary-heading{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.boundary-heading h3{font-size:25px;line-height:1.25;margin:0;color:var(--ink);font-weight:700}
.boundary-content p{font-size:18px;line-height:1.55;margin:0;color:var(--muted);font-weight:500}
.check{width:54px;height:54px;border-radius:16px;background:#fff;border:4px solid currentColor;position:relative;flex:0 0 auto}
.check:after{content:"";position:absolute;left:14px;top:8px;width:18px;height:30px;border-right:6px solid currentColor;border-bottom:6px solid currentColor;transform:rotate(38deg)}
.final-message{position:absolute;left:232px;right:232px;bottom:48px;height:60px;border-radius:32px;background:var(--burgundy);display:flex;align-items:center;justify-content:center;color:#fff;font-size:27px;font-weight:700;box-shadow:0 16px 30px rgba(122,52,84,.18)}
.scene-floor{position:absolute;left:0;right:0;bottom:0;height:46px;background:rgba(204,162,101,.18)}
.appliance{position:absolute;left:84px;top:52px;width:78px;height:96px;border-radius:12px;background:#f7fbfd;border:4px solid #6b94aa}
.appliance:before{content:"";position:absolute;left:19px;top:18px;width:34px;height:34px;border-radius:50%;border:4px solid #6b94aa}
.appliance:after{content:"";position:absolute;left:18px;bottom:15px;width:42px;height:8px;border-radius:6px;background:#6b94aa}
.recycle-arrow{position:absolute;left:174px;top:72px;width:84px;height:84px;border-radius:50%;border:8px solid #6b94aa;border-left-color:transparent;transform:rotate(-20deg)}
.recycle-arrow:after{content:"";position:absolute;right:-5px;top:4px;border-left:19px solid #6b94aa;border-top:13px solid transparent;border-bottom:13px solid transparent;transform:rotate(28deg)}
.stairs{position:absolute;left:62px;bottom:44px;width:118px;height:100px}
.stairs i{position:absolute;bottom:0;width:34px;height:24px;background:#f4c77a;border:3px solid #d56d5d}
.stairs i:nth-child(1){left:0}.stairs i:nth-child(2){left:28px;bottom:24px}.stairs i:nth-child(3){left:56px;bottom:48px}
.furniture{position:absolute;right:72px;top:58px;width:95px;height:100px;border-radius:12px;background:#b88762;border:4px solid #7d583e}
.furniture:before{content:"";position:absolute;left:12px;right:12px;top:22px;height:4px;background:#7d583e}.furniture:after{content:"";position:absolute;left:45px;top:0;bottom:0;width:4px;background:#7d583e}
.calendar{position:absolute;left:78px;top:54px;width:118px;height:106px;border-radius:16px;background:#fff;border:4px solid #67a77d;overflow:hidden}
.calendar:before{content:"";position:absolute;left:0;right:0;top:0;height:32px;background:#f6d78d}.calendar:after{content:"";position:absolute;left:24px;top:55px;width:68px;height:8px;border-radius:6px;background:#67a77d;box-shadow:0 24px 0 #67a77d}
.coin-clock{position:absolute;right:76px;top:64px;width:92px;height:92px;border-radius:50%;background:#fff8de;border:5px solid #67a77d}
.coin-clock:before{content:"";position:absolute;left:42px;top:18px;width:5px;height:32px;background:#67a77d}.coin-clock:after{content:"";position:absolute;left:42px;top:48px;width:26px;height:5px;background:#67a77d;transform:rotate(32deg);transform-origin:left center}
`;

function icon(name, color) {
  const stroke = color;
  if (name === "tag") {
    return `<svg viewBox="0 0 80 80" fill="none"><path d="M12 14h32l24 24-30 30L12 42V14z" fill="#fff4cf" stroke="${stroke}" stroke-width="5" stroke-linejoin="round"/><circle cx="31" cy="30" r="5" fill="#fff" stroke="${stroke}" stroke-width="4"/><path d="M43 44l12 12" stroke="${stroke}" stroke-width="5" stroke-linecap="round"/></svg>`;
  }
  if (name === "home") {
    return `<svg viewBox="0 0 80 80" fill="none"><path d="M15 38l25-22 25 22" stroke="${stroke}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 36v28h36V36" fill="#eef8f1" stroke="${stroke}" stroke-width="5" stroke-linejoin="round"/><path d="M35 64V47h12v17" fill="#fff" stroke="${stroke}" stroke-width="4"/></svg>`;
  }
  if (name === "truck") {
    return `<svg viewBox="0 0 80 80" fill="none"><path d="M10 31h38v25H10z" fill="#eaf4f8" stroke="${stroke}" stroke-width="5"/><path d="M48 39h17l7 10v7H48z" fill="#f8d58e" stroke="${stroke}" stroke-width="5"/><circle cx="25" cy="60" r="7" fill="${stroke}"/><circle cx="59" cy="60" r="7" fill="${stroke}"/></svg>`;
  }
  if (name === "car") {
    return `<svg viewBox="0 0 80 80" fill="none"><path d="M12 42h56v18H12z" fill="#eaf4f8" stroke="${stroke}" stroke-width="5"/><path d="M24 42l8-14h20l8 14" fill="#fff" stroke="${stroke}" stroke-width="5"/><circle cx="25" cy="62" r="7" fill="${stroke}"/><circle cx="56" cy="62" r="7" fill="${stroke}"/></svg>`;
  }
  if (name === "chat") {
    return `<svg viewBox="0 0 80 80" fill="none"><path d="M15 18h50v34H36L24 64V52h-9V18z" fill="#fff" stroke="${stroke}" stroke-width="5" stroke-linejoin="round"/><path d="M26 31h28M26 42h20" stroke="${stroke}" stroke-width="5" stroke-linecap="round"/></svg>`;
  }
  return `<svg viewBox="0 0 80 80" fill="none"><path d="M16 23h48v38H16z" fill="#fff" stroke="${stroke}" stroke-width="5"/><path d="M26 37h28M26 49h20" stroke="${stroke}" stroke-width="5" stroke-linecap="round"/></svg>`;
}

const html = `<!doctype html>
<html><head><meta charset="utf-8"><style>${css}</style></head><body>
  <section id="eyecatch" class="artboard eyecatch">
    <img class="logo top" src="${logo}" alt="">
    <div class="eyecatch-copy">
      <h1>実家の不用品を<br>安く処分する方法</h1>
      <p>粗大ごみ・持ち込み・回収業者の費用比較</p>
      <i></i>
    </div>
  </section>

  <section id="funnel" class="artboard">
    <span class="noise-dot" style="left:78px;top:108px"></span>
    <span class="noise-dot" style="right:86px;top:96px"></span>
    <span class="noise-dot" style="left:154px;bottom:98px"></span>
    <div class="figure-title"><h2>実家の不用品処分費用を安く抑える3つの手順</h2><p>売る・家庭ごみ・残りだけ依頼の順で、費用がかかる量を減らす</p></div>
    <div class="funnel-wrap">
      <div class="funnel-band" style="top:0;left:0;width:964px">
        <svg viewBox="0 0 964 132" preserveAspectRatio="none"><path d="M0 0h964l-80 132H80z" fill="#fff0c7" stroke="#dfa434" stroke-width="2"/></svg>
        <div class="funnel-content"><div class="num" style="background:var(--orange)">1</div><div class="icon">${icon("tag", "#dfa434")}</div><div class="funnel-text"><h3>売れるものを先に売る</h3><p>本・カメラ・工具などは、処分前に査定へ</p></div><div class="mini-stack"><b class="mini-box"></b><b class="mini-box"></b><b class="mini-box"></b><b class="mini-box"></b><b class="mini-box"></b><b class="mini-box"></b></div></div>
      </div>
      <div class="funnel-band" style="top:162px;left:72px;width:820px">
        <svg viewBox="0 0 820 132" preserveAspectRatio="none"><path d="M0 0h820l-76 132H76z" fill="#e8f6ec" stroke="#6ea77b" stroke-width="2"/></svg>
        <div class="funnel-content" style="padding-left:58px"><div class="num" style="background:var(--green)">2</div><div class="icon">${icon("home", "#6ea77b")}</div><div class="funnel-text"><h3>小さな不用品は家庭ごみへ</h3><p>自治体ルールに沿って、帰省ごとに処分</p></div><div class="mini-stack" style="grid-template-columns:repeat(2,38px)"><b class="mini-box"></b><b class="mini-box"></b><b class="mini-box"></b><b class="mini-box"></b></div></div>
      </div>
      <div class="funnel-band" style="top:324px;left:132px;width:700px">
        <svg viewBox="0 0 700 132" preserveAspectRatio="none"><path d="M0 0h700l-70 132H70z" fill="#e8f4f8" stroke="#5d94b1" stroke-width="2"/></svg>
        <div class="funnel-content" style="padding-left:48px;padding-right:46px"><div class="num" style="background:var(--blue)">3</div><div class="icon">${icon("truck", "#5d94b1")}</div><div class="funnel-text"><h3>大きい・重い物だけ依頼</h3><p>粗大ごみや回収業者に任せる量を最小化</p></div></div>
      </div>
    </div>
    <div class="side-label">大量の<br>荷物</div><div class="arrow"></div><div class="side-label bottom">依頼量を<br>最小化</div>
    <div class="bottom-note">業者に頼む分だけを小さくする</div>
    <img class="logo" src="${logo}" alt="">
  </section>

  <section id="matrix" class="artboard">
    <div class="leaf"><span></span><span></span><span></span><span></span><span></span></div>
    <span class="noise-dot" style="left:78px;top:108px"></span>
    <span class="noise-dot" style="right:86px;top:96px"></span>
    <div class="figure-title"><h2>不用品を手放す4つの方法：費用と手間の比較</h2><p>予算・時間・体力に合わせて、無理のない方法を選ぶ</p></div>
    <div class="matrix-card">
      <div class="axis-y"></div><div class="axis-x"></div>
      <div class="gridline-x" style="top:176px"></div><div class="gridline-x" style="top:298px"></div><div class="gridline-x" style="top:420px"></div>
      <div class="gridline-y" style="left:298px"></div><div class="gridline-y" style="left:516px"></div><div class="gridline-y" style="left:734px"></div>
      <div class="axis-label" style="left:-56px;top:-28px">手間が<br>かかる</div>
      <div class="axis-label" style="left:-54px;bottom:10px">手間<br>なし</div>
      <div class="axis-label" style="left:34px;bottom:20px">費用が安い</div>
      <div class="axis-label" style="right:48px;bottom:20px">高い</div>
      <div class="callout">大量・大型・急ぎなら<br>右下の方法も現実的</div>
      <div class="method" style="left:112px;top:34px"><div class="badge">${icon("car","#dfa434")}</div><div><strong>持ち込み</strong><span>最安だが車と搬出が必要</span></div></div>
      <div class="method" style="left:320px;top:150px;border-color:#b79ad6"><div class="badge" style="background:#f2ebf7">${icon("chat","#9d7ac2")}</div><div><strong>ジモティー等</strong><span>無料でも調整に時間が必要</span></div></div>
      <div class="method" style="left:190px;top:286px;border-color:#6ea77b"><div class="badge" style="background:#e8f6ec">${icon("doc","#6ea77b")}</div><div><strong>粗大ごみ</strong><span>安いが申込と搬出が必要</span></div></div>
      <div class="method" style="left:612px;top:326px;border-color:#5d94b1"><div class="badge" style="background:#e8f4f8">${icon("truck","#5d94b1")}</div><div><strong>回収業者</strong><span>費用は高めだが早くて楽</span></div></div>
    </div>
    <img class="logo" src="${logo}" alt="">
  </section>

  <section id="boundary" class="artboard">
    <div class="figure-title"><h2>自力での処分をやめる3つの境界線</h2><p>危険・割高・時間切れになりそうなら、プロへの相談も選択肢</p></div>
    <div class="cards">
      <article class="boundary-card">
        <div class="boundary-scene"><div class="scene-floor"></div><div class="appliance"></div><div class="recycle-arrow"></div></div>
        <div class="boundary-content"><div class="boundary-heading" style="color:var(--blue)"><div class="check"></div><h3>家電リサイクル対象品がある</h3></div><p>テレビ・冷蔵庫・洗濯機・エアコンは、自治体の粗大ごみに出せません。</p></div>
      </article>
      <article class="boundary-card">
        <div class="boundary-scene"><div class="scene-floor"></div><div class="stairs"><i></i><i></i><i></i></div><div class="furniture"></div></div>
        <div class="boundary-content"><div class="boundary-heading" style="color:var(--salmon)"><div class="check"></div><h3>階段で大型家具を搬出する</h3></div><p>無理な運搬はケガや壁・床の破損につながります。人数と動線を確認しましょう。</p></div>
      </article>
      <article class="boundary-card">
        <div class="boundary-scene"><div class="scene-floor"></div><div class="calendar"></div><div class="coin-clock"></div></div>
        <div class="boundary-content"><div class="boundary-heading" style="color:var(--green)"><div class="check"></div><h3>帰省の日数や体力に限界がある</h3></div><p>何度も通う費用や時間が膨らむなら、まとめて依頼した方が現実的です。</p></div>
      </article>
    </div>
    <div class="final-message">1つでも当てはまるなら、プロへの相談を検討</div>
    <img class="logo" src="${logo}" alt="">
  </section>
</body></html>`;

async function screenshot(page, selector, outputPath) {
  await page.evaluate((target) => {
    for (const board of document.querySelectorAll(".artboard")) {
      board.style.display = board.matches(target) ? "block" : "none";
    }
    window.scrollTo(0, 0);
  }, selector);
  const element = await page.$(selector);
  if (!element) throw new Error(`Missing selector: ${selector}`);
  await element.screenshot({ path: outputPath });
  console.log(`Wrote ${path.relative(PROJECT_ROOT, outputPath)}`);
}

fs.mkdirSync(OUT_DIR, { recursive: true });
const { chromium } = loadPlaywright();
const browser = await chromium.launch({ channel: "chrome", headless: true });
const page = await browser.newPage({ viewport: { width: 1200, height: 800 }, deviceScaleFactor: 1 });
await page.setContent(html, { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready);
await screenshot(page, "#eyecatch", path.join(OUT_DIR, "how-to-dispose-eyecatch.png"));
await screenshot(page, "#funnel", path.join(OUT_DIR, "how-to-dispose-inline-funnel.png"));
await screenshot(page, "#matrix", path.join(OUT_DIR, "how-to-dispose-inline-method-matrix.png"));
await screenshot(page, "#boundary", path.join(OUT_DIR, "how-to-dispose-inline-pro-boundary.png"));
await browser.close();
