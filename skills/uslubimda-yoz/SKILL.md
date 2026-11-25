---
name: uslubimda-yoz
description: Odamning matnlaridan uslubini o‘rganib, xuddi o‘zidek yozish: asosan akademik matnlar (referat, maqola, dissertatsiya, keys) va ba’zan ko‘cha tilidagi xabar va postlar.
---

# Uslubimda yoz: odamning yozish uslubiga moslashish

Ikki bosqich: (1) namunalardan **uslub profili** tuziladi, (2) yangi matn shu profil bo‘yicha yoziladi. Profil bir marta tuziladi va keyin qayta ishlatiladi.

Asosiy foydalanish ikki registrda: **akademik** (referat, maqola, keys stadi, magistrlik dissertatsiyasi, taqriz) va **ko‘cha tili** (do‘stlarga xabar, Telegram/Instagram post, norasmiy izoh). Bitta odamning bu ikki uslubi butunlay farq qiladi, shuning uchun profil **har registr uchun alohida** tuziladi va hech qachon aralashtirilmaydi. So‘rovdan registr aniq bo‘lmasa, so‘ra: "akademikmi yoki ko‘cha tilidami?"

## Chegaralar

- Kimning uslubi o‘rganilayotganini so‘ra. Foydalanuvchining o‘zi yoki ruxsat bergan odam (mijoz, hamkasb, blog muallifi uchun ghostwriting) — mumkin.
- Boshqa odam nomidan uni aldash uchun xabar, guvohnoma, hujjat yoki sharh yozma (u yozgandek qilib uchinchi shaxslarga taqdim etish uchun). Bunday so‘rovni rad et va halol variantni taklif qil.
- Namunadagi gaplarni so‘zma-so‘z ko‘chirma: uslubni olasan, matnni emas. Ikki-uch so‘zli sevimli iboralar bundan mustasno.
- Faktlar har doim to‘g‘ri bo‘lishi kerak: uslub faqat ifodaga ta’sir qiladi.

## 1-bosqich: profil tuzish

### Namuna yig‘ish
- Kamida 5–10 ta matn yoki jami 800+ so‘z. Kam bo‘lsa, profilni "dastlabki" deb belgila.
- Bir xil janrdan (post, ish xabari, ilmiy matn) yaxshiroq; har xil janr bo‘lsa, janr bo‘yicha alohida ko‘rsatkich yoz.
- AI yozgan yoki boshqa odam tahrir qilgan matnlarni chiqarib tashla (so‘ra).

### O‘lchash
Namunalarni bitta faylga jamlab (namunalar orasida bo‘sh qator), shu papkadagi `uslub_olch.py` skriptini ishga tushir (skript pastda ham keltirilgan):
```
python3 uslub_olch.py namunalar.txt
```
Skript gap va abzats uzunligi, yozuv (lotin / kirill / yangi alifbo), o‘/g‘ belgisi turi, tinish belgilari chastotasi, emoji va "))" kulgisi, sevimli so‘z va iboralar, gap boshlari, bosh harf odatlari va tinish belgisidan oldingi bo‘sh joylarni sanaydi.

### Qo‘lda tahlil (skript ko‘rmaydigan narsalar)
1. **Murojaat va ohang:** siz / sen, rasmiy / do‘stona, hazil bormi, so‘kinish bormi.
2. **Til aralashmasi:** ruscha, inglizcha so‘zlar qanchalik va qaysi sohada (texnik atamalar inglizchami?).
3. **Sheva va og‘zaki shakllar:** *qivor, ob tashla, ko‘rolishadimi, jigar, -miz / -man*, qisqartirilgan qo‘shimchalar.
4. **Tuzilish:** ro‘yxat yoki oddiy matn, sarlavha ishlatadimi, abzats qanday boshlanadi va tugaydi, xulosa yozadimi.
5. **Sevimli kirish va yakun:** salomlashish, "Qara", "Xullas", imzo, chaqiruv.
6. **Imlo odatlari:** ataylab qiladigan (masalan, hamma gapni kichik harfda yozish, nuqtasiz tugatish) va tasodifiy xatolar (*RAngi*, *MAshxur* — Shift tez qo‘yib yuborilgan). Tasodifiy xatolarni taqlid qilma, faqat izchil odatlarni ol.

