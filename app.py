import re

import streamlit as st
import streamlit.components.v1 as components

# Put your deployed Streamlit URL here (e.g. "https://your-app.streamlit.app").
# Then each user's QR code is a link, so even the phone's normal camera opens
# their profile. Leave empty to use in-app scanning only.
APP_URL = ""

st.set_page_config(
    page_title="Social Hub",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {visibility: hidden; height: 0; display: none;}
      html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], section.main {
        overflow: hidden !important; height: 100vh; height: 100dvh; margin: 0; padding: 0;
        background: #0b0f14;
      }
      .block-container, [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 480px; margin: 0 auto;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      [data-testid="stElementContainer"] {margin: 0 !important;}
      iframe {border: 0; display: block; width: 100%; height: 100vh !important; height: 100dvh !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML = r'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Social Hub</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Grand+Hotel&display=swap">
<style>
:root{--bg:#0b0f14;--sf:#262b32;--tx:#f5f6f7;--mt:#a3a9b1;--ln:#1c222a;--ac:#8ea6ff;color-scheme:dark;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*,*::before,*::after{box-sizing:inherit;margin:0}
html,body{height:100%}
body{background:var(--bg);color:var(--tx);font:15px/1.35 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-tap-highlight-color:transparent}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
input{font:inherit;color:inherit}
svg{display:block}
#app{height:100%;max-width:480px;margin:0 auto;display:flex;flex-direction:column;position:relative;overflow:hidden}
#main{flex:1;overflow-y:auto;position:relative;min-height:0}
#main.reels{overflow:hidden}
.top{display:flex;align-items:center;justify-content:space-between;padding:14px 16px}
.top h1{font:400 34px "Grand Hotel",cursive}
.top h2{font-size:20px;font-weight:700;display:flex;align-items:center;gap:4px}
.ib{padding:4px;display:grid;place-items:center;position:relative}
.badge{position:absolute;top:-4px;right:-6px;background:#ff3040;color:#fff;font-size:11px;font-weight:700;border-radius:10px;min-width:18px;height:18px;display:grid;place-items:center;padding:0 4px}
.av{border-radius:50%;display:grid;place-items:center;font-weight:700;color:#fff;flex:none;text-shadow:0 1px 3px #0006}
.stories{display:flex;gap:14px;padding:6px 16px 14px;overflow-x:auto;scrollbar-width:none}
.st{display:flex;flex-direction:column;align-items:center;gap:6px;width:76px;flex:none;font-size:12px}
.st span{max-width:76px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ring{padding:3px;border-radius:50%;background:conic-gradient(#f5a623,#e1306c,#c13584,#f5a623)}
.ring.seen{background:#3a4048}
.ring .in{padding:3px;background:var(--bg);border-radius:50%}
.me{position:relative}
.plus{position:absolute;right:-2px;bottom:-2px;width:26px;height:26px;border-radius:50%;background:var(--tx);color:#000;border:3px solid var(--bg);display:grid;place-items:center}
.ph{display:flex;align-items:center;gap:10px;padding:8px 14px}
.ph div:nth-child(2){flex:1;min-width:0}
.ph b{display:flex;align-items:center;gap:4px;font-size:14px}
.ph small{color:var(--mt);font-size:12px}
.media{aspect-ratio:4/5;background-size:cover;background-position:center;display:grid;place-items:center;text-align:center;user-select:none}
.media h2{font-size:34px;line-height:1.15;font-weight:600;text-shadow:0 2px 12px #0008;padding:0 20px}
.acts{display:flex;align-items:center;gap:6px;padding:10px 12px 4px}
.acts .sp{flex:1}
.act{display:flex;align-items:center;gap:6px;padding:4px 6px;font-size:14px}
.on svg{fill:#ff3b5c;stroke:#ff3b5c}
.act.sv.on svg{fill:var(--tx);stroke:var(--tx)}
.meta{padding:0 16px 18px;font-size:14px}
.meta p{margin-top:2px}
.meta .mt{color:var(--mt)}
nav{display:flex;justify-content:space-around;align-items:center;padding:8px 6px 10px;background:var(--bg);border-top:1px solid var(--ln)}
nav button{width:64px;height:48px;border-radius:24px;display:grid;place-items:center;position:relative}
nav button.act-t{background:var(--sf)}
nav .dot{position:absolute;top:10px;right:16px;width:9px;height:9px;border-radius:50%;background:#ff3040}
.reel{height:100%;scroll-snap-align:start;position:relative;display:grid;place-items:center;overflow:hidden}
.reel h2{font-size:30px;text-align:center;line-height:1.2;text-shadow:0 2px 12px #0008;padding:0 70px}
#reels{height:100%;overflow-y:auto;scroll-snap-type:y mandatory;scrollbar-width:none}
.rtop{position:absolute;top:0;left:0;right:0;z-index:5;display:flex;align-items:center;justify-content:center;padding:14px 16px;font-size:20px;font-weight:700;gap:18px}
.rtop .ib:first-child{position:absolute;left:12px}
.side{position:absolute;right:10px;bottom:90px;display:flex;flex-direction:column;gap:14px;align-items:center}
.side .act{flex-direction:column;gap:2px;font-size:13px;font-weight:600}
.rb{position:absolute;left:14px;right:70px;bottom:18px}
.rb .row{display:flex;align-items:center;gap:10px;margin-bottom:8px;font-weight:600}
.fb{border:1px solid #fff9;border-radius:10px;padding:5px 16px;font-weight:600;font-size:14px}
.fb.on{background:#fff2;border-color:transparent}
.search{display:flex;gap:12px;align-items:center;padding:14px 16px}
.pill{flex:1;display:flex;align-items:center;gap:10px;background:var(--sf);border-radius:26px;padding:12px 16px;color:var(--mt)}
.pill input{flex:1;background:none;border:0;outline:0;min-width:0}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px}
.tile{aspect-ratio:3/4;background-size:cover;background-position:center;display:flex;align-items:flex-end;padding:8px;font-size:14px;font-weight:600;gap:4px;position:relative;font-size:13px}
.tile i{position:absolute;inset:0;display:grid;place-items:center;font-style:normal;font-size:40px;opacity:.55}
.tile span{position:relative;display:flex;align-items:center;gap:4px;text-shadow:0 1px 4px #000a}
.phead{display:flex;align-items:center;gap:26px;padding:6px 16px}
.stats{display:flex;flex:1;justify-content:space-between;text-align:left}
.stats b{display:block;font-size:20px}
.note{position:absolute;top:-34px;left:-4px;background:#3a4048;color:var(--mt);font-size:12px;border-radius:16px;padding:8px 12px;width:104px;text-align:center;z-index:2}
.btns{display:flex;gap:8px;padding:12px 16px}
.btn{flex:1;background:var(--sf);border-radius:12px;padding:10px;font-weight:600;font-size:14px;text-align:center}
.btn.sq{flex:none;width:46px;display:grid;place-items:center;padding:0}
.hl{display:flex;gap:16px;padding:6px 16px 14px;overflow-x:auto;scrollbar-width:none}
.hl div{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:13px;width:70px;flex:none}
.hl .c{width:68px;height:68px;border-radius:50%;border:2px solid #3a4048;padding:3px}
.hl .c>*{width:100%;height:100%;border-radius:50%;display:grid;place-items:center;font-size:22px}
.tabs{display:flex;border-bottom:1px solid var(--ln)}
.tabs button{flex:1;padding:12px;display:grid;place-items:center;color:var(--mt);border-bottom:2px solid transparent}
.tabs button.on{color:var(--tx);border-color:var(--tx)}
.tabs button.on svg{fill:none;stroke:var(--tx)}
.cp{padding:22px 16px 10px}
.cp small{color:var(--mt);font-size:14px}
.cards{display:flex;gap:12px;overflow-x:auto;padding:12px 16px 24px;scrollbar-width:none}
.card{flex:none;width:200px;border:1px solid #2a3139;border-radius:14px;padding:18px 14px;text-align:center;font-size:14px}
.card b{display:block;margin-bottom:4px}
.card span{color:var(--mt);font-size:13px}
.sec{color:var(--mt);padding:18px 16px 8px;font-weight:600;font-size:14px}
.row2{display:flex;align-items:center;gap:16px;padding:14px 16px;width:100%;text-align:left}
.row2 div{flex:1}
.row2 small{display:block;color:var(--mt);font-size:14px}
.row2 b{font-weight:600;font-size:16px}
.sep{height:6px;background:var(--ln)}
.chat{display:flex;align-items:center;gap:12px;padding:10px 16px;width:100%;text-align:left}
.chat div{flex:1;min-width:0}
.chat small{display:block;color:var(--mt);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.chat .u{width:9px;height:9px;border-radius:50%;background:var(--ac)}
.ov{position:absolute;inset:0;z-index:50}
.sh{background:#0009;display:flex;align-items:flex-end;z-index:60}
.pn{background:#161b21;width:100%;border-radius:20px 20px 0 0;padding:20px 16px calc(20px + env(safe-area-inset-bottom,0px));display:flex;flex-direction:column;gap:12px}
.pn h3{text-align:center;font-size:16px}
.fld{background:var(--sf);border:0;border-radius:12px;padding:12px 14px;outline:0;width:100%}
.pre{height:200px;border-radius:12px;background:var(--sf) center/cover;display:grid;place-items:center;color:var(--mt)}
.go{background:#4a6cf7;color:#fff;border-radius:12px;padding:12px;font-weight:600}
.svw{display:flex;flex-direction:column;justify-content:center;align-items:center;font-size:30px;text-align:center;padding:0 30px}
.bar{position:absolute;top:12px;left:12px;right:12px;height:3px;background:#fff4;border-radius:3px;overflow:hidden}
.bar i{display:block;height:100%;background:#fff;width:0;animation:fill 4s linear forwards}
@keyframes fill{to{width:100%}}
.svh{position:absolute;top:26px;left:14px;display:flex;align-items:center;gap:10px;font-weight:600;font-size:15px}
#toast{position:absolute;left:50%;bottom:90px;transform:translateX(-50%);background:#e8eaed;color:#111;padding:10px 16px;border-radius:12px;font-size:14px;z-index:90;opacity:0;pointer-events:none;transition:opacity .2s;white-space:nowrap}
#toast.show{opacity:1}
@media (prefers-reduced-motion:reduce){.bar i{animation-duration:.01s}}

.auth{padding:40px 24px;display:flex;flex-direction:column;gap:12px;min-height:100%;justify-content:center}
.auth h1{font:400 56px "Grand Hotel",cursive;text-align:center;margin-bottom:10px}
.auth .sw{text-align:center;color:var(--mt);font-size:14px}.auth .sw b{color:var(--ac);cursor:pointer}
.msg{color:#ffb4b4;font-size:13px;text-align:center;min-height:18px}.msg.ok{color:#9fe3b0}
.cm{max-height:45vh;overflow-y:auto;display:flex;flex-direction:column;gap:10px;font-size:14px}
.cr{display:flex;gap:8px}.cr .fld{flex:1}.cr .go{padding:0 18px}
.empty{padding:50px 20px;text-align:center;color:var(--mt)}
.ph .ib{margin-left:auto}
.media img{width:100%;height:100%;object-fit:cover;display:block}
.tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.reel img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.reel::after{content:"";position:absolute;inset:0;background:linear-gradient(transparent 55%,#000a);pointer-events:none}
.side,.rb{z-index:2}
.msgs{display:flex;flex-direction:column;gap:6px;padding:8px 14px 16px}
.bub{max-width:75%;padding:9px 13px;border-radius:18px;background:var(--sf);word-break:break-word;font-size:15px}
.bub.me{margin-left:auto;background:#4a6cf7;color:#fff}
.cb{position:sticky;bottom:0;display:flex;gap:8px;padding:10px 14px;background:var(--bg);border-top:1px solid var(--ln)}
.cb .fld{flex:1}.cb .go{padding:0 18px}
.rt{color:#fff9;font-size:20px;font-weight:700;display:flex;align-items:center;gap:4px;text-shadow:0 1px 6px #0008}.rt.on{color:#fff}
.reel video,.tile video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.reel video{object-fit:contain;background:#000}
.cap{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;font-size:14px;line-height:1.35;cursor:pointer}.cap.x{display:block;max-height:30vh;overflow-y:auto}.more{display:block;color:#fffc;font-size:14px;font-weight:600;cursor:pointer;margin-top:2px}.cap.x+.more{display:none}
.media video{width:100%;height:100%;object-fit:cover;display:block}
.tile .rbadge{position:absolute;top:6px;right:6px;display:block}
.act.rp.on svg{fill:none;stroke:#3ddc84}
.side .act{text-shadow:0 1px 4px #000a}.side .act svg{filter:drop-shadow(0 1px 3px #0008)}
.rb{text-shadow:0 1px 4px #000a}.rb .row b{cursor:pointer}
.btn.on{background:var(--sf)}.btn.pri{background:#4a6cf7;color:#fff}
.card{width:164px}.card .av{margin:0 auto 8px}.card .btn{margin-top:12px;display:block;width:100%}
.card small{display:block;color:var(--mt);font-size:12px;min-height:30px}
.chips{display:flex;gap:8px;justify-content:center}.chip{padding:7px 18px;border-radius:18px;background:var(--sf);font-weight:600;font-size:14px;color:var(--mt)}.chip.on{background:var(--tx);color:#000}
.pre{overflow:hidden}.pre video{width:100%;height:100%;object-fit:cover}
.lock{display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;padding:50px 30px;color:var(--mt)}.lock b{color:var(--tx);font-size:16px}.lock svg{color:var(--tx)}
.opt{display:flex;align-items:center;gap:14px;padding:14px 16px;width:100%;text-align:left}.opt div{flex:1}.opt b{font-size:16px;font-weight:600}.opt small{display:block;color:var(--mt);font-size:13px;margin-top:2px}
.rad{width:22px;height:22px;border-radius:50%;border:2px solid #5a626b;flex:none}.opt.on .rad{border:7px solid #4a6cf7}
.frm{display:flex;flex-direction:column;gap:10px;padding:4px 16px 18px}
.go.sm{padding:8px 14px;font-size:14px}.go:disabled{opacity:.6}
.shr{padding:6px;max-width:55%;cursor:pointer}.shr .thumb{aspect-ratio:3/4;border-radius:12px;overflow:hidden;background:#000}.shr img,.shr video{width:100%;height:100%;object-fit:cover;display:block}.shr small{display:block;padding:6px 4px 2px;opacity:.85}
.row2 .badge{position:static}
.tabs button svg{margin:0 auto}
.stats>div[data-a]{cursor:pointer}
.chat .av,.row2 .av{flex:none}
b svg,h2 svg{display:inline-block;vertical-align:-2px;margin-left:2px}
</style></head><body>
<div id="app"><div id="main"></div><nav id="nav"></nav><div id="toast"></div></div>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/qrcode-generator@1.4.4/qrcode.js"></script>
<script src="https://cdn.jsdelivr.net/npm/tus-js-client@4.1.0/dist/tus.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jsqr@1.4.0/dist/jsQR.js"></script>
<script>
const I={plus:'<path d="M12 5v14M5 12h14"/>',heart:'<path d="M12 21s-7-4.6-9.3-9A5.3 5.3 0 0 1 12 6.5 5.3 5.3 0 0 1 21.3 12C19 16.4 12 21 12 21z"/>',home:'<path d="M3 11l9-8 9 8v10h-6v-6H9v6H3z"/>',reels:'<rect x="3" y="3" width="18" height="18" rx="5"/><path d="M10 8l6 4-6 4z"/>',send:'<path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/>',search:'<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/>',comment:'<path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6A8 8 0 1 1 21 12z"/>',mark:'<path d="M6 3h12v18l-6-4-6 4z"/>',repost:'<path d="M17 2l4 4-4 4M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4M21 13v2a3 3 0 0 1-3 3H3"/>',menu:'<path d="M3 7h18M3 12h18M3 17h18"/>',dots:'<path d="M4 9h16M4 15h10"/>',grid:'<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>',tag:'<rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="12" cy="10" r="3"/><path d="M6 19a6 6 0 0 1 12 0"/>',back:'<path d="M15 18l-6-6 6-6"/>',chev:'<path d="M9 6l6 6-6 6"/>',down:'<path d="M6 9l6 6 6-6"/>',qr:'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM20 14v1M14 20h1M18 18h3v3"/>',clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',bell:'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8M10 21h4"/>',pulse:'<path d="M3 12h4l3-8 4 16 3-8h4"/>',user:'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',lock:'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',star:'<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.2 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>',block:'<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',help:'<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 17h.01"/>',out:'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>',users:'<circle cx="9" cy="8" r="3.5"/><path d="M2 21a7 7 0 0 1 14 0M16 4.5a3.5 3.5 0 0 1 0 7M22 21a7 7 0 0 0-4-6.3"/>'};
const ic=(n,s=24)=>`<svg viewBox="0 0 24 24" width="${s}" height="${s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">${I[n]}</svg>`;
const tick='<svg viewBox="0 0 24 24" width="15" height="15"><path fill="#3897f0" d="M12 1l2.4 2 3.1-.3 1 3 2.7 1.6-.8 3L21 13l-2 2.4.3 3.1-3 1-1.6 2.7-3-.8L9 23l-2.4-2-3.1.3-1-3L.8 16l.8-3L0 10.6l2-2.4-.3-3.1 3-1L6.4 1.4l3 .8z" transform="scale(.95) translate(.6 .6)"/><path d="M8 12.4l2.7 2.7L16 9.7" fill="none" stroke="#fff" stroke-width="2"/></svg>';
window.APP_URL="__APP_URL__";window.OPEN_USER="__OPEN_USER__";
const SB_URL='https://vwxkbhrasiyafzbkaqvg.supabase.co',SB_KEY='sb_publishable_6soG-EJIOYUUHiSfVvxpVA_emGkRpCM';
const sb=supabase.createClient(SB_URL,SB_KEY);
const G=['#3a6073,#16222a','#e96443,#904e95','#134e5e,#71b280','#41295a,#2f0743','#f7971e,#a8431a','#0f2027,#2c5364','#614385,#516395','#c33764,#1d2671'];
const $=s=>document.querySelector(s);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=n=>n>=1e5?Math.round(n/1e3)+'K':n.toLocaleString('en-US');
const gi=u=>(u||'a').charCodeAt(0)%8;
const av=(n,s)=>S.AV&&S.AV[n]?`<div class="av" style="width:${s}px;height:${s}px;background:#262b32 url('${esc(S.AV[n])}') center/cover"></div>`:`<div class="av" style="width:${s}px;height:${s}px;font-size:${s*.4}px;background:linear-gradient(135deg,${G[gi(n)]})">${esc((n||'?')[0].toUpperCase())}</div>`;
async function loadAv(){try{const r=await sb.from('profiles').select('username,avatar_url').not('avatar_url','is',null).limit(1000);S.AV={};(r.data||[]).forEach(x=>{S.AV[x.username]=x.avatar_url})}catch(e){S.AV={}}}
const S={AV:{},tab:'home',unread:false,ST:{},me:null,L:new Set(),V:new Set(),R:new Set(),F:new Set(),P:new Set(),mode:'in',np:'post',rt:'all',pt:'posts',req:0};
const hdr=(l,r)=>`<div class="top"><button class="ib" data-a="post" aria-label="New post">${ic('plus',30)}</button>${l}<div>${r}</div></div>`;
const back=(t,to,id='')=>`<div class="top" style="justify-content:flex-start;gap:20px"><button class="ib" data-a="go" data-v="${to}" data-id="${id}" aria-label="Back">${ic('back',30)}</button><h2>${t}</h2></div>`;
const cn=(p,t)=>p[t]?.[0]?.count||0;
const isOn=(t,k)=>t==='likes'?S.L.has(k):t==='reposts'?S.R.has(k):t==='saves'?S.V.has(k):false;
const tot=(p,t)=>t==='saves'?(p.savec||0):cn(p,t);
const cnt=(p,t,s='')=>{const o=isOn(t,p.id)?1:0,b=tot(p,t)-o;return `<span class="n" data-c="${t}" data-k="${p.id}" data-b="${b}" data-s="${s}">${fmt(b+o)}${s}</span>`};
const ab=(a,p,i,sz,on,cl='')=>`<button class="act ${cl} ${on?'on':''}" data-a="${a}" data-k="${p.id}" aria-label="${a}">${ic(i,sz)}</button>`;
const rb=(a,p,i,t,cl='')=>`<button class="act ${cl} ${isOn(t,p.id)?'on':''}" data-a="${a}" data-k="${p.id}" aria-label="${a}">${ic(i,32)}${cnt(p,t)}</button>`;
const flab=id=>S.F.has(id)?'Following':S.P.has(id)?'Requested':'Follow';
const fbtn=(id,cl,pv,x='')=>{const on=S.F.has(id)||S.P.has(id);return `<button class="${cl} ${on?'on':'pri'}" data-a="follow" data-v="${id}" data-pv="${pv?1:0}" ${x}>${flab(id)}</button>`};
const mediaEl=p=>p.media_type==='video'?`<video src="${esc(p.image_url)}" muted loop playsinline preload="metadata" data-a="vt"></video>`:`<img src="${esc(p.image_url)}" alt="" loading="lazy">`;
const SEL='id,image_url,media_type,kind,caption,user_id,profiles!user_id(username,is_private),likes(count),comments(count),reposts(count),shares(count)';
async function attach(ps){if(!ps.length)return ps;try{const{data}=await sb.rpc('save_counts',{ids:ps.map(p=>p.id)});const m={};(data||[]).forEach(x=>m[x.post_id]=x.n);ps.forEach(p=>p.savec=m[p.id]||0)}catch(e){}return ps}
async function feed(o={}){let q=sb.from('posts').select(SEL).order('created_at',{ascending:false}).limit(o.kind==='reel'?80:40);if(o.uid)q=q.eq('user_id',o.uid);if(o.kind)q=q.eq('kind',o.kind);if(o.friends){const ids=[...S.F];if(!ids.length)return[];q=q.in('user_id',ids)}const{data,error}=await q;if(error)throw error;return attach(data||[])}
async function loadMine(){const u=S.me.id;const[l,v,f,r]=await Promise.all([sb.from('likes').select('post_id').eq('user_id',u),sb.from('saves').select('post_id').eq('user_id',u),sb.from('follows').select('following_id,status').eq('follower_id',u),sb.from('reposts').select('post_id').eq('user_id',u)]);S.L=new Set((l.data||[]).map(x=>x.post_id));S.V=new Set((v.data||[]).map(x=>x.post_id));S.R=new Set((r.data||[]).map(x=>x.post_id));const fl=f.data||[];S.F=new Set(fl.filter(x=>x.status==='accepted').map(x=>x.following_id));S.P=new Set(fl.filter(x=>x.status==='pending').map(x=>x.following_id))}
async function loadReq(){const{count}=await sb.from('follows').select('*',{count:'exact',head:true}).eq('following_id',S.me.id).eq('status','pending');S.req=count||0;nav()}
function authView(){const up=S.mode==='up';return `<div class="auth"><h1>Social Hub</h1>${up?'<input class="fld" id="au" placeholder="Username (a-z, 0-9, . _)" autocapitalize="none" aria-label="Username">':''}<input class="fld" id="ae" type="email" placeholder="Email" aria-label="Email"><input class="fld" id="ap" type="password" placeholder="Password (min 6)" aria-label="Password"><div class="msg" id="am"></div><button class="go" data-a="auth">${up?'Sign up':'Log in'}</button><div class="sw">${up?'Already have an account? <b data-a="mode" data-v="in">Log in</b>':'New here? <b data-a="mode" data-v="up">Sign up</b>'}</div></div>`}
function postHTML(p){const u=p.profiles?.username||'user';return `<article><div class="ph">${av(u,36)}<div data-a="go" data-v="profile" data-id="${p.user_id}" style="cursor:pointer"><b>${esc(u)}${p.profiles?.is_private?ic('lock',13):''}</b></div>${p.user_id===S.me.id?`<button class="ib" data-a="del" data-k="${p.id}" aria-label="Delete post">${ic('block',22)}</button>`:''}</div><div class="media" data-k="${p.id}">${mediaEl(p)}</div><div class="acts">${ab('like',p,'heart',26,S.L.has(p.id))}${ab('cm',p,'comment',26)}${ab('repost',p,'repost',26,S.R.has(p.id),'rp')}${ab('sendp',p,'send',26)}<span class="sp"></span>${ab('save',p,'mark',26,S.V.has(p.id),'sv')}</div><div class="meta"><b>${cnt(p,'likes',' likes')}</b>${p.caption?`<p><b>${esc(u)}</b> ${esc(p.caption)}</p>`:''}<p class="mt" data-a="cm" data-k="${p.id}">View all ${cn(p,'comments')} comments</p></div></article>`}
async function suggest(){const r=await sb.rpc('suggested_users',{lim:12});let l=r.data||[];
 if(!l.length){const ex=[S.me.id,...S.F,...S.P];const q=await sb.from('profiles').select('id,username,full_name,is_private').not('id','in',`(${ex.join(',')})`).order('created_at',{ascending:false}).limit(10);l=(q.data||[]).map(x=>({...x,via:null,mutuals:0}))}
 if(!l.length)return '';
 return `<div class="cp"><b>Suggested for you</b></div><div class="cards">`+l.map(u=>`<div class="card"><div data-a="go" data-v="profile" data-id="${u.id}" style="cursor:pointer">${av(u.username,64)}<b>${esc(u.username)}${u.is_private?' '+ic('lock',12):''}</b></div><small>${u.via?(u.mutuals>1?`Followed by ${esc(u.via)} + ${u.mutuals-1} more`:`Followed by ${esc(u.via)}`):'New on Social Hub'}</small>${fbtn(u.id,'btn',u.is_private)}</div>`).join('')+'</div>'}
async function home(){const ids=[...S.F];const[ps,pr,,sg]=await Promise.all([feed({kind:'post'}),ids.length?sb.from('profiles').select('id,username').in('id',ids).limit(30):Promise.resolve({data:[]}),loadStories(),suggest()]);
 const mine=S.ST[S.me.id];
 let s=`<div class="stories"><div class="st"><div class="me" data-a="${mine?'story':'storyAdd'}" data-id="${S.me.id}">${mine?`<div class="ring"><div class="in">${av(S.me.username,64)}</div></div>`:av(S.me.username,70)}<div class="plus" data-a="storyAdd">${ic('plus',14)}</div></div><span>Your story</span></div>`;
 const us=(pr.data||[]).sort((a,b)=>(S.ST[b.id]?1:0)-(S.ST[a.id]?1:0));
 us.forEach(u=>{const h=S.ST[u.id];s+=`<div class="st" data-a="${h?'story':'go'}" data-v="profile" data-id="${u.id}">${h?`<div class="ring"><div class="in">${av(u.username,64)}</div></div>`:av(u.username,70)}<span>${esc(u.username)}</span></div>`});
 s+='</div>';
 const h=ps.map(postHTML);
 s+=h.slice(0,2).join('')+sg+h.slice(2).join('');
 if(!ps.length)s+='<div class="empty">No posts yet. Tap + to share the first one.</div>';
 return hdr('<h1>Social Hub</h1>','<span style="width:30px;display:block"></span>')+s}
async function loadStories(){const{data}=await sb.from('stories').select('id,image_url,user_id,profiles!user_id(username)').gt('expires_at',new Date().toISOString()).order('created_at');S.ST={};(data||[]).forEach(x=>{(S.ST[x.user_id]??=[]).push(x)})}
function showStory(uid,i){close();clearTimeout(showStory.t);const L=S.ST[uid];if(!L||i>=L.length)return;const s=L[i];const d=document.createElement('div');d.className='ov';d.style.background='#000';d.innerHTML=`<img src="${esc(s.image_url)}" alt="" style="width:100%;height:100%;object-fit:contain" data-a="nx" data-u="${uid}" data-i="${i+1}"><div class="bar"><i></i></div><div class="svh">${av(s.profiles?.username,34)}${esc(s.profiles?.username)}</div><button class="ib" data-a="xs" aria-label="Close" style="position:absolute;top:22px;right:12px;font-size:22px">✕</button>`;$('#app').appendChild(d);showStory.t=setTimeout(()=>showStory(uid,i+1),5000)}
function reelHTML(p){const u=p.profiles?.username||'user',own=p.user_id===S.me.id;
 return `<section class="reel" style="background:#000" data-k="${p.id}">${mediaEl(p)}<div class="side">${rb('like',p,'heart','likes')}${rb('cm',p,'comment','comments')}${rb('repost',p,'repost','reposts','rp')}${rb('sendp',p,'send','shares')}${rb('save',p,'mark','saves','sv')}</div><div class="rb"><div class="row" data-a="go" data-v="profile" data-id="${p.user_id}">${av(u,38)}<b>${esc(u)}</b>${own?`<button class="fb" data-a="del" data-k="${p.id}">Delete</button>`:fbtn(p.user_id,'fb',p.profiles?.is_private)}</div>${p.caption?`<div class="cap" data-a="capx">${esc(p.caption)}</div>`:''}</div></section>`}
async function reels(){const fr=S.rt==='friends';const ps=await feed({kind:'reel',friends:fr});
 return `<div class="rtop"><button class="ib" data-a="newp" data-v="reel" aria-label="New reel">${ic('plus',30)}</button><button class="rt ${fr?'':'on'}" data-a="rt" data-v="all">Reels ${ic('down',16)}</button><button class="rt ${fr?'on':''}" data-a="rt" data-v="friends">Friends</button></div><div id="reels">`+(ps.length?ps.map(reelHTML).join(''):`<div class="empty" style="padding-top:35vh">${fr?'No reels from people you follow yet.':'No reels yet. Tap + to upload one.'}</div>`)+'</div>'}
function watchReels(root){const r=root||$('#reels');if(!r)return;r.querySelectorAll('.cap').forEach(c=>{if(!c.nextElementSibling?.classList.contains('more')&&c.scrollHeight>c.clientHeight+1)c.insertAdjacentHTML('afterend','<span class="more" data-a="capm">more</span>')});watchReels.io&&watchReels.io.disconnect();const io=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target.querySelector('video');if(!v)return;if(e.isIntersecting)v.play().catch(()=>{});else{v.pause();v.currentTime=0}}),{root:r,threshold:.6});r.querySelectorAll('.reel').forEach(s=>io.observe(s));watchReels.io=io}
const tile=p=>`<div class="tile" data-a="openPost" data-k="${p.id}">${p.media_type==='video'?`<video src="${esc(p.image_url)}#t=0.1" muted playsinline preload="metadata"></video><span class="rbadge">${ic('reels',20)}</span>`:`<img src="${esc(p.image_url)}" alt="" loading="lazy">`}</div>`;
async function explore(){const[ps,sg]=await Promise.all([feed(),suggest()]);return `<div class="search"><div class="pill">${ic('search',22)}<input id="q" placeholder="Search people" aria-label="Search people" autocapitalize="none"></div><button class="ib" data-a="scan" aria-label="Scan QR">${ic('qr',28)}</button></div><div id="res"></div>${sg}<div class="grid">`+ps.map(tile).join('')+'</div>'+(ps.length?'':'<div class="empty">Nothing to explore yet</div>')}
async function msgs(){const me=S.me.id;const{data}=await sb.from('messages').select('sender_id,receiver_id,body,read_at').or(`sender_id.eq.${me},receiver_id.eq.${me}`).order('created_at',{ascending:false}).limit(200);const last={};(data||[]).forEach(m=>{const o=m.sender_id===me?m.receiver_id:m.sender_id;if(!last[o])last[o]=m});const ids=Object.keys(last),nm={};if(ids.length){const r=await sb.from('profiles').select('id,username').in('id',ids);(r.data||[]).forEach(u=>nm[u.id]=u.username)}
 return `<div class="top"><h2>${esc(S.me.username)}</h2></div><div class="search" style="padding-top:0"><div class="pill">${ic('search',20)}<input id="mq" placeholder="Find someone to message" aria-label="Find someone" autocapitalize="none"></div></div><div id="mres"></div>`+(ids.map(o=>{const m=last[o],un=m.receiver_id===me&&!m.read_at;return `<button class="chat" data-a="chat" data-id="${o}">${av(nm[o],52)}<div><b>${esc(nm[o])}</b><small>${m.sender_id===me?'You: ':''}${esc(m.body)}</small></div>${un?'<span class="u"></span>':''}</button>`}).join('')||'<div class="empty">No messages yet. Search for someone above.</div>')}
async function chat(id){const me=S.me.id;S.chat=id;const[p,m]=await Promise.all([sb.from('profiles').select('id,username').eq('id',id).single(),sb.from('messages').select('id,sender_id,body,post_id,posts(image_url,media_type,profiles!user_id(username))').or(`and(sender_id.eq.${me},receiver_id.eq.${id}),and(sender_id.eq.${id},receiver_id.eq.${me})`).order('created_at').limit(200)]);const u=p.data?.username||'user';
 sb.from('messages').update({read_at:new Date().toISOString()}).eq('receiver_id',me).eq('sender_id',id).is('read_at',null).then(refreshUnread);
 return `<div class="top" style="justify-content:flex-start;gap:12px"><button class="ib" data-a="go" data-v="msgs" aria-label="Back">${ic('back',28)}</button>${av(u,36)}<h2>${esc(u)}</h2></div><div class="msgs" id="ml">${(m.data||[]).map(bub).join('')}</div><div class="cb"><input class="fld" id="mi" placeholder="Message…" maxlength="1000" aria-label="Message"><button class="go" data-a="dm" data-id="${id}">Send</button></div>`}
const bub=m=>{const c=m.sender_id===S.me.id?'me':'';if(!m.post_id)return `<div class="bub ${c}">${esc(m.body)}</div>`;const p=m.posts;return `<div class="bub shr ${c}" data-a="openPost" data-k="${m.post_id}">${p?`<div class="thumb">${p.media_type==='video'?`<video src="${esc(p.image_url)}#t=0.1" muted playsinline preload="metadata"></video>`:`<img src="${esc(p.image_url)}" alt="">`}</div><small>${esc(p.profiles?.username||'')}</small>`:'Shared a post'}</div>`};
async function refreshUnread(){const{count}=await sb.from('messages').select('*',{count:'exact',head:true}).eq('receiver_id',S.me.id).is('read_at',null);S.unread=count>0;nav()}
function subscribe(){sb.removeAllChannels();sb.channel('dm').on('postgres_changes',{event:'INSERT',schema:'public',table:'messages',filter:`receiver_id=eq.${S.me.id}`},p=>{const m=p.new;if(S.tab==='chat'&&S.chat===m.sender_id){$('#ml').insertAdjacentHTML('beforeend',bub(m));$('#main').scrollTop=1e9;sb.from('messages').update({read_at:new Date().toISOString()}).eq('id',m.id)}else{S.unread=true;nav();toast('New message')}}).subscribe()}
async function profile(id){id=id||S.me.id;const own=id===S.me.id;
 const pr=await sb.from('profiles').select('id,username,full_name,bio,is_private').eq('id',id).single();const u=pr.data;if(!u)return '<div class="empty">Profile not found</div>';
 if(own)S.me={...S.me,...u};
 const can=own||!u.is_private||S.F.has(id),pt=S.pt;let st=null,ps=[];
 if(can){const q=pt==='reposts'?sb.from('reposts').select(`posts(${SEL})`).eq('user_id',id).order('created_at',{ascending:false}).limit(40):feed({uid:id,kind:pt==='reels'?'reel':'post'});
  const[a,b]=await Promise.all([sb.rpc('profile_stats',{uid:id}),q,loadStories()]);st=a.data;ps=pt==='reposts'?await attach((b.data||[]).map(x=>x.posts).filter(Boolean)):b}
 const ava=can&&S.ST[id]?`<div class="ring" data-a="story" data-id="${id}"><div class="in">${av(u.username,80)}</div></div>`:av(u.username,86);
 const sv=k=>st?fmt(st[k]):'–',lnk=k=>can?`data-a="plist" data-v="${k}" data-id="${id}"`:'';
 const tb=(k,i)=>`<button class="${pt===k?'on':''}" data-a="ptab" data-v="${k}" data-id="${id}" aria-label="${k}">${ic(i,26)}</button>`;
 const emp={posts:'No posts yet',reels:'No reels yet',reposts:'No reposts yet'}[pt];
 return `<div class="top"><button class="ib" data-a="${own?'post':'go'}" data-v="home">${ic(own?'plus':'back',30)}</button><h2>${esc(u.username)}${u.is_private?ic('lock',16):''}</h2>${own?`<button class="ib" data-a="go" data-v="settings" aria-label="Settings">${ic('menu',30)}${S.req?'<span class="badge">'+S.req+'</span>':''}</button>`:'<span style="width:30px"></span>'}</div>
 <div class="phead">${ava}<div class="stats"><div><b>${sv('posts')}</b>posts</div><div ${lnk('followers')}><b>${sv('followers')}</b>followers</div><div ${lnk('following')}><b>${sv('following')}</b>following</div></div></div>
 <div style="padding:6px 16px"><b>${esc(u.full_name||'')}</b><div style="color:var(--mt)">${esc(u.bio||'')}</div></div>
 <div class="btns">${own?`<button class="btn" data-a="edit">Edit profile</button><button class="btn" data-a="share">Share profile</button>`:`${fbtn(id,'btn',u.is_private,'data-r="1"')}<button class="btn" data-a="chat" data-id="${id}">Message</button>`}</div>`
 +(can?`<div class="tabs">${tb('posts','grid')}${tb('reels','reels')}${tb('reposts','repost')}</div>`+(ps.length?'<div class="grid">'+ps.map(tile).join('')+'</div>':`<div class="empty">${emp}</div>`):`<div class="lock">${ic('lock',36)}<b>This account is private</b><span>Follow this account to see their posts, reels, stories, followers and following.</span></div>`)}
const urow=u=>`<div class="chat">${av(u.username,48)}<div data-a="go" data-v="profile" data-id="${u.id}" style="cursor:pointer"><b>${esc(u.username)}${u.is_private?' '+ic('lock',12):''}</b><small>${esc(u.full_name||'')}</small></div>${u.id===S.me.id?'':fbtn(u.id,'fb',u.is_private)}</div>`;
async function plist(){const{id,type}=S.pl;const pr=await sb.from('profiles').select('id,username,is_private').eq('id',id).single();const u=pr.data;if(!u)return '<div class="empty">Profile not found</div>';
 const hd=back(type==='followers'?'Followers':'Following','profile',id);
 if(!(id===S.me.id||!u.is_private||S.F.has(id)))return hd+`<div class="lock">${ic('lock',36)}<b>This account is private</b><span>Follow this account to see their followers and following.</span></div>`;
 const col=type==='followers'?'following_id':'follower_id',oc=type==='followers'?'follower_id':'following_id';
 const f=await sb.from('follows').select(oc).eq(col,id).eq('status','accepted').limit(200);const ids=(f.data||[]).map(x=>x[oc]);let us=[];
 if(ids.length){const r=await sb.from('profiles').select('id,username,full_name,is_private').in('id',ids);us=r.data||[]}
 return hd+(us.map(urow).join('')||`<div class="empty">${type==='followers'?'No followers yet':'Not following anyone yet'}</div>`)}
async function requests(){const f=await sb.from('follows').select('follower_id').eq('following_id',S.me.id).eq('status','pending');const ids=(f.data||[]).map(x=>x.follower_id);let us=[];
 if(ids.length){const r=await sb.from('profiles').select('id,username,full_name').in('id',ids);us=r.data||[]}
 return back('Follow requests','settings')+(us.map(u=>`<div class="chat" id="rq${u.id}">${av(u.username,48)}<div><b>${esc(u.username)}</b><small>${esc(u.full_name||'')}</small></div><button class="go sm" data-a="acc" data-id="${u.id}">Confirm</button><button class="fb" data-a="rej" data-id="${u.id}">Delete</button></div>`).join('')||'<div class="empty">No pending requests</div>')}
async function saved(){const r=await sb.from('saves').select(`posts(${SEL})`).eq('user_id',S.me.id).limit(60);const ps=await attach((r.data||[]).map(x=>x.posts).filter(Boolean));return back('Saved','settings')+(ps.length?'<div class="grid">'+ps.map(tile).join('')+'</div>':'<div class="empty">Posts and reels you save will show up here</div>')}
async function settings(){loadReq();const r=(i,t,a='toast',v=t+' is coming soon',sub='',bd='')=>`<button class="row2" data-a="${a}" data-v="${esc(v)}">${ic(i,28)}<div><b>${t}</b>${sub?`<small>${sub}</small>`:''}</div>${bd?`<span class="badge" style="position:static">${bd}</span>`:''}${ic('chev',22)}</button>`;
 return back('Settings and activity','profile')+`<div class="sec">Your account</div>${r('lock','Account privacy','go','privacy',S.me.is_private?'Private account':'Public account')}${r('users','Follow requests','go','requests','',S.req||'')}${r('user','Accounts Center')}<div class="sep"></div><div class="sec">How you use Social Hub</div>${r('mark','Saved','go','saved')}${r('clock','Archive')}${r('pulse','Your activity')}${r('bell','Notifications')}<div class="sep"></div><div class="sec">Who can see your content</div>${r('star','Close Friends')}${r('block','Blocked')}<div class="sep"></div><button class="row2" data-a="logout">${ic('out',28)}<div><b>Log out</b><small>${esc(S.me.email||'')}</small></div></button><div style="height:30px"></div>`}
async function privacy(){const{data}=await sb.from('user_private').select('phone').eq('id',S.me.id).maybeSingle();const ph=data?.phone||'',pv=!!S.me.is_private;
 return back('Account privacy','settings')+`<div class="sec">Account type</div>
 <button class="opt ${pv?'':'on'}" data-a="acct" data-v="public"><div><b>Public</b><small>Anyone can see your posts, reels, stories, followers and following.</small></div><i class="rad"></i></button>
 <button class="opt ${pv?'on':''}" data-a="acct" data-v="private"><div><b>Private</b><small>Only people you approve can see your posts, reels, stories, followers and following.</small></div><i class="rad"></i></button>
 <div class="sep"></div><div class="sec">Mobile number</div><div class="frm"><input class="fld" id="ph" type="tel" inputmode="tel" placeholder="+91 98765 43210" value="${esc(ph)}" maxlength="20" aria-label="Mobile number"><button class="go" data-a="savePh">${ph?'Update number':'Add number'}</button></div>
 <div class="sep"></div><div class="sec">Change password</div><div class="frm"><input class="fld" id="p0" type="password" placeholder="Current password" autocomplete="current-password" aria-label="Current password"><input class="fld" id="p1" type="password" placeholder="New password (min 6)" autocomplete="new-password" aria-label="New password"><input class="fld" id="p2" type="password" placeholder="Confirm new password" autocomplete="new-password" aria-label="Confirm new password"><div class="msg" id="pm"></div><button class="go" data-a="savePw">Change password</button></div><div style="height:30px"></div>`}
function nav(){if(!S.me){$('#nav').innerHTML='';return}const t=({settings:'profile',privacy:'profile',requests:'profile',saved:'profile',plist:'profile',chat:'msgs'})[S.tab]||S.tab;$('#nav').innerHTML=[['home','home'],['reels','reels'],['msgs','send'],['explore','search']].map(([k,i])=>`<button class="${t===k?'act-t':''}" data-a="go" data-v="${k}" aria-label="${k}">${ic(i,28)}${k==='msgs'&&S.unread?'<span class="dot"></span>':''}</button>`).join('')+`<button class="${t==='profile'?'act-t':''}" data-a="go" data-v="profile" aria-label="Profile">${av(S.me.username,32)}${S.req?'<span class="dot"></span>':''}</button>`}
const V={chat,home,reels,explore,msgs,profile,settings,privacy,requests,saved,plist};
async function go(t,id){S.tab=t;const m=$('#main');m.className=t;if(!S.me){m.innerHTML=authView();nav();return}m.innerHTML='<div class="empty">Loading…</div>';nav();try{m.innerHTML=await V[t](id);m.scrollTop=t==='chat'?1e9:0;if(t==='reels')watchReels()}catch(e){console.error(e);m.innerHTML='<div class="empty">Something went wrong. Check your connection and try again.<br><small style="opacity:.7">'+esc(e&&e.message||'')+'</small></div>'}}
function toast(t){const e=$('#toast');e.textContent=t;e.classList.add('show');clearTimeout(toast.t);toast.t=setTimeout(()=>e.classList.remove('show'),2200)}
function ov(h){const d=document.createElement('div');d.className='ov sh';d.innerHTML=h;$('#app').appendChild(d);return d}
const close=()=>document.querySelectorAll('.ov').forEach(o=>o.remove());
const closeSh=()=>document.querySelectorAll('.sh').forEach(o=>o.remove());
function sheetHTML(m){const chips=[['post','Post'],['reel','Reel'],['story','Story']].map(([k,l])=>`<button class="chip ${m===k?'on':''}" data-a="newp" data-v="${k}">${l}</button>`).join('');const vid=m==='reel';
 return `<div class="pn" data-a="noop"><h3>New ${m}</h3><div class="chips">${chips}</div><label class="pre" id="pv" for="nf" ${vid?'style="height:260px"':''}>${vid?'Tap to choose a video':'Tap to choose a photo'}</label><input type="file" id="nf" accept="${vid?'video/*':'image/*'}" hidden>${m==='story'?'':'<input class="fld" id="pc" placeholder="Write a caption" maxlength="150">'}<button class="go" data-a="doNew">${m==='post'?'Share':m==='reel'?'Share reel':'Share to story'}</button></div>`}
function newSheet(m){S.np=m;const d=document.querySelector('.sh');if(d&&d.querySelector('#nf'))d.innerHTML=sheetHTML(m);else ov(sheetHTML(m))}
async function tog(t,k,table){const set=S[{likes:'L',reposts:'R',saves:'V'}[t]],on=!set.has(k),a={likes:'like',reposts:'repost',saves:'save'}[t];on?set.add(k):set.delete(k);
 document.querySelectorAll(`[data-a="${a}"][data-k="${k}"]`).forEach(e=>e.classList.toggle('on',on));document.querySelectorAll(`[data-c="${t}"][data-k="${k}"]`).forEach(e=>e.textContent=fmt(+e.dataset.b+(on?1:0))+e.dataset.s);
 const r=on?await sb.from(table).insert({post_id:k,user_id:S.me.id}):await sb.from(table).delete().match({post_id:k,user_id:S.me.id});if(r.error)toast('Could not update');return on}
async function sendList(q){const c=$('#sres');if(!c)return;let us=[];if(q){const r=await sb.from('profiles').select('id,username,full_name').ilike('username',q+'%').neq('id',S.me.id).limit(10);us=r.data||[]}else if(S.F.size){const r=await sb.from('profiles').select('id,username,full_name').in('id',[...S.F]).limit(30);us=r.data||[]}
 c.innerHTML=us.map(u=>`<button class="chat" data-a="sendTo" data-id="${u.id}">${av(u.username,44)}<div><b>${esc(u.username)}</b><small>${esc(u.full_name||'')}</small></div></button>`).join('')||`<div class="empty" style="padding:20px">${q?'No users found':'Follow people to send them posts, or search above'}</div>`}
async function tusUp(path,f,onp){const{data:{session}}=await sb.auth.getSession();if(!session)throw new Error('Not logged in');if(!window.tus)throw new Error('Uploader not loaded');
 return new Promise((res,rej)=>{const u=new tus.Upload(f,{endpoint:SB_URL.replace('.supabase.co','.storage.supabase.co')+'/storage/v1/upload/resumable',retryDelays:[0,3000,5000,10000,20000],headers:{authorization:'Bearer '+session.access_token,apikey:SB_KEY},uploadDataDuringCreation:true,removeFingerprintOnSuccess:true,metadata:{bucketName:'posts',objectName:path,contentType:f.type||'video/mp4',cacheControl:'3600'},chunkSize:6*1024*1024,onError:rej,onProgress:(a,b)=>onp&&onp(Math.round(a/b*100)),onSuccess:()=>res()});
  try{u.findPreviousUploads().then(p=>{if(p.length)u.resumeFromPreviousUpload(p[0]);u.start()}).catch(()=>u.start())}catch(e){u.start()}})}
const A={
 go:(v,t)=>{if(v==='profile')S.pt='posts';go(v,t.dataset.id)},chat:(_,t)=>go('chat',t.dataset.id),
 story:(_,t)=>showStory(t.dataset.id,0),nx:(_,t)=>showStory(t.dataset.u,+t.dataset.i),xs:()=>{clearTimeout(showStory.t);close()},
 post:()=>newSheet('post'),storyAdd:()=>newSheet('story'),newp:v=>newSheet(v),
 doNew:async(_,t)=>{const m=S.np,f=$('#nf').files[0];if(!f){toast(m==='reel'?'Choose a video first':'Choose a photo first');return}
  if(m==='reel'&&!f.type.startsWith('video/')){toast('Reels need a video file');return}
  if(m!=='reel'&&!f.type.startsWith('image/')){toast('Choose an image file');return}
  if(f.size>500*1048576){toast('File is over 500 MB');return}
  const lab=t.textContent,cap=$('#pc')?$('#pc').value:'';t.disabled=true;t.textContent='Uploading…';
  const ext=((f.name.split('.').pop()||'').toLowerCase().replace(/[^a-z0-9]/g,''))||(m==='reel'?'mp4':'jpg');
  const path=`${S.me.id}/${m==='story'?'s':m==='reel'?'r':''}${Date.now()}.${ext}`;
  try{if(m==='reel'){await tusUp(path,f,p=>{t.textContent='Uploading… '+p+'%'})}else{const up=await sb.storage.from('posts').upload(path,f,{contentType:f.type});if(up.error)throw up.error}}
  catch(e){console.error(e);const big=/size|exceed|413|too large/i.test(String(e&&(e.message||e)));toast(big?'File too large for your Supabase plan':'Upload failed - try again');t.disabled=false;t.textContent=lab;return}
  t.textContent='Saving…';
  const url=sb.storage.from('posts').getPublicUrl(path).data.publicUrl;
  const r=m==='story'?await sb.from('stories').insert({user_id:S.me.id,image_url:url}):await sb.from('posts').insert({user_id:S.me.id,image_url:url,caption:cap,kind:m,media_type:m==='reel'?'video':'image'});
  closeSh();if(r.error){toast('Could not share');return}toast(m==='story'?'Story shared':m==='reel'?'Reel shared':'Posted');go(m==='reel'?'reels':m==='story'?'home':(S.tab==='profile'?'profile':'home'))},
 dm:async(_,t)=>{const i=$('#mi'),b=i.value.trim();if(!b)return;const r=await sb.from('messages').insert({sender_id:S.me.id,receiver_id:t.dataset.id,body:b}).select('id,sender_id,body').single();if(r.error){toast('Could not send');return}i.value='';$('#ml').insertAdjacentHTML('beforeend',bub(r.data));$('#main').scrollTop=1e9},
 toast:v=>toast(v),mode:v=>{S.mode=v;go('home')},noop:()=>{},
 auth:async(_,t)=>{const e=$('#ae').value.trim(),p=$('#ap').value,m=$('#am');m.className='msg';m.textContent='';let r;
  const fe=x=>/database error saving new user/i.test(x)?'Could not create the account. This username is probably already taken - try a different one.':/already registered/i.test(x)?'This email is already registered. Please log in.':x;
  t.disabled=true;
  try{
  if(S.mode==='up'){const u=$('#au').value.trim().toLowerCase();if(!/^[a-z0-9._]{3,30}$/.test(u)){m.textContent='Username: 3-30 letters, numbers, . or _';return}
   if(!e){m.textContent='Enter your email';return}if(p.length<6){m.textContent='Password must be at least 6 characters';return}
   const ck=await sb.from('profiles').select('id',{count:'exact',head:true}).eq('username',u);if(!ck.error&&ck.count>0){m.textContent='Username already taken. Try another one.';return}
   r=await sb.auth.signUp({email:e,password:p,options:{data:{username:u}}});if(!r.error&&!r.data.session){m.className='msg ok';m.textContent='Check your email to confirm, then log in.';return}}
  else r=await sb.auth.signInWithPassword({email:e,password:p});
  if(r.error)m.textContent=fe(r.error.message)}finally{t.disabled=false}},
 logout:async()=>{await sb.auth.signOut()},
 like:(_,t)=>tog('likes',t.dataset.k,'likes'),repost:async(_,t)=>{const on=await tog('reposts',t.dataset.k,'reposts');toast(on?'Reposted':'Repost removed')},
 save:async(_,t)=>{const on=await tog('saves',t.dataset.k,'saves');toast(on?'Saved':'Removed from saved')},
 capx:(_,t)=>t.classList.toggle('x'),
 capm:(_,t)=>{const c=t.previousElementSibling;if(c)c.classList.add('x')},
 vt:(_,t)=>{if(t.paused)t.play().catch(()=>{});t.muted=!t.muted;toast(t.muted?'Sound off':'Sound on')},
 rt:v=>{S.rt=v;go('reels')},ptab:(v,t)=>{S.pt=v;go('profile',t.dataset.id)},plist:(v,t)=>{S.pl={id:t.dataset.id,type:v};go('plist')},
 follow:async(v,t)=>{const id=v,pv=t.dataset.pv==='1',had=S.F.has(id)||S.P.has(id);
  if(had&&S.F.has(id)&&pv&&!confirm('Unfollow this private account? You will need to send a new request.'))return;
  const r=had?await sb.from('follows').delete().match({follower_id:S.me.id,following_id:id}):await sb.from('follows').insert({follower_id:S.me.id,following_id:id,status:pv?'pending':'accepted'});
  if(r.error){toast('Could not update follow');await loadMine();return}
  if(had){S.F.delete(id);S.P.delete(id)}else(pv?S.P:S.F).add(id);
  document.querySelectorAll(`[data-a="follow"][data-v="${id}"]`).forEach(b=>{const on=!had;b.textContent=flab(id);b.classList.toggle('on',on);b.classList.toggle('pri',!on)});
  if(!had&&pv)toast('Follow request sent');if(t.dataset.r)go('profile',id)},
 acc:async(_,t)=>{const id=t.dataset.id;const r=await sb.from('follows').update({status:'accepted'}).match({follower_id:id,following_id:S.me.id});if(r.error){toast('Could not confirm');return}$('#rq'+id)?.remove();S.req=Math.max(0,S.req-1);nav();toast('Request confirmed')},
 rej:async(_,t)=>{const id=t.dataset.id;const r=await sb.from('follows').delete().match({follower_id:id,following_id:S.me.id});if(r.error){toast('Could not delete');return}$('#rq'+id)?.remove();S.req=Math.max(0,S.req-1);nav()},
 del:async(_,t)=>{if(!confirm('Delete this post?'))return;await sb.from('posts').delete().eq('id',t.dataset.k);close();go(S.tab)},
 openPost:async(_,t)=>{const r=await sb.from('posts').select(SEL).eq('id',t.dataset.k).maybeSingle();if(!r.data){toast('This post is not available');return}const[p]=await attach([r.data]);clearTimeout(showStory.t);close();const d=document.createElement('div');d.className='ov';d.style.background='#000';d.innerHTML=`<div class="rtop"><button class="ib" data-a="xs" aria-label="Close">${ic('back',28)}</button></div>`+reelHTML(p);$('#app').appendChild(d);d.querySelector('video')?.play().catch(()=>{})},
 sendp:async(_,t)=>{S.sp=t.dataset.k;ov(`<div class="pn" data-a="noop"><h3>Send to</h3><div class="pill">${ic('search',20)}<input id="sq" placeholder="Search people" aria-label="Search people" autocapitalize="none"></div><div class="cm" id="sres">Loading…</div></div>`);await sendList('')},
 sendTo:async(_,t)=>{const id=t.dataset.id,k=S.sp;const r=await sb.from('messages').insert({sender_id:S.me.id,receiver_id:id,body:'Shared a post',post_id:k});if(r.error){toast('Could not send');return}sb.from('shares').insert({post_id:k,user_id:S.me.id,receiver_id:id}).then(()=>{});
  document.querySelectorAll(`[data-c="shares"][data-k="${k}"]`).forEach(e=>{e.dataset.b=+e.dataset.b+1;e.textContent=fmt(+e.dataset.b)});closeSh();toast('Sent')},
 share:()=>{const q=qrcode(0,'M');q.addData(qrText(S.me.username));q.make();
  ov(`<div class="pn" data-a="noop"><h3>My QR code</h3><div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="background:#fff;padding:12px;border-radius:16px;width:230px;height:230px"><img alt="QR code" src="${q.createDataURL(8,0)}" style="width:100%;height:100%;image-rendering:pixelated;display:block"></div><b>@${esc(S.me.username)}</b><small style="color:var(--mt);text-align:center">Scan this to open my profile and follow me</small></div><button class="go" data-a="scan">Scan a QR code</button><button class="btn" data-a="copyLink">Copy profile link</button></div>`)},
 copyLink:()=>{try{navigator.clipboard.writeText(qrText(S.me.username))}catch(e){}toast('Profile link copied')},
 scan:()=>{closeSh();ov(`<div class="pn" data-a="noop"><h3>Scan QR code</h3><div style="border-radius:16px;overflow:hidden;background:#000;aspect-ratio:1"><video id="qv" playsinline muted style="width:100%;height:100%;object-fit:cover;display:block"></video></div><div class="msg" id="qm">Point the camera at a Social Hub QR code</div><label class="btn" for="qf" style="cursor:pointer">Choose a QR photo instead</label><input type="file" id="qf" accept="image/*" hidden></div>`);startScan()},
 edit:()=>ov(`<div class="pn" data-a="noop"><h3>Edit profile</h3><div style="display:flex;flex-direction:column;align-items:center;gap:8px"><label for="ea" id="ap" style="cursor:pointer">${av(S.me.username,84)}</label><label for="ea" style="color:var(--ac);font-weight:600;font-size:14px;cursor:pointer">Change profile photo</label><input type="file" id="ea" accept="image/*" hidden></div><input class="fld" id="en" value="${esc(S.me.full_name||'')}" placeholder="Name" maxlength="50"><input class="fld" id="eb" value="${esc(S.me.bio||'')}" placeholder="Bio" maxlength="120"><button class="go" data-a="saveP">Save changes</button></div>`),
 saveP:async(_,t)=>{const upd={full_name:$('#en').value,bio:$('#eb').value},f=$('#ea')&&$('#ea').files[0];
  if(f){if(!f.type.startsWith('image/')){toast('Choose an image file');return}
   if(t){t.disabled=true;t.textContent='Uploading…'}
   const ext=((f.name.split('.').pop()||'').toLowerCase().replace(/[^a-z0-9]/g,''))||'jpg';
   const path=`${S.me.id}/a${Date.now()}.${ext}`;
   const up=await sb.storage.from('posts').upload(path,f,{contentType:f.type});
   if(up.error){toast('Photo upload failed');if(t){t.disabled=false;t.textContent='Save changes'}return}
   upd.avatar_url=sb.storage.from('posts').getPublicUrl(path).data.publicUrl}
  const{error}=await sb.from('profiles').update(upd).eq('id',S.me.id);closeSh();
  if(error){toast('Could not save');return}
  Object.assign(S.me,upd);await loadAv();go('profile')},
 acct:async v=>{const pv=v==='private';if(pv===!!S.me.is_private)return;const{error}=await sb.from('profiles').update({is_private:pv}).eq('id',S.me.id);if(error){toast('Could not update account type');return}S.me.is_private=pv;if(!pv)S.req=0;toast(pv?'Account is now private':'Account is now public');go('privacy')},
 savePh:async()=>{const raw=$('#ph').value.replace(/[\s\-()]/g,'');if(raw&&!/^\+?[0-9]{7,15}$/.test(raw)){toast('Enter a valid mobile number');return}const{error}=await sb.from('user_private').upsert({id:S.me.id,phone:raw||null,updated_at:new Date().toISOString()});error?toast('Could not save number'):(toast(raw?'Mobile number saved':'Mobile number removed'),go('privacy'))},
 savePw:async(_,t)=>{const m=$('#pm'),c=$('#p0').value,n=$('#p1').value,n2=$('#p2').value;m.className='msg';m.textContent='';
  if(!c){m.textContent='Enter your current password';return}if(n.length<6){m.textContent='New password must be at least 6 characters';return}if(n!==n2){m.textContent='New passwords do not match';return}if(n===c){m.textContent='Choose a different password';return}
  t.disabled=true;S.quiet=true;try{const v=await sb.auth.signInWithPassword({email:S.me.email,password:c});if(v.error){m.textContent='Current password is incorrect';return}const u=await sb.auth.updateUser({password:n});if(u.error){m.textContent=u.error.message;return}m.className='msg ok';m.textContent='Password changed';['p0','p1','p2'].forEach(i=>$('#'+i).value='');toast('Password changed')}finally{S.quiet=false;t.disabled=false}},
 cm:async(_,t)=>{const k=t.dataset.k;ov(`<div class="pn" data-a="noop"><h3>Comments</h3><div class="cm" id="cl">Loading…</div><div class="cr"><input class="fld" id="ci" placeholder="Add a comment" maxlength="500" aria-label="Comment"><button class="go" data-a="csend" data-k="${k}">Post</button></div></div>`);await loadC(k)},
 csend:async(_,t)=>{const b=$('#ci').value.trim();if(!b)return;const k=t.dataset.k;const r=await sb.from('comments').insert({post_id:k,user_id:S.me.id,body:b});if(r.error){toast('Could not comment');return}$('#ci').value='';document.querySelectorAll(`[data-c="comments"][data-k="${k}"]`).forEach(e=>{e.dataset.b=+e.dataset.b+1;e.textContent=fmt(+e.dataset.b)});loadC(k)}
};
async function loadC(k){const{data}=await sb.from('comments').select('body,profiles!user_id(username)').eq('post_id',k).order('created_at');const c=$('#cl');if(c)c.innerHTML=(data||[]).map(x=>`<div><b>${esc(x.profiles?.username)}</b> ${esc(x.body)}</div>`).join('')||'<div class="empty" style="padding:20px">No comments yet</div>'}
document.addEventListener('click',e=>{if(e.target.classList.contains('sh')){e.target.remove();return}const t=e.target.closest('[data-a]');if(!t)return;A[t.dataset.a]&&A[t.dataset.a](t.dataset.v,t,e)});
document.addEventListener('change',e=>{if(e.target.id==='ea'){const f=e.target.files[0];if(f){const l=$('#ap');if(l)l.innerHTML=`<div class="av" style="width:84px;height:84px;background:#262b32 url('${URL.createObjectURL(f)}') center/cover"></div>`}return}if(e.target.id!=='nf')return;const f=e.target.files[0];if(!f)return;const p=$('#pv'),u=URL.createObjectURL(f);if(f.type.startsWith('video/')){p.style.backgroundImage='';p.innerHTML=`<video src="${u}" muted playsinline autoplay loop></video>`}else{p.innerHTML='';p.style.backgroundImage=`url(${u})`}});
document.addEventListener('dblclick',e=>{const m=e.target.closest('.media,.reel');if(m&&m.dataset.k&&!S.L.has(m.dataset.k))A.like(null,{dataset:{k:m.dataset.k}})});
document.addEventListener('keydown',e=>{if(e.key==='Enter'&&(e.target.id==='mi'||e.target.id==='ci'))e.target.nextElementSibling.click()});
let st;document.addEventListener('input',e=>{const sid=e.target.id;if(sid!=='q'&&sid!=='mq'&&sid!=='sq')return;clearTimeout(st);st=setTimeout(async()=>{const q=e.target.value.trim().toLowerCase().replace(/[%,]/g,'');if(sid==='sq'){sendList(q);return}const r=$(sid==='q'?'#res':'#mres');if(!q){r.innerHTML='';return}const{data}=await sb.from('profiles').select('id,username,full_name,is_private').ilike('username',q+'%').limit(10);r.innerHTML=(data||[]).map(u=>`<button class="chat" data-a="${sid==='q'?'go':'chat'}" ${sid==='q'?'data-v="profile" ':''}data-id="${u.id}">${av(u.username,48)}<div><b>${esc(u.username)}${u.is_private?' '+ic('lock',12):''}</b><small>${esc(u.full_name||'')}</small></div></button>`).join('')||'<div class="empty" style="padding:20px">No users found</div>'},300)});

const APPURL=(window.APP_URL&&!String(window.APP_URL).startsWith('__'))?String(window.APP_URL):'';
const qrText=u=>APPURL?`${APPURL}${APPURL.includes('?')?'&':'?'}u=${u}`:`socialhub:${u}`;
const parseQR=t=>{t=String(t||'');const m=t.match(/[?&]u=([a-z0-9._]{3,30})/i)||t.match(/^socialhub:([a-z0-9._]{3,30})$/i);return m?m[1].toLowerCase():null};
async function openUser(name){const r=await sb.from('profiles').select('id').eq('username',name).maybeSingle();if(!r.data){toast('User not found');return false}closeSh();go('profile',r.data.id);return true}
async function startScan(){const v=$('#qv'),m=$('#qm');if(!v)return;let stream;
 try{stream=await navigator.mediaDevices.getUserMedia({video:{facingMode:'environment'}})}catch(e){m.textContent='Camera not available. Use the photo option below.';return}
 v.srcObject=stream;try{await v.play()}catch(e){}
 const det=window.BarcodeDetector?new BarcodeDetector({formats:['qr_code']}):null,cv=document.createElement('canvas'),cx=cv.getContext('2d',{willReadFrequently:true});let busy=false;
 const stop=()=>stream.getTracks().forEach(t=>t.stop());
 const tick=async()=>{if(!document.body.contains(v)){stop();return}
  if(!busy&&v.videoWidth){busy=true;let txt=null;
   try{if(det){const r=await det.detect(v);txt=r[0]&&r[0].rawValue}else if(window.jsQR){cv.width=v.videoWidth;cv.height=v.videoHeight;cx.drawImage(v,0,0);const d=cx.getImageData(0,0,cv.width,cv.height);const c=jsQR(d.data,d.width,d.height);txt=c&&c.data}}catch(e){}
   busy=false;
   if(txt){const u=parseQR(txt);if(u){stop();await openUser(u);return}m.textContent='This is not a Social Hub QR code'}}
  setTimeout(tick,200)};
 tick()}
async function pendingOpen(){let u=window.OPEN_USER;if(!u||String(u).startsWith('__')){try{u=new URLSearchParams(location.search).get('u')}catch(e){u=null}}
 u=parseQR('?u='+(u||''));if(!u||!S.me)return;window.OPEN_USER='';if(u!==S.me.username)await openUser(u)}
document.addEventListener('change',e=>{if(e.target.id!=='qf')return;const f=e.target.files[0];if(!f)return;const img=new Image();
 img.onload=async()=>{const k=Math.min(1,1200/Math.max(img.naturalWidth,img.naturalHeight)),cv=document.createElement('canvas');cv.width=Math.round(img.naturalWidth*k);cv.height=Math.round(img.naturalHeight*k);const cx=cv.getContext('2d');cx.drawImage(img,0,0,cv.width,cv.height);let txt=null;
  try{if(window.BarcodeDetector){const r=await new BarcodeDetector({formats:['qr_code']}).detect(cv);txt=r[0]&&r[0].rawValue}
   if(!txt&&window.jsQR){const d=cx.getImageData(0,0,cv.width,cv.height);const c=jsQR(d.data,d.width,d.height);txt=c&&c.data}}catch(e){}
  const u=parseQR(txt);u?openUser(u):toast('No Social Hub QR code found')};
 img.src=URL.createObjectURL(f)});
async function boot(session){if(!session){S.me=null;S.unread=false;S.req=0;sb.removeAllChannels();go('home');return}const{data}=await sb.from('profiles').select('*').eq('id',session.user.id).single();S.me={...data,email:session.user.email};await loadAv();await loadMine();subscribe();refreshUnread();loadReq();await go(['settings','chat','plist','privacy','requests'].includes(S.tab)?'home':S.tab);pendingOpen()}
sb.auth.onAuthStateChange((ev,s)=>{if(S.quiet)return;if(ev==='INITIAL_SESSION'||ev==='SIGNED_IN'||ev==='SIGNED_OUT')setTimeout(()=>boot(s),0)});

</script></body></html>
'''

_u = st.query_params.get("u", "")
_u = _u.lower() if re.fullmatch(r"[A-Za-z0-9._]{3,30}", _u or "") else ""
components.html(
    HTML.replace("__APP_URL__", APP_URL).replace("__OPEN_USER__", _u),
    height=800,
    scrolling=False,
)
