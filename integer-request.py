son=int(input("Biror butun son kiriting."))
sonlar=list(range(2,10))
for n in sonlar:
    if not son%n:
        print(f"{son} {n} ga qoldiqsiz bo'linadi.")