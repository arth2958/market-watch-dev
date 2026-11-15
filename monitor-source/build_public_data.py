import json, pathlib, datetime, math
import yfinance as yf
import pandas as pd
ROOT=pathlib.Path(__file__).resolve().parent
universe=json.loads((ROOT/'universe.json').read_text())
# This fixed public universe is independent of every uploaded file.
data=yf.download(list(universe),period='2y',auto_adjust=False,progress=False,threads=8)
result={'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':'Yahoo Finance via yfinance; adjusted closes for returns, Close for marking','universe_source':'https://github.com/datasets/s-and-p-500-companies/blob/main/data/constituents.csv','universe_count':len(universe),'symbols':{},'failures':[]}
for ticker,meta in universe.items():
 try:
  adj=data['Adj Close'][ticker].dropna(); close=data['Close'][ticker].dropna()
  if len(adj)<200 or close.empty: raise ValueError('insufficient history')
  result['symbols'][ticker]={**meta,'dates':[x.strftime('%Y-%m-%d') for x in adj.index],'adj':[round(float(x),6) for x in adj.values],'close':round(float(close.iloc[-1]),6),'asof':close.index[-1].strftime('%Y-%m-%d')}
 except Exception: result['failures'].append(ticker)
if len(result['symbols'])<len(universe)*.8:raise SystemExit('Coverage under 80%; refusing update')
(ROOT/'public-market-data.json').write_text(json.dumps(result,separators=(',',':'),allow_nan=False))
print('Public symbols:',len(result['symbols']),'unavailable:',len(result['failures']),'latest:',max(x['asof'] for x in result['symbols'].values()))
