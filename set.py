'''ranglar={'sariq', 'qizil', 'yashil'}
ranglar.add('oq')
ranglar.update(['qora', 'ko\'k'])
print(sorted(ranglar))
'''

'''set1={10,20,30,40,50}
set2={30,40,50,60,70}
set3=set1.symmetric_difference(set2)
print(set3)
'''

'''bozorlik={'choy','non','kartoshka', 'tuxum','sut'} # siz sotib olishingiz kerak bo'lgan mahsulotlar
mahsulotlar={'non','sut','olma', 'un', 'tuxum', 'tuz'} # do'kondagi mavjud mahsulotlar
bor=bozorlik.intersection(mahsulotlar)
mavjudmas=bozorlik.difference(mahsulotlar)
mahsulotlar.update(mavjudmas)
print(mahsulotlar)'''


'''shaxs1={'ismi':'Alisher Navoiy', 'kasbi':'adib', 't-yili':'1441', 't-joyi':'Hirot'}
shaxs2={'ismi':'Muhammad Muso Al-Xorazmiy', 'kasbi':'matematik', 't-yili':'983', 't-joyi':'Xorazm'}
shaxs3={'ismi':'Anvar', 'kasbi':'dasturchi', 't-yili':'1983', 't-joyi':'Toshkent'}
shaxs4={'ismi':'Muhammadali', 'kasbi':'biznes-trener', 't-yili':'1991', 't-joyi':'Jizzax'}
shaxslar=[shaxs4,shaxs3, shaxs2, shaxs1]
shaxs1.append({'asari':'Xamsa'})
shaxs2.append({'asari':'Al-Jabr val-muqobala'})
shaxs3.append({'asari':'pyton dasturlash asoslari'})
shaxs1.append({'asari':'Yuksalish'})
for shaxs in shaxslar:
    print(f"{shaxs['ismi']},  "
          f"{shaxs['kasbi']}, "
          f"{shaxs['asari']}"
          f"{shaxs['t-yili']}-yil {shaxs['t-joyi']}da tug'ilgan, ")'''

davlatlar={
    'O\'zbekiston':{'poytaxti':'Toshkent', 'joylashgan mintaqasi':'Markaziy Osiyo', },
    'Turkiya':{'poytaxti':'Anqara','joylashgan mintaqasi':'G\'arbiy Osiyo'},
    'Qozog\'iston':{'poytaxti':'Ostona','joylashgan mintaqasi':'Markaziy Osiyo'}
}
davlat=input("davlat kirit: ")
davlat=davlatlar.get(davlat, 'Bizda bu davlat haqida ma\'lumot yo\'q.')
print(davlat)

