from pathlib import Path
import json,hashlib,base64
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'public-market-data.json').read_text())
import pandas as pd
rets={s:pd.Series(v['adj'],index=v['dates']).pct_change(fill_method=None).dropna() for s,v in raw['symbols'].items()}
frame=pd.DataFrame(rets)
corr=frame.tail(252).corr(min_periods=200)
pairs={}
for ticker,target in raw['symbols'].items():
 ranked=corr[ticker].dropna().sort_values(ascending=False)
 out=[]
 for other,r in ranked.items():
  candidate=raw['symbols'][other]
  if other==ticker or (target.get('cik') and target['cik']==candidate.get('cik')) or r<=0:continue
  one=frame.tail(252)[[ticker,other]].dropna();two=frame.tail(504)[[ticker,other]].dropna()
  if len(one)<200:continue
  out.append({'symbol':other,'r':round(float(one.corr().iloc[0,1]),6),'r2':round(float(two.corr().iloc[0,1]),6) if len(two)>=400 else None,'n':len(one),'n2':len(two),'start':one.index[0],'end':one.index[-1],'kind':candidate['kind'],'name':candidate['name'],'sector':candidate['sector'],'same':candidate['sector']==target['sector']})
  if len(out)==3:break
 pairs[ticker]=out
public={k:v for k,v in raw.items() if k!='symbols'}
public['symbols']={s:{k:v for k,v in x.items() if k not in ('adj','dates')} for s,x in raw['symbols'].items()}
public['pairs']=pairs
(ROOT/'derived-public-data.json').write_text(json.dumps(public,separators=(',',':')))
js=(ROOT/'monitor.js').read_text().replace('/*PUBLIC_DATA*/',json.dumps(public,separators=(',',':')))
# Only height leaves the sandbox. No private values are sent to the parent.
js+='\nnew ResizeObserver(()=>parent.postMessage({type:"loss-height",height:Math.ceil(document.documentElement.scrollHeight)},"*")).observe(document.body);\n'
hash=base64.b64encode(hashlib.sha256(js.encode()).digest()).decode()
csp=f"<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none'; script-src 'sha256-{hash}'; style-src 'unsafe-inline'; connect-src 'none'; img-src 'none'; form-action 'none'; base-uri 'none'; object-src 'none';\">"
html=(ROOT/'monitor-template.html').read_text().replace('<!--CSP-->',csp).replace('/*MONITOR_SCRIPT*/',js)
(ROOT/'dev/loss-monitor.html').write_text(html)
index=(ROOT/'dev/index.html').read_text()
if 'href="#harvest"' not in index:
 index=index.replace('<a href="#knight">Tim Knight watch</a>','<a href="#knight">Tim Knight watch</a><a href="#harvest">Loss-harvest review</a>')
 index=index.replace("const id=location.hash==='#knight'?'knight':'earnings';","const id=location.hash==='#harvest'?'harvest':location.hash==='#knight'?'knight':'earnings';")
 panel='<main class="dashboard" id="harvest" hidden><iframe id="loss-frame" title="Private local loss-harvest review" src="loss-monitor.html" loading="lazy" sandbox="allow-scripts allow-downloads" style="border:0;width:100%;height:1700px;display:block"></iframe></main>'
 index=index.replace('</div><script>',panel+'</div><script>',1)
 index=index.replace("addEventListener('hashchange',showTab);showTab();","addEventListener('hashchange',showTab);showTab();\naddEventListener('message',event=>{const f=document.getElementById('loss-frame');if(event.source===f.contentWindow&&event.data?.type==='loss-height'&&Number.isFinite(event.data.height))f.style.height=Math.max(800,Math.min(100000,event.data.height+40))+'px'});")
 (ROOT/'dev/index.html').write_text(index)
print('Child bytes',len(html),'source public pairs',len(pairs),'CBOE top',pairs.get('CBOE'))
