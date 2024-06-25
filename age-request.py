yosh=int(input("Yoshingizni kiriting.\n--> "))
if yosh<4 or yosh>60:
    print("Chipta bepul.")
elif yosh<18:
    print("Chipta narxi 10000 so'm")
else:
    print("Chipta narxi 20000 so'm")