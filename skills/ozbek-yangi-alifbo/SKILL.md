---
name: ozbek-yangi-alifbo
description: O‘zbekcha lotin yoki kirill matnini 2026-yilgi yangi alifboga o‘tkazish (O‘→Ö, G‘→Ğ, Sh→Ş, Ch→Ç): matn, .md, .txt yoki .docx faylni ko‘chirish yoki tekshirishda ishlating.
---

# O‘zbek tilining yangi lotin alifbosiga o‘tkazish

2026-yil 21-oktabrda imzolangan qonun bilan o‘zbek lotin alifbosidagi to‘rtta harf o‘zgardi:

| Eski | Yangi | Misol |
|---|---|---|
| O‘ o‘ | Ö ö | o‘qish → öqiş, O‘zbekiston → Özbekiston |
| G‘ g‘ | Ğ ğ | g‘alaba → ğalaba, tog‘ → toğ |
| Sh sh | Ş ş | shahar → şahar, AQSh → AQŞ |
| Ch ch | Ç ç | choy → çoy, ko‘chirish → köçiriş |

Qolgan harflar, *ng* birikmasi va tutuq belgisi (’ / ʼ: *ma’no, ta’lim*) o‘zgarmaydi — qonun haqidagi rasmiy xabarlarda ular haqida o‘zgarish aytilmagan. Agar foydalanuvchi qonun matnida boshqa o‘zgarish borligini aytsa, unga amal qil.

O‘tish bosqichma-bosqich: eski hujjatlar, pul va qimmatli qog‘ozlar amal qilishda davom etadi. Shuning uchun foydalanuvchi aniq so‘ramasa, matnni o‘zboshimchalik bilan yangi alifboga o‘tkazma.

## Qoidalar

1. **Katta-kichik harf:** *Sh → Ş*, *SH → Ş*, *sh → ş* (Ch ham shunday). Bosh harfli yozuvda *O‘ZBEKISTON → ÖZBEKISTON*, *TOSHKENT → TOŞKENT*.
2. **O‘/G‘ belgisi variantlari:** o va g dan keyin kelgan ‘ ʻ ’ ' ` belgilarning hammasi bitta harfga aylanadi (*o‘, oʻ, o’, o', o`* → *ö*). *o‘* faqat keyin harf kelsa o‘zgaradi (so‘z oxiridagi *‘video’* — qo‘shtirnoq); *g‘* so‘z oxirida ham o‘zgaradi (*tog‘ → toğ*).
3. **Tutuq belgisi** o va g dan boshqa harflardan keyin turadi (*ma’no, san’at, Is’hoq*) — tegma. *Is’hoq* da s va h alohida tovush, ş emas.
4. **sh, ch har doim bitta harf:** *mashhur → maşhur* (ş + h), *ishchi → işçi*.
5. **Tegilmaydigan joylar:** URL, e-pochta, kod, fayl nomi, kimyoviy formula, inglizcha va boshqa chet tilidagi so‘z hamda brendlar asl yozuvida qoladi: *Disney Channel, Shanghai, Chicago, Microsoft, Hugh Johnston*. Chet so‘zni bilish uchun belgi: w, c (ch dan tashqari), th, ph, ck, gh, ee, oo, ea birikmalari o‘zbekchada yo‘q.
6. **O‘zbekcha yozilgan chet ismlar** (*Josh D’Amaro, Shanxay, Chikago*) — o‘zbekcha transkripsiya bo‘lgani uchun yangi alifboga o‘tadi (*Joş, Şanxay, Çikago*), lekin rasmiy hujjatda ismni pasportdagidek qoldirish kerak bo‘lishi mumkin. Shubhali ismlarni foydalanuvchiga ro‘yxat qilib ko‘rsat.
7. **Kirill yozuvi** to‘g‘ridan-to‘g‘ri yangi lotinga o‘tadi (oraliq eski lotinsiz, shuning uchun *Исҳоқ → Ishoq* to‘g‘ri chiqadi): ш→ş, ч→ç, ў→ö, ғ→ğ, қ→q, ҳ→h, х→x, ё→yo, ю→yu, я→ya, ъ→’, ь→(tushib qoladi), щ→şç. *е* so‘z boshida va unli / ъ / ь dan keyin → *ye* (*ер → yer*), aks holda *e*. *ц* unlidan keyin → *ts* (*лицей → litsey*), aks holda *s* (*цех → sex, станция → stansiya*). Lotin va kirill aralash matn ham ishlaydi.

## Ish tartibi

1. Matn qisqa bo‘lsa (chatda), qoidalar bo‘yicha qo‘lda o‘tkaz va o‘zgargan ism / chet so‘zlarni pastda sanab ber.
2. Fayl bo‘lsa (.txt, .md, .docx; eski .doc ni avval `soffice --headless --convert-to docx fayl.doc` bilan .docx ga o‘tkaz), shu papkadagi `uz2026.py` skriptini ishga tushir (skript pastda ham keltirilgan). U har doim **yangi fayl** yozadi, asl faylni o‘zgartirmaydi. .docx da formatlash (shrift, qalin, jadval, kolontitul) saqlanadi.
   ```
   python3 uz2026.py kirish.docx chiqish_yangi_alifbo.docx
   ```
3. Skript ikki ro‘yxat chiqaradi: **tegilmagan chet so‘zlar** va **gap o‘rtasidagi o‘zgargan bosh harfli so‘zlar** (ismlar, brendlar, qisqartmalar). Ikkalasini ko‘zdan kechir: noto‘g‘ri o‘zgargan brendni (masalan, *Channel → Çannel*) qo‘lda qaytar, o‘zbekcha so‘z chet deb o‘tkazib yuborilgan bo‘lsa, qo‘lda tuzat. Natijani foydalanuvchiga shu ro‘yxatlar bilan qisqa qilib ayt.
4. Shriftni tekshir: Ö Ğ Ş Ç turk va Yevropa shriftlarida bor (Times New Roman, Arial, Calibri, Roboto). Juda bezakli shrift bo‘lsa, PDF / skrinshot qilib harflar to‘g‘ri chiqqanini ko‘r.

## Skript: uz2026.py

```python
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
```

Manba: qonun imzolangani haqida gov.uz xabarlari (21.10.2026): https://gov.uz/en/yoshlar/news/view/246056
