// Test de fumée : chaque jeu se charge sans erreur JavaScript, a un titre et des commandes.
const {JSDOM,VirtualConsole}=require('jsdom');const fs=require('fs');
const files=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));const out=[];
(async()=>{for(const [nom,f] of files){const errs=[];const vc=new VirtualConsole();vc.on('jsdomError',e=>errs.push(((e.detail&&e.detail.message)||e.message).slice(0,100)));
  let titre='',boutons=0,ko=0;try{const d=new JSDOM(fs.readFileSync(f,'utf8'),{runScripts:'dangerously',virtualConsole:vc,pretendToBeVisual:true,beforeParse(w){try{Object.defineProperty(w,'crypto',{value:require('crypto').webcrypto});}catch(e){}w.HTMLCanvasElement.prototype.getContext=()=>null;w.URL.createObjectURL=()=>'blob:x';}});
   await new Promise(r=>setTimeout(r,900));const doc=d.window.document;titre=(doc.querySelector('h1')||doc.querySelector('title')||{}).textContent||'';boutons=doc.querySelectorAll('button,.btn,[onclick]').length;ko=Math.round(fs.statSync(f).size/1024);d.window.close();}catch(e){errs.push(e.message.slice(0,100));}
  out.push({nom,fichier:require('path').basename(f),titre:titre.trim().slice(0,60),commandes:boutons,ko,erreurs:errs.filter(e=>!/canvas|WebGL|not implemented/i.test(e))});}
 fs.writeFileSync(process.argv[3],JSON.stringify(out,null,1));console.log(out.map(o=>`${o.erreurs.length?'✗':'✓'} ${o.nom} · ${o.commandes} commandes · ${o.ko} Ko`).join('\n'));})();
