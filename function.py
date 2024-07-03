def yil_top(ism, yosh):
    """Foydalanuvchidan ismi va yoshini hisoblab,
    uni konsolga chiqaruvchi funksiya!
    """
    print(f"{ism.title()}ning tug'ilgan yili {2024 - int(yosh)}ga teng")

def son_ber(x):
    x=int(x)
    sonlar=[]
    for y in list(range(2,10)):
        if x%y==0:
            print(f"{x} soni {y} ga qoldiqsiz bo'linadi! ")
son_ber(16)