### Akademik registr: nimaga qarash kerak
- **Kim gapiradi:** "biz" (muallif-biz), shaxssiz shakl (*o‘rganildi, tahlil qilindi, aniqlandi*) yoki "men". Qaysi biri ko‘p — shuni ol.
- **Gap tuzilishi:** o‘rtacha uzunlik, ergash gaplar, "-ligi sababli", "-ganligi bois" kabi bog‘lovchilar.
- **Atamalar:** bir tushuncha uchun doim bitta atama (*tushum* yoki *daromad* — aralashtirma); ruscha/inglizcha atamalar qavsda beriladimi.
- **Iqtibos va manba:** [1], [1, 12-b.] yoki (Muallif, yil); jadval va rasm imzosi ("1-jadval.", "2-rasm."); raqam formati (*102,3 mlrd*).
- **Tuzilma:** kirish — asosiy qism — xulosa, bo‘lim raqamlari, "Xulosa qilib aytganda" kabi o‘tishlar ishlatadimi.
- Akademik matnda ham AI qoliplarini tozala (humanizer-uz), lekin muallif doim ishlatadigan rasmiy iboralar (*"shuni ta’kidlash lozimki"*) profilda bo‘lsa, me’yorida qoladi.
- Sheva, ko‘cha so‘zlari, emoji va "))" akademik matnga hech qachon o‘tmaydi.

### Ko‘cha tili registri: nimaga qarash kerak
- **Qisqartirilgan og‘zaki shakllar:** *qivor, ob tashla, ko‘rolishadimi, demadimku, bo‘pti*.
- **Murojaat va laqablar:** *jigar, brat, aka, sen*.
- **Ruscha va inglizcha qo‘shimchalar:** *prosta, voobshe, koroche, okay, link*; qaysi so‘zlar va qanchalik tez-tez.
- **Imlo erkinligi:** o‘/g‘ o‘rniga o', yangi alifbo (*köça, bölişi*), bosh harfsiz yoki nuqtasiz yozish, tinish belgisidan oldin bo‘sh joy — izchil bo‘lsa, odat sifatida ol.
- **Kulgi va emoji:** "))", ")))", emoji turi va chastotasi.
- **Gap uzunligi:** odatda qisqa; bir xabarda bitta fikr yoki bir nechta xabarga bo‘lish.
- Ko‘cha tilida ham ma’noni buzadigan imlo xatosini qilma; faqat odatdagi og‘zaki shakllarni ol.

### Profil fayli
Natijani qisqa profil qilib yoz (bitta sahifa):
```
# <Ism> uslubi — <akademik | ko‘cha tili> (<janr>, <namuna soni>, <so‘z soni>)
Raqamlar: o‘rtacha gap N so‘z (qisqa/uzun aralash?), abzats N so‘z, "!" N/1000, emoji ..., "))" ...
Yozuv va imlo: ...
Ohang va murojaat: ...
Doim qiladi: (5–8 band, har biri namunadan 2–4 so‘zli misol bilan)
Hech qachon qilmaydi: (3–6 band)
Sevimli so‘z / iboralar: ...
Janr farqlari: ...
```
Har registr uchun alohida profil yoz. Profilni foydalanuvchiga ko‘rsat va to‘g‘riligini so‘ra. Saqlash uchun: foydalanuvchining o‘z uslubi bo‘lsa — xotiraga (memory) yoki `uslub-<ism>` nomli alohida skill qilib taklif qil; boshqa odamniki bo‘lsa — fayl qilib ber.

## 2-bosqich: profil bo‘yicha yozish

1. Avval mazmunni yoz (faktlar, tartib), keyin uni profilga o‘tkaz — ikkalasini bir vaqtda qilma.
2. Raqamli ko‘rsatkichlarga mosla: gap uzunligi o‘rtachadan ±30% dan oshmasin, tinish belgilari, emoji va "))" chastotasi profilga yaqin bo‘lsin.
3. Profildagi "doim qiladi" va "hech qachon qilmaydi" ro‘yxatlarini band-band tekshir.
4. AI belgilarini olib tashla (humanizer-uz bo‘lsa, uni qo‘lla), lekin muallifning o‘z odatlarini saqla: u chiziqcha yoki "nafaqat… balki"ni ko‘p ishlatsa, ular qoladi.
5. Registrni tekshir: faqat shu registr profilini qo‘lla. Akademik matnga ko‘cha so‘zi, ko‘cha xabariga esa akademik ibora (*"tahlil natijalari shuni ko‘rsatadiki"*) o‘tmasin.
6. Akademik matnda yozuv va imloni oxirida alohida tekshir: bitta alifbo, bir xil o‘/g‘ belgisi, atamalar izchil, raqam va iqtibos formati bir xil.
7. Qoralamani berib, "qaysi joy o‘zingizga o‘xshamadi?" deb so‘ra. Har bir tuzatishni o‘sha registr profiliga yangi band qilib qo‘sh.

## Skript: uslub_olch.py

```python
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
```
