'''cars=[
    'toyota','mazda', 'hyundai', 'gm', 'kia'
]
for car in cars:
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())'''
'''
ism=input("Ismingizni kiriting.\n>>> ")
if ism.title()=="Admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {ism.title()}")
'''
'''
sonlar=[]
for son in range(2):
    son=int(input(f"{son+1}-sonni kiriting:\n--> "))
    sonlar.append(son)
if sonlar[0]==sonlar[1]:
    print("Sonlar teng.")

'''


son=int(input("istalgan sonni kiriting. \n-->"))
if son%2==1:
    print("Toq son")
else:
    print("Juft son")

