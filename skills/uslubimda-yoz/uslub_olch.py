import re,sys,collections,statistics as st
t=open(sys.argv[1],encoding='utf-8').read()
paras=[p for p in re.split(r'\n\s*\n',t) if p.strip()]
sents=[s for s in re.split(r'(?<=[.!?])\s+|\n+',t) if s.strip()]
words=re.findall(r"[A-Za-zА-Яа-яЁёЎўҚқҒғҲҳÖöĞğŞşÇçʻʼ‘’'`-]+",t)
W=len(words) or 1
sl=[len(re.findall(r"\S+",s)) for s in sents]
cyr=sum(1 for c in t if 'А'<=c<='я' or c in 'ЎўҚқҒғҲҳЁё');lat=sum(1 for c in t if c.isascii() and c.isalpha())
def per1k(n):return round(n/W*1000,1)
print(f"So‘z: {W}, gap: {len(sents)}, abzats: {len(paras)}")
print(f"Gap uzunligi: o‘rtacha {st.mean(sl):.1f} so‘z, median {st.median(sl)}, eng qisqa {min(sl)}, eng uzun {max(sl)}")
print(f"Abzats: o‘rtacha {W/len(paras):.0f} so‘z")
print(f"Yozuv: lotin {lat}, kirill {cyr} harf; yangi alifbo harflari (ÖĞŞÇ): {len(re.findall('[ÖöĞğŞşÇç]',t))}")
print("O‘/g‘ belgisi:",dict(collections.Counter(re.findall(r"[oOgG]([‘'ʻ`’])",t))))
for name,rx in [("chiziqcha —",r" [—–] "),("defis-chiziqcha ' - '",r" - "),("ko‘p nuqta",r"\.\.\.|…"),("undov !",r"!"),("savol ?",r"\?"),("qavs-kulgi ))",r"\)\)+"),("emoji",r"[\U0001F300-\U0001FAFF☀-➿]"),("vergul",r","),("ikki nuqta",r":")]:
    print(f"{name}: {per1k(len(re.findall(rx,t)))} / 1000 so‘z")
print("Kichik harf bilan boshlangan gaplar:",sum(1 for s in sents if s.strip()[0].islower()),"/",len(sents))
print("Nuqtasiz tugagan abzatslar:",sum(1 for p in paras if p.strip()[-1] not in '.!?)…'),"/",len(paras))
low=[w.lower() for w in words]
print("Eng ko‘p so‘zlar:",', '.join(f"{w}({c})" for w,c in collections.Counter(low).most_common(25)))
bi=collections.Counter(zip(low,low[1:]))
print("Eng ko‘p ikki so‘zlik:",', '.join(f"{a} {b}({c})" for (a,b),c in bi.most_common(12)))
print("Gap boshlari:",', '.join(f"{w}({c})" for w,c in collections.Counter(re.findall(r"\S+",s)[0].lower() for s in sents if s.split()).most_common(10)))
mid=[w for s in sents for w in re.findall(r"\S+",s)[1:] if w[0].isupper() and not w.isupper()]
print("Gap o‘rtasidagi bosh harfli so‘zlar:",len(mid),"→",', '.join(mid[:15]))
print("Ikki bosh harf xatosi (RAngi):",', '.join(re.findall(r"\b[A-ZА-Я]{2}[a-zа-я]\w*",t)) or '—')
print("Tinish belgisidan oldin bo‘sh joy (' ,' ' ?'):",len(re.findall(r"\s[,?!.]",t)))
