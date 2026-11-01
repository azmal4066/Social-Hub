import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Social Hub",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 480px;}
      iframe {border: 0; display: block;}
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
</style></head><body>
<div id="app"><div id="main"></div><nav id="nav"></nav><div id="toast"></div></div>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js"></script>
<script>
const I={plus:'<path d="M12 5v14M5 12h14"/>',heart:'<path d="M12 21s-7-4.6-9.3-9A5.3 5.3 0 0 1 12 6.5 5.3 5.3 0 0 1 21.3 12C19 16.4 12 21 12 21z"/>',home:'<path d="M3 11l9-8 9 8v10h-6v-6H9v6H3z"/>',reels:'<rect x="3" y="3" width="18" height="18" rx="5"/><path d="M10 8l6 4-6 4z"/>',send:'<path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/>',search:'<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/>',comment:'<path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6A8 8 0 1 1 21 12z"/>',mark:'<path d="M6 3h12v18l-6-4-6 4z"/>',repost:'<path d="M17 2l4 4-4 4M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4M21 13v2a3 3 0 0 1-3 3H3"/>',menu:'<path d="M3 7h18M3 12h18M3 17h18"/>',dots:'<path d="M4 9h16M4 15h10"/>',grid:'<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>',tag:'<rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="12" cy="10" r="3"/><path d="M6 19a6 6 0 0 1 12 0"/>',back:'<path d="M15 18l-6-6 6-6"/>',chev:'<path d="M9 6l6 6-6 6"/>',down:'<path d="M6 9l6 6 6-6"/>',clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',bell:'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8M10 21h4"/>',pulse:'<path d="M3 12h4l3-8 4 16 3-8h4"/>',user:'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',lock:'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',star:'<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.2 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>',block:'<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',help:'<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 17h.01"/>',out:'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>'};
const ic=(n,s=24)=>`<svg viewBox="0 0 24 24" width="${s}" height="${s}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">${I[n]}</svg>`;
const tick='<svg viewBox="0 0 24 24" width="15" height="15"><path fill="#3897f0" d="M12 1l2.4 2 3.1-.3 1 3 2.7 1.6-.8 3L21 13l-2 2.4.3 3.1-3 1-1.6 2.7-3-.8L9 23l-2.4-2-3.1.3-1-3L.8 16l.8-3L0 10.6l2-2.4-.3-3.1 3-1L6.4 1.4l3 .8z" transform="scale(.95) translate(.6 .6)"/><path d="M8 12.4l2.7 2.7L16 9.7" fill="none" stroke="#fff" stroke-width="2"/></svg>';
const SB_URL='https://vwxkbhrasiyafzbkaqvg.supabase.co',SB_KEY='sb_publishable_6soG-EJIOYUUHiSfVvxpVA_emGkRpCM';
const sb=supabase.createClient(SB_URL,SB_KEY);
const G=['#3a6073,#16222a','#e96443,#904e95','#134e5e,#71b280','#41295a,#2f0743','#f7971e,#a8431a','#0f2027,#2c5364','#614385,#516395','#c33764,#1d2671'];
const $=s=>document.querySelector(s);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=n=>n>=1e5?Math.round(n/1e3)+'K':n.toLocaleString('en-US');
const gi=u=>(u||'a').charCodeAt(0)%8;
const av=(n,s)=>`<div class="av" style="width:${s}px;height:${s}px;font-size:${s*.4}px;background:linear-gradient(135deg,${G[gi(n)]})">${esc((n||'?')[0].toUpperCase())}</div>`;
const S={tab:'home',unread:false,ST:{},me:null,L:new Set(),V:new Set(),F:new Set(),mode:'in'};
const hdr=(l,r)=>`<div class="top"><button class="ib" data-a="post" aria-label="New post">${ic('plus',30)}</button>${l}<div>${r}</div></div>`;
const cnt=(k,b,s='')=>`<span class="n" data-lc="${k}" data-b="${b}" data-s="${s}">${fmt(b+(S.L.has(k)?1:0))}${s}</span>`;
const lk=(p,sz=26,s='')=>`<button class="act ${S.L.has(p.id)?'on':''}" data-a="like" data-k="${p.id}" aria-label="Like">${ic('heart',sz)}</button>`;
const nLikes=p=>(p.likes?.[0]?.count||0)-(S.L.has(p.id)?1:0);
const nCom=p=>p.comments?.[0]?.count||0;
const SEL='id,image_url,caption,user_id,profiles(username),likes(count),comments(count)';
async function feed(uid){let q=sb.from('posts').select(SEL).order('created_at',{ascending:false}).limit(40);if(uid)q=q.eq('user_id',uid);const{data}=await q;return data||[]}
async function loadMine(){const u=S.me.id;const[l,v,f]=await Promise.all([sb.from('likes').select('post_id').eq('user_id',u),sb.from('saves').select('post_id').eq('user_id',u),sb.from('follows').select('following_id').eq('follower_id',u)]);S.L=new Set((l.data||[]).map(x=>x.post_id));S.V=new Set((v.data||[]).map(x=>x.post_id));S.F=new Set((f.data||[]).map(x=>x.following_id))}
function authView(){const up=S.mode==='up';return `<div class="auth"><h1>Social Hub</h1>${up?'<input class="fld" id="au" placeholder="Username (a-z, 0-9, . _)" autocapitalize="none" aria-label="Username">':''}<input class="fld" id="ae" type="email" placeholder="Email" aria-label="Email"><input class="fld" id="ap" type="password" placeholder="Password (min 6)" aria-label="Password"><div class="msg" id="am"></div><button class=\"go\" data-a=\"auth\">${up?'Sign up':'Log in'}</button><div class="sw">${up?'Already have an account? <b data-a="mode" data-v="in">Log in</b>':'New here? <b data-a="mode" data-v="up">Sign up</b>'}</div></div>`}
function postHTML(p){const u=p.profiles?.username||'user';return `<article><div class="ph">${av(u,36)}<div><b>${esc(u)}</b></div>${p.user_id===S.me.id?`<button class="ib" data-a="del" data-k="${p.id}" aria-label="Delete post">${ic('block',22)}</button>`:''}</div><div class="media" data-k="${p.id}"><img src="${esc(p.image_url)}" alt="" loading="lazy"></div><div class="acts">${lk(p)}<button class="act" data-a="cm" data-k="${p.id}" aria-label="Comments">${ic('comment',26)}</button><span class="sp"></span><button class="act sv ${S.V.has(p.id)?'on':''}" data-a="save" data-k="${p.id}" aria-label="Save">${ic('mark',26)}</button></div><div class="meta"><b>${cnt(p.id,nLikes(p),' likes')}</b>${p.caption?`<p><b>${esc(u)}</b> ${esc(p.caption)}</p>`:''}<p class="mt" data-a="cm" data-k="${p.id}">View all ${nCom(p)} comments</p></div></article>`}
async function home(){const[ps,pr]=await Promise.all([feed(),sb.from('profiles').select('id,username').neq('id',S.me.id).limit(12),loadStories()]);
 const mine=S.ST[S.me.id];
 let s=`<div class="stories"><div class="st"><div class="me" data-a="${mine?'story':'storyAdd'}" data-id="${S.me.id}">${mine?`<div class="ring"><div class="in">${av(S.me.username,64)}</div></div>`:av(S.me.username,70)}<div class="plus" data-a="storyAdd">${ic('plus',14)}</div></div><span>Your story</span></div>`;
 const us=(pr.data||[]).sort((a,b)=>(S.ST[b.id]?1:0)-(S.ST[a.id]?1:0));
 us.forEach(u=>{const h=S.ST[u.id];s+=`<div class="st" data-a="${h?'story':'go'}" data-v="profile" data-id="${u.id}">${h?`<div class="ring"><div class="in">${av(u.username,64)}</div></div>`:av(u.username,70)}<span>${esc(u.username)}</span></div>`});
 s+='</div>'+(ps.length?ps.map(postHTML).join(''):'<div class="empty">No posts yet. Tap + to share the first one.</div>');
 return hdr('<h1>Social Hub</h1>','<span style="width:30px;display:block"></span>')+s}
async function loadStories(){const{data}=await sb.from('stories').select('id,image_url,user_id,profiles(username)').gt('expires_at',new Date().toISOString()).order('created_at');S.ST={};(data||[]).forEach(x=>{(S.ST[x.user_id]??=[]).push(x)})}
function showStory(uid,i){close();clearTimeout(showStory.t);const L=S.ST[uid];if(!L||i>=L.length)return;const s=L[i];const d=document.createElement('div');d.className='ov';d.style.background='#000';d.innerHTML=`<img src="${esc(s.image_url)}" alt="" style="width:100%;height:100%;object-fit:contain" data-a="nx" data-u="${uid}" data-i="${i+1}"><div class="bar"><i></i></div><div class="svh">${av(s.profiles?.username,34)}${esc(s.profiles?.username)}</div><button class="ib" data-a="xs" aria-label="Close" style="position:absolute;top:22px;right:12px;font-size:22px">✕</button>`;$('#app').appendChild(d);showStory.t=setTimeout(()=>showStory(uid,i+1),5000)}
async function reels(){const ps=await feed();return `<div class="rtop"><button class="ib" data-a="post">${ic('plus',30)}</button><span>Reels ${ic('down',16)}</span></div><div id="reels">`+(ps.length?ps.map(p=>{const u=p.profiles?.username||'user';return `<section class="reel" style="background:#000"><img src="${esc(p.image_url)}" alt=""><div class="side">${lk(p,32)}<button class="act" data-a="cm" data-k="${p.id}">${ic('comment',32)}<span class="n">${nCom(p)}</span></button><button class="act sv ${S.V.has(p.id)?'on':''}" data-a="save" data-k="${p.id}">${ic('mark',32)}</button></div><div class="rb"><div class="row">${av(u,38)}${esc(u)}${p.user_id!==S.me.id?`<button class="fb ${S.F.has(p.user_id)?'on':''}" data-a="follow" data-v="${p.user_id}">${S.F.has(p.user_id)?'Following':'Follow'}</button>`:''}</div><div>${esc(p.caption)}</div></div></section>`}).join(''):'<div class="empty">No reels yet</div>')+'</div>'}
async function explore(){const ps=await feed();return `<div class="search"><div class="pill">${ic('search',22)}<input id="q" placeholder="Search people" aria-label="Search people" autocapitalize="none"></div></div><div id="res"></div><div class="grid">`+ps.map(p=>`<div class="tile" data-a="cm" data-k="${p.id}"><img src="${esc(p.image_url)}" alt="" loading="lazy"></div>`).join('')+'</div>'+(ps.length?'':'<div class="empty">Nothing to explore yet</div>')}
async function msgs(){const me=S.me.id;const{data}=await sb.from('messages').select('sender_id,receiver_id,body,read_at').or(`sender_id.eq.${me},receiver_id.eq.${me}`).order('created_at',{ascending:false}).limit(200);const last={};(data||[]).forEach(m=>{const o=m.sender_id===me?m.receiver_id:m.sender_id;if(!last[o])last[o]=m});const ids=Object.keys(last),nm={};if(ids.length){const r=await sb.from('profiles').select('id,username').in('id',ids);(r.data||[]).forEach(u=>nm[u.id]=u.username)}
 return `<div class="top"><h2>${esc(S.me.username)}</h2></div><div class="search" style="padding-top:0"><div class="pill">${ic('search',20)}<input id="mq" placeholder="Find someone to message" aria-label="Find someone" autocapitalize="none"></div></div><div id="mres"></div>`+(ids.map(o=>{const m=last[o],un=m.receiver_id===me&&!m.read_at;return `<button class="chat" data-a="chat" data-id="${o}">${av(nm[o],52)}<div><b>${esc(nm[o])}</b><small>${m.sender_id===me?'You: ':''}${esc(m.body)}</small></div>${un?'<span class="u"></span>':''}</button>`}).join('')||'<div class="empty">No messages yet. Search for someone above.</div>')}
async function chat(id){const me=S.me.id;S.chat=id;const[p,m]=await Promise.all([sb.from('profiles').select('id,username').eq('id',id).single(),sb.from('messages').select('id,sender_id,body').or(`and(sender_id.eq.${me},receiver_id.eq.${id}),and(sender_id.eq.${id},receiver_id.eq.${me})`).order('created_at').limit(200)]);const u=p.data?.username||'user';
 sb.from('messages').update({read_at:new Date().toISOString()}).eq('receiver_id',me).eq('sender_id',id).is('read_at',null).then(refreshUnread);
 return `<div class="top" style="justify-content:flex-start;gap:12px"><button class="ib" data-a="go" data-v="msgs" aria-label="Back">${ic('back',28)}</button>${av(u,36)}<h2>${esc(u)}</h2></div><div class="msgs" id="ml">${(m.data||[]).map(bub).join('')}</div><div class="cb"><input class="fld" id="mi" placeholder="Message…" maxlength="1000" aria-label="Message"><button class="go" data-a="dm" data-id="${id}">Send</button></div>`}
const bub=m=>`<div class="bub ${m.sender_id===S.me.id?'me':''}">${esc(m.body)}</div>`;
async function refreshUnread(){const{count}=await sb.from('messages').select('*',{count:'exact',head:true}).eq('receiver_id',S.me.id).is('read_at',null);S.unread=count>0;nav()}
function subscribe(){sb.removeAllChannels();sb.channel('dm').on('postgres_changes',{event:'INSERT',schema:'public',table:'messages',filter:`receiver_id=eq.${S.me.id}`},p=>{const m=p.new;if(S.tab==='chat'&&S.chat===m.sender_id){$('#ml').insertAdjacentHTML('beforeend',bub(m));$('#main').scrollTop=1e9;sb.from('messages').update({read_at:new Date().toISOString()}).eq('id',m.id)}else{S.unread=true;nav();toast('New message')}}).subscribe()}
async function profile(id){id=id||S.me.id;const own=id===S.me.id;const[pr,fr,fg,ps]=await Promise.all([sb.from('profiles').select('*').eq('id',id).single(),sb.from('follows').select('*',{count:'exact',head:true}).eq('following_id',id),sb.from('follows').select('*',{count:'exact',head:true}).eq('follower_id',id),feed(id)]);
 const u=pr.data;if(!u)return '<div class="empty">Profile not found</div>';if(own)S.me={...S.me,...u};
 return `<div class="top"><button class="ib" data-a="${own?'post':'go'}" data-v="home">${ic(own?'plus':'back',30)}</button><h2>${esc(u.username)}</h2>${own?`<button class="ib" data-a="go" data-v="settings" aria-label="Settings">${ic('menu',30)}</button>`:'<span style="width:30px"></span>'}</div>
 <div class="phead">${av(u.username,86)}<div class="stats"><div><b>${ps.length}</b>posts</div><div><b>${fr.count||0}</b>followers</div><div><b>${fg.count||0}</b>following</div></div></div>
 <div style="padding:6px 16px"><b>${esc(u.full_name||'')}</b><div style="color:var(--mt)">${esc(u.bio||'')}</div></div>
 <div class="btns">${own?`<button class="btn" data-a="edit">Edit profile</button><button class="btn" data-a="share">Share profile</button>`:`<button class=\"btn\" data-a=\"follow\" data-v=\"${id}\" data-r=\"1\">${S.F.has(id)?'Following':'Follow'}</button><button class=\"btn\" data-a=\"chat\" data-id=\"${id}\">Message</button>`}</div>
 <div class="tabs"><button class="on" aria-label="Posts">${ic('grid',26)}</button></div>`+(ps.length?'<div class="grid">'+ps.map(p=>`<div class="tile" data-a="cm" data-k="${p.id}"><img src="${esc(p.image_url)}" alt="" loading="lazy"></div>`).join('')+'</div>':'<div class="empty">No posts yet</div>')}
async function settings(){const r=(i,t,a='toast')=>`<button class="row2" data-a="${a}" data-v="${t} is coming soon">${ic(i,28)}<div><b>${t}</b></div>${ic('chev',22)}</button>`;
 return `<div class="top" style="justify-content:flex-start;gap:20px"><button class="ib" data-a="go" data-v="profile" aria-label="Back">${ic('back',30)}</button><h2>Settings and activity</h2></div><div class="sec">Your account</div>${r('user','Accounts Center')}<div class="sep"></div><div class="sec">How you use Social Hub</div>${r('mark','Saved')}${r('clock','Archive')}${r('pulse','Your activity')}${r('bell','Notifications')}<div class="sep"></div><div class="sec">Who can see your content</div>${r('lock','Account privacy')}${r('star','Close Friends')}${r('block','Blocked')}<div class="sep"></div><button class="row2" data-a="logout">${ic('out',28)}<div><b>Log out</b><small>${esc(S.me.email||'')}</small></div></button><div style="height:30px"></div>`}
function nav(){if(!S.me){$('#nav').innerHTML='';return}const t=S.tab==='settings'?'profile':S.tab==='chat'?'msgs':S.tab;$('#nav').innerHTML=[['home','home'],['reels','reels'],['msgs','send'],['explore','search']].map(([k,i])=>`<button class="${t===k?'act-t':''}" data-a="go" data-v="${k}" aria-label="${k}">${ic(i,28)}${k==='msgs'&&S.unread?'<span class=\"dot\"></span>':''}</button>`).join('')+`<button class="${t==='profile'?'act-t':''}" data-a="go" data-v="profile" aria-label="Profile">${av(S.me.username,32)}</button>`}
const V={chat,home,reels,explore,msgs,profile,settings};
async function go(t,id){S.tab=t;const m=$('#main');m.className=t;if(!S.me){m.innerHTML=authView();nav();return}m.innerHTML='<div class="empty">Loading…</div>';nav();try{m.innerHTML=await V[t](id);m.scrollTop=t==='chat'?1e9:0}catch(e){m.innerHTML='<div class="empty">Something went wrong. Check your connection and try again.</div>'}}
function toast(t){const e=$('#toast');e.textContent=t;e.classList.add('show');clearTimeout(toast.t);toast.t=setTimeout(()=>e.classList.remove('show'),2200)}
function ov(h){const d=document.createElement('div');d.className='ov sh';d.innerHTML=h;$('#app').appendChild(d);return d}
const close=()=>document.querySelectorAll('.ov').forEach(o=>o.remove());
const A={
 go:(v,t)=>go(v,t.dataset.id),chat:(_,t)=>go('chat',t.dataset.id),google:()=>sb.auth.signInWithOAuth({provider:'google',options:{redirectTo:location.origin+location.pathname}}),
 story:(_,t)=>showStory(t.dataset.id,0),nx:(_,t)=>showStory(t.dataset.u,+t.dataset.i),xs:()=>{clearTimeout(showStory.t);close()},
 storyAdd:()=>ov(`<div class="pn" data-a="noop"><h3>New story</h3><label class="pre" id="pv" for="sf">Tap to choose a photo</label><input type="file" id="sf" accept="image/*" hidden><button class="go" data-a="doStory">Share to story</button></div>`),
 doStory:async(_,t)=>{const f=$('#sf').files[0];if(!f){toast('Choose a photo first');return}t.disabled=true;t.textContent='Sharing…';const path=`${S.me.id}/s${Date.now()}.${(f.name.split('.').pop()||'jpg').toLowerCase()}`;const up=await sb.storage.from('posts').upload(path,f,{contentType:f.type});if(up.error){toast('Upload failed');t.disabled=false;t.textContent='Share to story';return}const r=await sb.from('stories').insert({user_id:S.me.id,image_url:sb.storage.from('posts').getPublicUrl(path).data.publicUrl});close();r.error?toast('Could not share story'):(toast('Story shared'),go('home'))},
 dm:async(_,t)=>{const i=$('#mi'),b=i.value.trim();if(!b)return;const r=await sb.from('messages').insert({sender_id:S.me.id,receiver_id:t.dataset.id,body:b}).select('id,sender_id,body').single();if(r.error){toast('Could not send');return}i.value='';$('#ml').insertAdjacentHTML('beforeend',bub(r.data));$('#main').scrollTop=1e9},
toast:v=>toast(v),mode:v=>{S.mode=v;go('home')},noop:()=>{},
 auth:async()=>{const e=$('#ae').value.trim(),p=$('#ap').value,m=$('#am');m.className='msg';m.textContent='';let r;
  if(S.mode==='up'){const u=$('#au').value.trim().toLowerCase();if(!/^[a-z0-9._]{3,30}$/.test(u)){m.textContent='Username: 3-30 letters, numbers, . or _';return}r=await sb.auth.signUp({email:e,password:p,options:{data:{username:u}}});if(!r.error&&!r.data.session){m.className='msg ok';m.textContent='Check your email to confirm, then log in.';return}}
  else r=await sb.auth.signInWithPassword({email:e,password:p});
  if(r.error)m.textContent=r.error.message},
 logout:async()=>{await sb.auth.signOut()},
 like:async(_,t)=>{const k=t.dataset.k,on=!S.L.has(k);on?S.L.add(k):S.L.delete(k);document.querySelectorAll(`[data-a="like"][data-k="${k}"]`).forEach(e=>e.classList.toggle('on',on));document.querySelectorAll(`[data-lc="${k}"]`).forEach(e=>e.textContent=fmt(+e.dataset.b+(on?1:0))+e.dataset.s);
  const r=on?await sb.from('likes').insert({post_id:k,user_id:S.me.id}):await sb.from('likes').delete().match({post_id:k,user_id:S.me.id});if(r.error)toast('Could not update like')},
 save:async(_,t)=>{const k=t.dataset.k,on=!S.V.has(k);on?S.V.add(k):S.V.delete(k);document.querySelectorAll(`[data-a="save"][data-k="${k}"]`).forEach(e=>e.classList.toggle('on',on));toast(on?'Saved':'Removed from saved');on?await sb.from('saves').insert({post_id:k,user_id:S.me.id}):await sb.from('saves').delete().match({post_id:k,user_id:S.me.id})},
 follow:async(v,t)=>{const on=!S.F.has(v);on?S.F.add(v):S.F.delete(v);t.classList.toggle('on',on);t.textContent=on?'Following':'Follow';on?await sb.from('follows').insert({follower_id:S.me.id,following_id:v}):await sb.from('follows').delete().match({follower_id:S.me.id,following_id:v});if(t.dataset.r)go('profile',v)},
 del:async(_,t)=>{if(!confirm('Delete this post?'))return;await sb.from('posts').delete().eq('id',t.dataset.k);go(S.tab)},
 share:()=>{try{navigator.clipboard.writeText(location.href+'#'+S.me.username)}catch(e){}toast('Profile link copied')},
 edit:()=>ov(`<div class="pn" data-a="noop"><h3>Edit profile</h3><input class="fld" id="en" value="${esc(S.me.full_name||'')}" placeholder="Name" maxlength="50"><input class="fld" id="eb" value="${esc(S.me.bio||'')}" placeholder="Bio" maxlength="120"><button class="go" data-a="saveP">Save changes</button></div>`),
 saveP:async()=>{const{error}=await sb.from('profiles').update({full_name:$('#en').value,bio:$('#eb').value}).eq('id',S.me.id);close();error?toast('Could not save'):go('profile')},
 post:()=>ov(`<div class="pn" data-a="noop"><h3>New post</h3><label class="pre" id="pv" for="pf">Tap to choose a photo</label><input type="file" id="pf" accept="image/*" hidden><input class="fld" id="pc" placeholder="Write a caption" maxlength="150"><button class="go" data-a="doPost">Share</button></div>`),
 doPost:async(_,t)=>{const f=$('#pf').files[0];if(!f){toast('Choose a photo first');return}t.disabled=true;t.textContent='Posting…';const path=`${S.me.id}/${Date.now()}.${(f.name.split('.').pop()||'jpg').toLowerCase()}`;
  const up=await sb.storage.from('posts').upload(path,f,{contentType:f.type});if(up.error){toast('Upload failed');t.disabled=false;t.textContent='Share';return}
  const url=sb.storage.from('posts').getPublicUrl(path).data.publicUrl;const r=await sb.from('posts').insert({user_id:S.me.id,image_url:url,caption:$('#pc').value});close();if(r.error)toast('Could not post');else{toast('Posted');go(S.tab==='profile'?'profile':'home')}},
 cm:async(_,t)=>{const k=t.dataset.k;const d=ov(`<div class="pn" data-a="noop"><h3>Comments</h3><div class="cm" id="cl">Loading…</div><div class="cr"><input class="fld" id="ci" placeholder="Add a comment" maxlength="500" aria-label="Comment"><button class="go" data-a="send" data-k="${k}">Post</button></div></div>`);await loadC(k)},
 send:async(_,t)=>{const b=$('#ci').value.trim();if(!b)return;const r=await sb.from('comments').insert({post_id:t.dataset.k,user_id:S.me.id,body:b});if(r.error){toast('Could not comment');return}$('#ci').value='';loadC(t.dataset.k)}
};
async function loadC(k){const{data}=await sb.from('comments').select('body,profiles(username)').eq('post_id',k).order('created_at');const c=$('#cl');if(c)c.innerHTML=(data||[]).map(x=>`<div><b>${esc(x.profiles?.username)}</b> ${esc(x.body)}</div>`).join('')||'<div class="empty" style="padding:20px">No comments yet</div>'}
document.addEventListener('click',e=>{if(e.target.classList.contains('sh')){close();return}const t=e.target.closest('[data-a]');if(!t)return;A[t.dataset.a]&&A[t.dataset.a](t.dataset.v,t,e)});
document.addEventListener('change',e=>{if(e.target.id==='pf'||e.target.id==='sf'){const f=e.target.files[0];if(f){const p=$('#pv');p.style.backgroundImage=`url(${URL.createObjectURL(f)})`;p.textContent=''}}});
document.addEventListener('dblclick',e=>{const m=e.target.closest('.media');if(m&&!S.L.has(m.dataset.k))A.like(null,{dataset:{k:m.dataset.k}})});
document.addEventListener('keydown',e=>{if(e.key==='Enter'&&(e.target.id==='mi'||e.target.id==='ci'))e.target.nextElementSibling.click()});
let st;document.addEventListener('input',e=>{const sid=e.target.id;if(sid!=='q'&&sid!=='mq')return;clearTimeout(st);st=setTimeout(async()=>{const q=e.target.value.trim().toLowerCase().replace(/[%,]/g,'');const r=$(sid==='q'?'#res':'#mres');if(!q){r.innerHTML='';return}const{data}=await sb.from('profiles').select('id,username,full_name').ilike('username',q+'%').limit(10);r.innerHTML=(data||[]).map(u=>`<button class="chat" data-a=\"${sid==='q'?'go':'chat'}\" ${sid==='q'?'data-v=\"profile\" ':''}data-id=\"${u.id}\">${av(u.username,48)}<div><b>${esc(u.username)}</b><small>${esc(u.full_name||'')}</small></div></button>`).join('')||'<div class="empty" style="padding:20px">No users found</div>'},300)});
async function boot(session){if(!session){S.me=null;S.unread=false;sb.removeAllChannels();go('home');return}const{data}=await sb.from('profiles').select('*').eq('id',session.user.id).single();S.me={...data,email:session.user.email};await loadMine();subscribe();refreshUnread();go(S.tab==='settings'?'home':S.tab)}
sb.auth.onAuthStateChange((ev,s)=>{if(ev==='INITIAL_SESSION'||ev==='SIGNED_IN'||ev==='SIGNED_OUT')setTimeout(()=>boot(s),0)});

</script></body></html>'''

components.html(HTML, height=860, scrolling=False)
