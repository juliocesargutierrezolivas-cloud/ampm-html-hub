
const appGrid=document.getElementById('appGrid');
const search=document.getElementById('appSearch');
let APPS=[];
function escText(v){return String(v??'').replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]||c));}
function renderApps(){
  const q=(search.value||'').trim().toLowerCase();
  const rows=APPS.filter(a=>`${a.name} ${a.description} ${a.category}`.toLowerCase().includes(q));
  appGrid.innerHTML=rows.map(a=>`<a class="app-card card" href="${a.path}"><div class="app-icon">${a.icon}</div><div class="app-category">${escText(a.category)}</div><h3>${escText(a.name)}</h3><p>${escText(a.description)}</p><div class="app-footer"><span class="pill">${escText(a.status)}</span><span class="open">Abrir →</span></div></a>`).join('')||'<div class="empty card">No se encontraron herramientas.</div>';
}
async function init(){
  try{
    const res=await fetch('./config/apps.json?v='+Date.now(),{cache:'no-store'}); APPS=await res.json(); renderApps();
    const mr=await fetch('./data/gastos/manifest.json?v='+Date.now(),{cache:'no-store'}); const m=await mr.json();
    const latest=(m.periods||[]).find(p=>p.id===m.latest);
    document.getElementById('portalStatus').textContent=latest?latest.label:'Sin periodo';
    document.getElementById('portalMeta').textContent=`${(m.periods||[]).length} periodos publicados · actualización automática`;
  }catch(e){document.getElementById('portalStatus').textContent='Error de publicación';document.getElementById('portalMeta').textContent=e.message;}
}
search.addEventListener('input',renderApps); init();
