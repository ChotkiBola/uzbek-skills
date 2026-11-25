# Uzbek skills — o‘zbek tili uchun Claude skill’lari

Uchta skill bitta to‘plamda:

| Skill | Nima qiladi |
|---|---|
| [`humanizer-uz`](skills/humanizer-uz/SKILL.md) | O‘zbekcha matndan AI uslubini tozalaydi: qolip iboralar ("muhim ahamiyat kasb etadi", "yorqin misol bo‘la oladi"), sun’iy bo‘rttirish, ortiqcha chiziqcha, qalin yorliqlar. Iboralar ro‘yxati odam yozgan 4 mln so‘zlik korpusda o‘lchangan. |
| [`ozbek-yangi-alifbo`](skills/ozbek-yangi-alifbo/SKILL.md) | Matnni 2026-yilgi yangi lotin alifbosiga o‘tkazadi: O‘→Ö, G‘→Ğ, Sh→Ş, Ch→Ç. `.txt`, `.md`, `.docx` fayllar uchun skript bor (`uz2026.py`), formatlash saqlanadi. |
| [`uslubimda-yoz`](skills/uslubimda-yoz/SKILL.md) | Odamning matnlaridan uslub profilini tuzadi va xuddi o‘sha odamdek yozadi. Ikki registr: akademik va ko‘cha tili. O‘lchash skripti: `uslub_olch.py`. |

## O‘rnatish

**Claude Code (plugin sifatida):**
```
/plugin marketplace add ChotkiBola/uzbek-skills
/plugin install uzbek-skills
```
yoki `skills/` ichidagi papkalarni `~/.claude/skills/` ga nusxalang.

**claude.ai / Claude ilovasi:** Settings → Capabilities → Skills → har bir skill papkasini zip qilib yuklang.

## Tez sinov

```
python3 skills/ozbek-yangi-alifbo/uz2026.py matn.docx matn_yangi.docx
python3 skills/uslubimda-yoz/uslub_olch.py namunalar.txt
```

## Ma’lumot manbalari

- Iboralar chastotasi: Hugging Face’dagi [MLDataScientist/Uzbek_news_dataset](https://huggingface.co/datasets/MLDataScientist/Uzbek_news_dataset) (CC BY 4.0) va [MLDataScientist/Wikipedia-uzbek-2024-05-01](https://huggingface.co/datasets/MLDataScientist/Wikipedia-uzbek-2024-05-01) to‘plamlaridan tasodifiy namuna (jami ~4,1 mln so‘z).
- Yangi alifbo: [gov.uz xabari, 21.10.2026](https://gov.uz/en/yoshlar/news/view/246056).
- Tamoyillar: Vikipediyadagi ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

Muallif: Anvar Zarifov.
