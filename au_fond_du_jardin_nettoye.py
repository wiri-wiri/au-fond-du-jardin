#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Au Fond du Jardin — générateur du tableau de bord local
Auteur      : Bruno Romero
Pseudonyme  : Curl est ton ami
Licence     : GNU General Public License v3.0 (GNU GPLv3)

Ce fichier génère index.html à partir du modèle embarqué.
Le modèle HTML doit rester cohérent avec le README, cahier des charges du projet.
"""

from pathlib import Path
from copernicus import obtenir_humidite_sol
import webbrowser

FICHIER_SORTIE = Path("index.html")

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Au Fond du Jardin</title>
<style>
:root{--primary:#1b5e20;--bg:#f4f6f8;--card:#fff}
*{box-sizing:border-box}
body{font-family:system-ui,-apple-system,sans-serif;background:var(--bg);color:#2c3e50;margin:0;padding:15px}
.container{max-width:950px;margin:auto}
.card{background:var(--card);padding:20px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,.06);margin-bottom:20px}
.header{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:2px solid #edf2f7;padding-bottom:12px;margin-bottom:12px}
h1{margin:0;font-size:1.5rem;color:var(--primary)}
h2{font-size:1.1rem;margin-top:0;color:var(--primary)}
.btn{background:var(--primary);color:#fff;border:0;padding:9px 14px;border-radius:8px;cursor:pointer;font-weight:600}
.site-meta{font-size:.9rem;color:#64748b;margin:4px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:15px 0}
.metric{background:#f8fafc;padding:14px;border-radius:8px;border-left:4px solid var(--primary)}
.metric-title{font-size:.75rem;color:#64748b;text-transform:uppercase;font-weight:700}
.metric-value{font-size:1.3rem;font-weight:700;margin-top:4px;color:#0f172a}
.vigilance{margin-top:15px;background:#f8fafc;padding:12px;border-radius:8px}
.vigilance-note{font-size:.75rem;color:#64748b;margin-top:6px}
.badge{display:inline-block;padding:4px 10px;border-radius:12px;font-weight:700;color:#fff;font-size:.8rem}
.tag{display:inline-block;background:#f1f5f9;padding:2px 6px;border-radius:4px;font-size:.75rem;margin:2px 4px 2px 0}
.table-wrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:.9rem;min-width:680px}
th,td{padding:10px 12px;text-align:left;border-bottom:1px solid #e2e8f0}
th{background:#f8fafc;color:#475569;font-weight:600}
.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);justify-content:center;align-items:center;z-index:1000}
.modal-content{background:#fff;padding:25px;border-radius:12px;max-width:460px;width:90%}
.form-group{margin-bottom:12px}
.form-group label{display:block;font-size:.85rem;font-weight:600;margin-bottom:4px}
.form-group input{width:100%;padding:9px;border:1px solid #cbd5e1;border-radius:6px}
.actions{display:flex;gap:8px;margin-top:16px}
.actions .btn{flex:1}
.btn-secondary{background:#64748b}
.footer{text-align:center;font-size:.8rem;color:#94a3b8;margin-top:20px}
@media(max-width:600px){body{padding:8px}.card{padding:15px}.metric-value{font-size:1.2rem}}
</style>
</head>
<body>
<div class="container">
  <div class="card">
    <div class="header">
      <h1 id="site-title">🌿 Au Fond du Jardin</h1>
      <button class="btn" onclick="toggleModal(true)">⚙️ Mon terrain</button>
    </div>

    <p class="site-meta"><strong>Altitude :</strong> <span id="altitude-display">Analyse…</span></p>

    <div class="grid">
      <div class="metric">
        <div class="metric-title">Température actuelle</div>
        <div class="metric-value" id="t-actuelle">-- °C</div>
      </div>
      <div class="metric">
        <div class="metric-title">Pluie 7j / 30j</div>
        <div class="metric-value" id="pluie-cumul">-- / -- mm</div>
      </div>
      <div class="metric">
        <div class="metric-title">Cumul chaleur · GDD 10°C</div>
        <div class="metric-value" id="gdd-cumul">-- °C.j</div>
      </div>
      <div class="metric">
        <div class="metric-title">Qualité air · IQA / Ozone</div>
        <div class="metric-value" id="air-quality">-- / --</div>
      </div>
      <div class="metric">
        <div class="metric-title">Humidité moyenne du sol</div>
        <div class="metric-value" id="soil-moisture">-- %</div>
        <div class="site-meta" id="soil-moisture-meta">ERA5-Land · couche 0–7 cm</div>
      </div>
    </div>

    <div class="vigilance">
      <strong>Vigilance :</strong>
      <span class="badge" id="vigilance-badge" style="background:#64748b">…</span>
      <span id="vigilance-motifs" style="font-size:.85rem;margin-left:8px;color:#475569">Analyse…</span>
      <div class="vigilance-note">Indicateur expérimental — seuils non validés comme référence agronomique.</div>
    </div>
  </div>

  <div class="card">
    <h2>Synthèse mensuelle & degrés-jours</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Mois</th><th>T° min moy.</th><th>T° max moy.</th><th>GDD</th><th>Vigilance</th><th>Cumuls</th></tr>
        </thead>
        <tbody id="tableau-mensuel"><tr><td colspan="6">Chargement…</td></tr></tbody>
      </table>
    </div>
  </div>

  <div class="footer">Bruno Romero · <em>Curl est ton ami</em> · GNU GPLv3</div>
</div>

<div class="modal" id="settings-modal">
  <div class="modal-content">
    <h2>⚙️ Mon terrain</h2>
    <div class="form-group"><label for="cfg-site">Nom du site</label><input id="cfg-site" type="text"></div>
    <div class="form-group"><label for="cfg-lat">Latitude</label><input id="cfg-lat" type="number" step="0.000001"></div>
    <div class="form-group"><label for="cfg-lon">Longitude</label><input id="cfg-lon" type="number" step="0.000001"></div>
    <div class="actions">
      <button class="btn btn-secondary" onclick="toggleModal(false)">Annuler</button>
      <button class="btn" onclick="sauvegarderConfig()">Enregistrer</button>
    </div>
  </div>
</div>

<script>
const defaultConfig={site:"Mon Jardin",latitude:45.8336,longitude:1.2611};
const couleursCSS={VERT:"#2e7d32",JAUNE:"#f57f17",ORANGE:"#e65100",ROUGE:"#c62828",INDISPONIBLE:"#64748b"};

function getConfig(){
  try{
    const saved=JSON.parse(localStorage.getItem("jardin_config"));
    if(saved && Number.isFinite(Number(saved.latitude)) && Number.isFinite(Number(saved.longitude))){
      return {site:saved.site||defaultConfig.site,latitude:Number(saved.latitude),longitude:Number(saved.longitude)};
    }
  }catch(e){}
  return {...defaultConfig};
}
function toggleModal(show){document.getElementById("settings-modal").style.display=show?"flex":"none"}
function sauvegarderConfig(){
  const site=document.getElementById("cfg-site").value.trim()||"Mon Jardin";
  const latitude=parseFloat(document.getElementById("cfg-lat").value);
  const longitude=parseFloat(document.getElementById("cfg-lon").value);
  if(!Number.isFinite(latitude)||latitude<-90||latitude>90||!Number.isFinite(longitude)||longitude<-180||longitude>180){
    alert("Coordonnées GPS invalides."); return;
  }
  localStorage.setItem("jardin_config",JSON.stringify({site,latitude,longitude}));
  toggleModal(false); chargerDonnees();
}
function evaluerNiveau(tMin,tMax,iqa,ozone){
  let niveau="VERT",motifs=[];
  const rank={VERT:0,JAUNE:1,ORANGE:2,ROUGE:3};
  const monter=n=>{if(rank[n]>rank[niveau])niveau=n};
  if(tMin!=null){
    if(tMin<=0){monter("ROUGE");motifs.push(`Gel (${tMin.toFixed(1)} °C)`)}
    else if(tMin<=3){monter("JAUNE");motifs.push(`Température basse (${tMin.toFixed(1)} °C)`)}
  }
  if(tMax!=null){
    if(tMax>=35){monter("ROUGE");motifs.push(`Très forte chaleur (${tMax.toFixed(1)} °C)`)}
    else if(tMax>=33){monter("ORANGE");motifs.push(`Forte chaleur (${tMax.toFixed(1)} °C)`)}
    else if(tMax>=30){monter("JAUNE");motifs.push(`Chaleur (${tMax.toFixed(1)} °C)`)}
  }
  if(iqa!=null){
    if(iqa>=4){monter("ORANGE");motifs.push(`IQA ${Math.round(iqa)}`)}
    else if(iqa>=3){monter("JAUNE");motifs.push(`IQA ${Math.round(iqa)}`)}
  }
  if(ozone!=null && ozone>=120){monter("ORANGE");motifs.push(`Ozone ${Math.round(ozone)} µg/m³`)}
  return {niveau,motifs};
}
async function jsonFetch(url){
  const r=await fetch(url);
  if(!r.ok)throw new Error(`HTTP ${r.status}`);
  return r.json();
}
async function chargerDonnees(){
  const cfg=getConfig();
  document.getElementById("site-title").innerText="🌿 "+cfg.site;
  document.getElementById("cfg-site").value=cfg.site;
  document.getElementById("cfg-lat").value=cfg.latitude;
  document.getElementById("cfg-lon").value=cfg.longitude;

  let iqaVal=null,ozoneVal=null,tMinJour=null,tMaxJour=null;

  try{
    const d=await jsonFetch(`https://api.open-meteo.com/v1/elevation?latitude=${cfg.latitude}&longitude=${cfg.longitude}`);
    document.getElementById("altitude-display").innerText=d.elevation?.[0]!=null?`${Math.round(d.elevation[0])} m`:"Indisponible";
  }catch(e){document.getElementById("altitude-display").innerText="Indisponible"}

  try{
    const d=await jsonFetch(`https://api.open-meteo.com/v1/forecast?latitude=${cfg.latitude}&longitude=${cfg.longitude}&current=temperature_2m&daily=temperature_2m_min,temperature_2m_max&timezone=auto&forecast_days=1`);
    if(d.current?.temperature_2m!=null)document.getElementById("t-actuelle").innerText=d.current.temperature_2m.toFixed(1)+" °C";
    tMinJour=d.daily?.temperature_2m_min?.[0]??null;
    tMaxJour=d.daily?.temperature_2m_max?.[0]??null;
  }catch(e){document.getElementById("t-actuelle").innerText="Indisponible"}

  try{
    const d=await jsonFetch(`https://air-quality-api.open-meteo.com/v1/air-quality?latitude=${cfg.latitude}&longitude=${cfg.longitude}&current=european_aqi,ozone`);
    iqaVal=d.current?.european_aqi??null; ozoneVal=d.current?.ozone??null;
    const iqa=iqaVal!=null?Math.round(iqaVal):"N/A";
    const o3=ozoneVal!=null?`${Math.round(ozoneVal)} µg/m³`:"N/A";
    document.getElementById("air-quality").innerText=`IQA ${iqa} | ${o3}`;
  }catch(e){document.getElementById("air-quality").innerText="Indisponible"}

  const vig=evaluerNiveau(tMinJour,tMaxJour,iqaVal,ozoneVal);
  const badge=document.getElementById("vigilance-badge");
  badge.innerText=vig.niveau; badge.style.backgroundColor=couleursCSS[vig.niveau];
  document.getElementById("vigilance-motifs").innerText=vig.motifs.length?vig.motifs.join(" · "):"Aucun seuil expérimental atteint.";

  try{
    const fin=new Date(); fin.setDate(fin.getDate()-1);
    const debut=new Date(fin); debut.setDate(debut.getDate()-180);
    const iso=d=>d.toISOString().slice(0,10);
    const d=await jsonFetch(`https://archive-api.open-meteo.com/v1/archive?latitude=${cfg.latitude}&longitude=${cfg.longitude}&start_date=${iso(debut)}&end_date=${iso(fin)}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto`);
    const times=d.daily?.time||[], mins=d.daily?.temperature_2m_min||[], maxs=d.daily?.temperature_2m_max||[], rain=d.daily?.precipitation_sum||[];
    let pluie7=0,pluie30=0,gddTotal=0; const mois={};
    for(let i=0;i<times.length;i++){
      const dt=new Date(times[i]+"T12:00:00"), mn=mins[i],mx=maxs[i],p=rain[i]??0;
      if(mn==null||mx==null)continue;
      const age=(fin-dt)/86400000;
      if(age<7)pluie7+=p;
      if(age<30)pluie30+=p;
      const gdd=Math.max(0,((mn+mx)/2)-10); gddTotal+=gdd;
      const key=times[i].slice(0,7);
      if(!mois[key])mois[key]={min:[],max:[],gdd:0,gel:0,chaleur:0,pluie:0};
      mois[key].min.push(mn);mois[key].max.push(mx);mois[key].gdd+=gdd;mois[key].pluie+=p;
      if(mn<=0)mois[key].gel++; if(mx>=35)mois[key].chaleur++;
    }
    document.getElementById("pluie-cumul").innerText=`${pluie7.toFixed(1)} / ${pluie30.toFixed(1)} mm`;
    document.getElementById("gdd-cumul").innerText=`${gddTotal.toFixed(1)} °C.j`;
    let rows="";
    for(const [m,v] of Object.entries(mois).sort()){
      const avg=a=>a.reduce((x,y)=>x+y,0)/a.length;
      const niv=evaluerNiveau(Math.min(...v.min),Math.max(...v.max),null,null).niveau;
      rows+=`<tr><td><strong>${m}</strong></td><td>${avg(v.min).toFixed(1)} °C</td><td>${avg(v.max).toFixed(1)} °C</td><td><strong>${v.gdd.toFixed(1)}</strong> °C.j</td><td><span class="badge" style="background:${couleursCSS[niv]}">${niv}</span></td><td><span class="tag">Gel ${v.gel}j</span><span class="tag">≥35 °C ${v.chaleur}j</span><span class="tag">Pluie ${v.pluie.toFixed(1)} mm</span></td></tr>`;
    }
    document.getElementById("tableau-mensuel").innerHTML=rows||'<tr><td colspan="6">Données indisponibles.</td></tr>';
  }catch(e){
    document.getElementById("pluie-cumul").innerText="Indisponible";
    document.getElementById("gdd-cumul").innerText="Indisponible";
    document.getElementById("tableau-mensuel").innerHTML='<tr><td colspan="6">Erreur de chargement de l’historique.</td></tr>';
  }
}
window.addEventListener("load",chargerDonnees);
window.addEventListener("click",e=>{if(e.target.id==="settings-modal")toggleModal(false)});
</script>
</body>
</html>
"""

def generer_interface():
    humidite_sol = obtenir_humidite_sol()

    html = HTML_TEMPLATE.replace(
        '<div class="metric-value" id="soil-moisture">-- %</div>',
        f'<div class="metric-value" id="soil-moisture">{humidite_sol["humidite_pourcent"]:.2f} %</div>'
    )

    html = html.replace(
        '<div class="site-meta" id="soil-moisture-meta">ERA5-Land · couche 0–7 cm</div>',
        f'<div class="site-meta" id="soil-moisture-meta">ERA5-Land · couche 0–7 cm · {humidite_sol["date"]}</div>'
    )

    FICHIER_SORTIE.write_text(html, encoding="utf-8")
    print(f"✅ Interface générée : {FICHIER_SORTIE.resolve()}")
    print("📜 Licence : GNU General Public License v3.0 (GNU GPLv3)")
    webbrowser.open(FICHIER_SORTIE.resolve().as_uri())

if __name__ == "__main__":
    generer_interface()
