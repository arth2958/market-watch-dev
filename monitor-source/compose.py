from pathlib import Path
import json,hashlib,base64
ROOT=Path(__file__).resolve().parent
# Automatic data disabled pending permitted source and display/derived-data rights.
public={'generated_at':'2026-11-16','source':'Manual user marks only; automatic data paused','universe_count':0,'failures':[],'symbols':{},'pairs':{}}
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
print('Child bytes',len(html),'manual-only; no bundled market data')

indexpath=ROOT/'dev/index.html'
index=indexpath.read_text()
bridge=(ROOT/'storage-bridge.js').read_text()
if '/* Device-only portfolio storage bridge.' not in index:
 index=index.replace('</body>','<script>'+bridge+'</script></body>')
 indexpath.write_text(index)
