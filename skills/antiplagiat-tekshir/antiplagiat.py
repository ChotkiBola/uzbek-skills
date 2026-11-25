"""Platformasiz antiplagiat yordamchisi.
  python3 antiplagiat.py tayyorla  hujjat.docx            -> matn.txt (titul, mundarija, adabiyotlar olib tashlanadi)
  python3 antiplagiat.py gaplar    matn.txt [--n 30]       -> gaplar.json (internetda qidirish uchun o'ziga xos gaplar)
  python3 antiplagiat.py solishtir matn.txt manba1 [manba2 ...] [--k 6]  -> moslik foizi va parchalar
  python3 antiplagiat.py ai        matn.txt                -> AI uslubi ko'rsatkichlari
"""
import re,sys,json,subprocess,statistics as st,collections
AP="‘’ʻʼ`´'"
def read(p):
    if p.endswith('.docx'):
        from docx import Document
        d=Document(p);parts=[x.text for x in d.paragraphs]
        for t in d.tables:
            for r in t.rows: parts.append(' | '.join(c.text for c in r.cells))
        return '\n'.join(parts)
    if p.endswith('.pdf'): return subprocess.run(['pdftotext','-layout',p,'-'],capture_output=True,text=True).stdout
    if p.endswith('.doc'):
        subprocess.run(['soffice','--headless','--convert-to','txt:Text (encoded):UTF8','--outdir','/tmp',p],capture_output=True)
        import os;return open('/tmp/'+os.path.basename(p)[:-4]+'.txt',encoding='utf-8',errors='ignore').read()
    return open(p,encoding='utf-8',errors='ignore').read()
def words(t):
    t=t.lower()
    for a in AP: t=t.replace(a,'')
    return re.findall(r"[a-zа-яёўқғҳöğşç0-9]+",t)
STOP_HEAD=re.compile(r"^(mundarija|содержание|оглавление|contents)\b",re.I)
REF_HEAD=re.compile(r"^(foydalanilgan (adabiyot|manba|internet)|adabiyotlar ro|manbalar|список литературы|литература|references|bibliography)",re.I)
BOILER=re.compile(r"(vazirligi|universiteti|kafedrasi|fakulteti|bajardi|tekshirdi|ilmiy rahbar|toshkent\s*[–-]\s*20\d\d|министерство|университет)",re.I)
def tayyorla(t):
    out=[];skip=False
    lines=[l.strip() for l in t.split('\n') if l.strip()]
    refs=[i for i,l in enumerate(lines) if REF_HEAD.match(l)]
    if refs: lines=lines[:refs[-1]]                     # oxirgi "adabiyotlar" sarlavhasidan keyingisi olib tashlanadi
    for s in lines:
        if STOP_HEAD.match(s): skip='toc';continue
        if skip=='toc':
            if len(s.split())>12 and not re.search(r"\.{4,}|\d+\s*$",s): skip=False
            else: continue
        if len(s.split())<4 and BOILER.search(s): continue
        if BOILER.search(s) and len(s.split())<12: continue
        out.append(s)
    return '\n'.join(out)
