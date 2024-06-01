'''buyurtma="Buyurtmalaringiz ro'yxatini shakllantiruvchi dastur. "
mahsulotlar=[]
n=1
while True:
    buyurtma=f"{n}-buyurtmani bering: "
    mahsulot=input(buyurtma)
    mahsulotlar.append(mahsulot)
    javob=input("Yana qoshasizmi (ha \ yo'q): ")
    if javob=='ha':
        n+=1
        continue
    else:
        break
print("Ro'yxat tuzildi.")
for mahsulot in mahsulotlar:
    print(mahsulot.title())'''

print("Mahsulotlar va ularning narxlari ro'yxatini shakllantiruvchi dastur.")
e_bozor={}
ishora = True
while ishora:
    mahsulot=input("mahsulot kiriting: ")
    narx=input(f"{mahsulot}ning narxini kiriting: ")
    e_bozor[mahsulot]=int(narx)
    javob= input("Yana ma'lumot qo'shasizmi?(ha\yo'q)")
    if not javob=='ha':
        ishora=False

print(e_bozor)











