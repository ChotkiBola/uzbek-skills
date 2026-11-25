import re,sys
AP="‘'ʻ`’"   # o‘/g‘ belgisi variantlari
FOREIGN=re.compile(r"w|c(?!h)|th|ph|ck|gh|ee|oo|ea|[äüßéè]",re.I)
PROTECT=re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+|`[^`]*`")
WORD=re.compile(r"[A-Za-zА-Яа-яЁёЎўҚқҒғҲҳʻʼ‘’'`ÖöĞğŞşÇç]+")
CYR={'а':'a','б':'b','в':'v','г':'g','д':'d','ё':'yo','ж':'j','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'x','ч':'ç','ш':'ş','щ':'şç','ъ':'’','ы':'i','ь':'','э':'e','ю':'yu','я':'ya','ў':'ö','қ':'q','ғ':'ğ','ҳ':'h'}
VOW='аеёиоуэюяўАЕЁИОУЭЮЯЎ'
def cyr_word(w):
    out=[]
    for i,ch in enumerate(w):
        lo=ch.lower();prev=w[i-1] if i else ''
        if lo=='е': r='ye' if (i==0 or prev in VOW or prev.lower() in 'ъь') else 'e'
        elif lo=='ц': r='ts' if (prev and prev in VOW) else 's'
        else: r=CYR.get(lo,ch)
        if ch!=lo and r:
            allcaps=len(w)>1 and w.isupper()
            r=r.upper() if allcaps else r[0].upper()+r[1:]
        out.append(r)
    return ''.join(out)
CYRW=re.compile(r"[А-Яа-яЁёЎўҚқҒғҲҳ]+")
def conv_word(w):
    if FOREIGN.search(w): return w
    def oq(m):
        L=m.group(1);return {'o':'ö','O':'Ö','g':'ğ','G':'Ğ'}[L]
    w=re.sub(r"([oO])[%s](?=[A-Za-zÖöĞğŞşÇç])"%AP,oq,w)   # o‘ faqat harfdan oldin
    w=re.sub(r"([gG])[%s]"%AP,oq,w)                        # g‘ so‘z oxirida ham (tog‘)
    w=re.sub(r"SH","Ş",w);w=re.sub(r"Sh|sH","Ş" ,w);w=w.replace("sh","ş")
    w=re.sub(r"CH","Ç",w);w=re.sub(r"Ch|cH","Ç",w);w=w.replace("ch","ç")
    return w
def convert(text,report=None):
    out=[];pos=0
    for m in PROTECT.finditer(text):
        out.append(_conv(text[pos:m.start()],report));out.append(m.group());pos=m.end()
    out.append(_conv(text[pos:],report));return ''.join(out)
def _conv(t,report):
    def f(m):
        w=m.group()
        if CYRW.search(w): return cyr_word(w)   # kirill -> to‘g‘ridan-to‘g‘ri yangi lotin
        n=conv_word(w)
        if report is not None:
            if n==w and re.search(r"sh|ch|[og][%s]"%AP,w,re.I) and FOREIGN.search(w): report['skipped'].add(w)
            elif n!=w and w[0].isupper():
                pre=t[:m.start()].rstrip()
                if pre and pre[-1] not in '.!?:;\n"“«(-–—0123456789' and not w.isupper(): report['names'].add(w+' → '+n)
        return n
    return WORD.sub(f,t)
if __name__=='__main__':
    src,dst=sys.argv[1],sys.argv[2];rep={'skipped':set(),'names':set()}
    if src.endswith('.docx'):
        from docx import Document
        d=Document(src)
        def paras(container):
            for p in container.paragraphs: yield p
            for t in container.tables:
                for row in t.rows:
                    for c in row.cells: yield from paras(c)
        allp=list(paras(d))
        for s in d.sections: allp+=list(paras(s.header))+list(paras(s.footer))
        for p in allp:
            for r in p.runs: r.text=convert(r.text,rep)
        d.save(dst)
    else:
        open(dst,'w').write(convert(open(src).read(),rep))
    print('Tegilmagan (chet so‘z deb topildi):',', '.join(sorted(rep['skipped'])) or '—')
    print('O‘zgargan bosh harfli so‘zlar (ismlarni tekshiring):',', '.join(sorted(rep['names'])) or '—')
