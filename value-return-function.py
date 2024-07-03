# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     "To'liq ism qayatruvchi funksiya"
#     if otasining_ismi:
#         toliq_ism=f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism
# talaba1=toliq_ism_yasa('olim', 'hakimov')
# talaba2=toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
# print(talaba1, talaba2)






# avto1=avto_info('gm','malibu','qora','avtomat',2018)
# avto2=avto_info('gm','gentra','oq','mexanik',2016,15000)
# avtolar=[avto1,avto2]
# print('Bozordagi mavjud avtomobillar: ')
# for avto in avtolar:
#     if avto['narxi']:
#         narx=avto['narxi']
#     else:
#         narx="Noma'lum"
#     print(f"{avto['Rangi'.title()]} {avto['Modeli'.title()]}. Narxi {narx}")

# def oraliq(min, max, qadam=''):
#     sonlar=[]
#     while min<max:
#         if qadam:
#             sonlar.append(min)
#             min=min+int(qadam)
#         else:
#             sonlar.append(min)
#             min+=1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(0,21,2))



# def avto_info(maker, model, rangi, korobka, yili, narxi=None):
#     avto={'kompaniya':maker,
#           'Modeli':model,
#           'Rangi':rangi,
#           'korobka':korobka,
#           'yil':yili,
#           'narxi':narxi}
#     return avto
#
#
# print("Saytimizdagi avtomobillar ro'yxatini shakllantiramiz.")
# avtolar=[]
# while True:
#     print("Quyidagi ma'lumotlarni kiriting:")
#     maker=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narxi: ")
#     avtolar.append(avto_info(maker,model,rangi,korobka,yili,narxi))
#     javob=input("Yana qo'shasizmi? (ha/yo\'q)")
#     if not javob=='ha':
#         break
# for avto in avtolar:
#     print(f"{avto['Rangi'.title()]} {avto['Modeli'.title()]}. Narxi {avto['narxi']}")


# def user_cred(ismi, familiyasi, yili, joyi, emaili='', raqami=''):
#     users={
#         'ismi':ismi,
#         'familiyasi':familiyasi,
#         'tug\'ilgan yili':yili,
#         'yoshi':2024-int(yili),
#         'tug\'ilgan joyi':joyi,
#         "elektron manzili":emaili,
#         'telefon raqami':raqami
#     }
#     return users
# # user1=user_cred('Oybek','boltaboyev', 2004,'shovot','oybekboltaboyev1443@gmail.com','+998935716139')
# # user2=user_cred('hikmat','boltaboyev', 2007,'shovot',)
# # users=[user1,user2]
# # for user in users:
# #     if user['elektron manzili'] and user['telefon raqami']:
# #         print(f"{user['ismi'].title()} {user['familiyasi'].title()}, yoshi {user['yoshi']}. Elektron manzili {user['elektron manzili']} raqami {user['telefon raqami']}")
# #     else:
# #         print(f"{user['ismi'].title()} {user['familiyasi'].title()}, yoshi {user['yoshi']}.")
# mijozlar=[]
# while True:
#     ismi=input("Ismni kiriting: ")
#     familiyasi=input("Familiyani kiriting: ")
#     yili=input("Tug'ilgan yilini kiriting: ")
#     joyi=input("Tug'ilgan joyini kiriting: ")
#     emaili=input("Elektron manzilini kiriting: ")
#     raqami=input("Tlefon raqamini kiriting: ")
#     mijozlar.append(user_cred(ismi,familiyasi,yili,joyi,emaili,raqami))
#     javob=input("Yana qo'shasizmi? (ha\yo\'q)")
#     if javob=='yo\'q':
#         break
# for mijoz in mijozlar:
#     print(f"{mijoz['ismi'].title()} {mijoz['familiyasi'].title()}. Yoshi {mijoz['yoshi']}")

# radius=int(input("Aylananing radiusini kiriting: "))
# def lugat(radius):
#     natija= {
#         'radiusi':radius,
#         "diametri": radius * 2,
#         'perimetri':2*3.14*radius,
#         'yuzi':radius**2*3.14
#     }
#     return natija
# natija=lugat(radius)
#
# print(natija)

# def oraliq(min, max):
#     sonlar=[]
#     min=int(min)
#     max=int(max)
#     for son in range(min,max+1):
#         if son>1:
#             tub=True
#             for i in range(2, son):
#                 if son%i==0:
#                     tub=False
#                     break
#             if tub:
#                 sonlar.append(son)
#     return sonlar
# tubsonlar=oraliq(1,21)
# print(tubsonlar)

def fibonacci_numbers(n):
    sonlar=[]
    x=0
    while x<n:
        if x==0 or x==1:
            sonlar.append(1)
            x+=1
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
            x+=1
    return sonlar

n=fibonacci_numbers(int(input("Son kirit: ")))
print(n)









