from pathlib import Path
import re,json,statistics
root=Path(__file__).parent
results=[]
for p in sorted((root/'tekst').glob('0[0-6]*.md')):
 paras=[x.strip() for x in p.read_text().split('\n\n') if x.strip() and not x.startswith(('#','|','**Tabela','Źródło:'))]
 sents=[]
 for par in paras:
  par=re.sub(r'\([^()]*\b(?:19|20)\d{2}[^()]*\)','',par)
  par=re.sub(r'\b(?:m\.in\.|np\.|tzw\.|art\.|ust\.|lit\.|in\.|nr\.)',lambda m:m.group(0).replace('.','∯'),par,flags=re.I)
  par=re.sub(r'(?<=\d)\.(?=\d)','∯',par)
  for s in re.split(r'(?<=[.!?])\s+',par):
   words=re.findall(r"[^\W_]+(?:[-’'][^\W_]+)*",s,re.UNICODE)
   if words:sents.append((len(words),s.replace('∯','.')))
 lens=[n for n,s in sents]
 results.append({'file':p.name,'sentences':len(lens),'words':sum(lens),'mean':round(statistics.mean(lens),2),'median':statistics.median(lens),'max':max(lens),'over30':sum(n>30 for n in lens)})
 for n,s in sents:
  if n>30:print('DŁUGIE',p.name,n,s)
print(json.dumps(results,ensure_ascii=False,indent=2))
agg={'sentences':sum(r['sentences'] for r in results),'words':sum(r['words'] for r in results)}
agg['mean']=round(agg['words']/agg['sentences'],2)
print('CAŁOŚĆ',agg)
(root/'statystyki.json').write_text(json.dumps({'chapters':results,'total':agg},ensure_ascii=False,indent=2))
