# Kabisa yilini aniqlash
year = int(input("Yilni kiriting: "))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} yil kabisa yili.")
else:
    print(f"{year} yil kabisa yili EMAS.")
