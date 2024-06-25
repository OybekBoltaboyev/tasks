mahsulotlar=['guruch', 'sabzi','yog\'', 'un', 'kartoshka','piyoz','go\'sht','pomidor','xurmo','suv']
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
print("Savat uchun 5 ta mahsulot yozing.")
for mahsulot in range(5):
    mahsulot=input(f"{mahsulot+1}-mahsulot: -->")
    savat.append(mahsulot)

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print(f"Quyidagi mahsulotlar do'konimizda yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")