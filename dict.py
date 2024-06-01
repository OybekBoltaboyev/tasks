'''otam={'t-yil':1982, 't-joy':'Turkmaniston', 'manzili':'Shovot'}
onam={'t-yil':1980, 't-joy':'O\'zbekiston', 'manzili':'Shovot'}
ukam={'t-yil':2007, 't-joy':"O'zbekiston", 'manzili':'Shovot'}
oila=[onam,otam,ukam]
for i in oila:
    print(f"Tug'ilgan yili {i['t-yil']}, tug'ilgan joyi {i['t-joy']}, yashash manzili {i['manzili']}")'''
'''
taom={'otam':'baliq', 'onam':'kurtik', 'ukam':'shashlik', 'singlim':'barak', "o'zim":"lag'mon"}
print(taom['otam'], taom['onam'], taom['ukam'])'''

'''atamalar={'dict':'lug\'at', 'set':'to\'plam', 'get':'bo\'lmoq', 'string':'zanjir', 'integer':'butun son', 'float':'suzish (bu yerda o\'nli kasrni nuqtasiga urg\'u berilgan', 'if':'agar', 'else':'aks holda', 'variable':'o\'zgaruvchi', 'print':'chop qilish'}
atama=input("Atamani so'rang: ")
print(atamalar.get(atama, "Bunday so'z mavjud emas"))
atama=atamalar.get('atama', 'Bunday so\'z mavjud emas')'''

'''
lugat = { 'dict':'lug\'at', 'set':'to\'plam', 'get':'bo\'lmoq', 'string':'zanjir', 'integer':'butun son', 'float':'suzish (bu yerda o\'nli kasrni nuqtasiga urg\'u berilgan', 'if':'agar', 'else':'aks holda', 'variable':'o\'zgaruvchi', 'print':'chop qilish'}
for key, value in sorted(lugat.items()):
    print(f"{key.title()}-{value}")'''

'''davlatlar={'O\'zbekistan':'Toshkent',
           'Turkiya':'Anqara',
           'Qozog\'iston':'Ostona',
           'Turkmaniston':'Ashxobod',
           'Afg\'oniston':'Kobul', }

print(sorted(davlatlar.keys()))
print(sorted(davlatlar.values()))

davlat=input("Poytaxtini bilmoqchi bo'lgan davlatingizni kiriting: ")
if davlat.title() in davlatlar.keys():
    print(f"{davlat.title()}-{davlatlar[davlat.title()]}")
else:
    print("Bizda bunday ma'lumot yo'q")'''

menu={'osh':20000, 'manti':25000, 'lag\'mon':18000, 'chuchvara':23000, 'somsa':15000, 'gumma':10000, 'norin':13000, 'lavash':24000, 'doner':12000, 'unoshi':19000}
request=[]
print("3 ta buyurtma ber ")
for n in range(3):
    request.append(input(f"{n+1}- taom: ").lower())

for buyurtma in request:
    if buyurtma in menu:
        print(f"{buyurtma}ning narxi {menu[buyurtma]}")
    else:
        print(f"{buyurtma} haqida bizda ma'lumot yo'q")