def gaplar(t,n):
    sents=[x.strip() for x in re.split(r'(?<=[.!?])\s+|\n+',t) if len(x.split())>=12]
    freq=collections.Counter(w for s in sents for w in words(s))
    def score(s):
        ws=words(s);rare=sum(1 for w in ws if freq[w]<=2 and len(w)>5)
        return rare+2*(len(re.findall(r'\d',s))>0)+min(len(ws),30)/10
    idx=sorted(range(len(sents)),key=lambda i:-score(sents[i]))[:n]
    idx.sort()   # hujjat bo'ylab bir tekis
    res=[]
    for k,i in enumerate(idx):
        ws=sents[i].split();mid=max(0,len(ws)//2-5)
        res.append({'id':k+1,'gap':sents[i],'qidiruv':' '.join(ws[mid:mid+10])})
    return res,len(sents)
def solishtir(t,srcs,k):
    w=words(t);cov=[0]*len(w);per={}
    for s in srcs:
        sw=words(read(s));S={tuple(sw[i:i+k]) for i in range(len(sw)-k+1)};h=0
        for i in range(len(w)-k+1):
            if tuple(w[i:i+k]) in S:
                h+=1
                for j in range(i,i+k): cov[j]=1
        per[s]=h
    pct=100*sum(cov)/max(1,len(w))
    runs=[];i=0
    while i<len(w):
        if cov[i]:
            j=i
            while j<len(w) and cov[j]: j+=1
            runs.append((j-i,' '.join(w[i:j])));i=j
        else: i+=1
    return pct,per,sorted(runs,reverse=True)[:10],len(w)
STRONG=["muhim ahamiyat kasb eta","alohida e'tiborga (?:loyiq|molik)","yorqin misol","bo'la oladi","xulosa qilib aytganda","zamonaviy dunyoda","ajralmas qismi","yo'l ochib beradi","mustahkam poydevor","yangi imkoniyatlar","keng imkoniyatlar","muhim qadam","yangicha yondashuv","eng qizig'i","savol tug'iladi","\\btasavvur qiling","umid qilamanki","namunasidir"]
def ai(t):
    low=t.lower()
    for a in AP: low=low.replace(a,"'")
    n=max(1,len(low.split()))
    hits={p:len(re.findall(r"\b"+p,low)) for p in STRONG};hits={k:v for k,v in hits.items() if v}
    sents=[s for s in re.split(r'(?<=[.!?])\s+',t) if len(s.split())>2]
    L=[len(s.split()) for s in sents] or [0]
    d=len(re.findall(r" [—–] ",t))
    return {"so'z":n,"kuchli qoliplar (1 mln so'zga)":round(sum(hits.values())/n*1e6),"topilganlar":hits,
            "chiziqcha / 1000 so'z (odam ~5,3)":round(d/n*1000,1),
            "'muhim' / 1 mln (odam ~500)":round(len(re.findall(r"\bmuhim",low))/n*1e6),
            "gap uzunligi o'rtacha":round(st.mean(L),1),"gap uzunligi tarqoqligi (CV; odam odatda >0,6)":round(st.pstdev(L)/max(1,st.mean(L)),2),
            "'nafaqat/emas, balki' / 1000 so'z":round(len(re.findall(r"nafaqat|emas,? balki",low))/n*1000,2)}
if __name__=='__main__':
    cmd=sys.argv[1];a=[x for x in sys.argv[2:] if not x.startswith('--')]
    opt=lambda k,d:int(sys.argv[sys.argv.index(k)+1]) if k in sys.argv else d
    a=[x for x in a if not (x.isdigit())]
    if cmd=='tayyorla':
        t=tayyorla(read(a[0]));open('matn.txt','w').write(t)
        print(f"matn.txt: {len(words(t))} so'z (asl: {len(words(read(a[0])))} so'z; titul, mundarija, adabiyotlar olib tashlandi)")
    elif cmd=='gaplar':
        t=read(a[0]);n=opt('--n',max(15,min(60,len(words(t))//200)))
        res,tot=gaplar(t,n);json.dump(res,open('gaplar.json','w'),ensure_ascii=False,indent=1)
        print(f"{tot} ta gapdan {len(res)} tasi tanlandi -> gaplar.json")
        for r in res: print(f"{r['id']:>3}. \"{r['qidiruv']}\"")
    elif cmd=='solishtir':
        pct,per,runs,nw=solishtir(read(a[0]),a[1:],opt('--k',6))
        print(f"Matn {nw} so'z; manbalar bilan mos: {pct:.1f}%")
        for s,h in sorted(per.items(),key=lambda x:-x[1]): print(f"  {s}: {h} ta mos bo'lak")
        for L,x in runs: print(f"  [{L} so'z] {x[:200]}")
    elif cmd=='ai':
        for k,v in ai(read(a[0])).items(): print(f"{k}: {v}")
