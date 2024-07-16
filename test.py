# oylar = {
#     "yanvar": "01",
#     "fevral": "02",
#     "mart": "03",
#     "aprel": "04",
#     "may": "05",
#     "iyun": "06",
#     "iyul": "07",
#     "avgust": "08",
#     "sentabr": "09",
#     "oktabr": "10",
#     "noyabr": "11",
#     "dekabr": "12",
# }


# def tugulgan(sana):
#     bloklar = sana.split()

#     if len(bloklar) != 3:
#         return "noto`g`ri ishlatilindi"

#     kun, oy, yil = bloklar
#     print(yil, type(yil))
#     try:
#         kun = int(kun)
#         if kun < 1 or kun > 31:
#             return "sanalar noto`g`ri kiritildi"
#         kun = str(kun).zfill(2)
#     except ValueError as e:
#         return f"error{e}"

#     oy = oy.lower()

#     if oy not in oylar:
#         return "noto`g`ri oy"

#     oy_raqami = oylar[oy]
#     # yil = int(yil)
#     if not yil.isdigit() or len(yil) != 4:
#         return "yil xato"

#     return f"{kun}.{oy_raqami}.{yil}"


# sana = input("Tug'ilgan kuningizni kiriting (masalan, 5 may 2004): ")
# natija = tugulgan(sana)
# print("Natija:", natija)
import re

# Oylarni songa aylantirish uchun lug'at
oylar = {
    "yanvar": "01",
    "fevral": "02",
    "mart": "03",
    "aprel": "04",
    "may": "05",
    "iyun": "06",
    "iyul": "07",
    "avgust": "08",
    "sentabr": "09",
    "oktabr": "10",
    "noyabr": "11",
    "dekabr": "12",
}


def tugilgan_kun_formatini_ozgartir(sana):
    # Regular expression yordamida sanani ajratib olish
    pattern = r"(\d{1,2})\s+(\w+)\s+(\d{4})"
    match = re.search(pattern, sana)

    if match:
        kun, oy, yil = match.groups()

        # Oyni songa aylantirish
        oy_raqami = oylar.get(oy.lower())

        if oy_raqami:
            # Kunni ikki xonali qilish
            kun = kun.zfill(2)

            # Yangi formatdagi sanani qaytarish
            return f"{kun}.{oy_raqami}.{yil}"

    return "Noto'g'ri format"


# Dasturni sinab ko'rish
sana = input("Tug'ilgan kuningizni kiriting (masalan, 05 may 2004): ")
natija = tugilgan_kun_formatini_ozgartir(sana)
print("Natija:", natija)
