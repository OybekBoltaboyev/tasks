foydalanuvchilar=['ali', 'usmon', 'hasan','husayyin']
foydalanuvchi=input("Login kiriting!\n-->")
if foydalanuvchi in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {foydalanuvchi}")