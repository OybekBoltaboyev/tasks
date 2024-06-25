print("2 ta son kiriting.")
sonlar=[]
for son in range(2):
    son=int(input(f"{son+1}-son \n--> "))
    sonlar.append(son)
if sonlar[0]>sonlar[1]:
    print(f"{sonlar[0]} katta.")
elif sonlar[1]>sonlar[0]:
    print(f"{sonlar[1]} katta")
else:
    print("Sonlar teng")