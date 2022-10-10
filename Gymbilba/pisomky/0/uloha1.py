inp = int(input("Zadaj číslo:"))
cifra = 0
suc = 0
while inp > 0:
    print(inp)
    cifra = inp % 10
    if cifra % 2 != 0:
        suc = suc + cifra
    inp = inp // 10
print("Sucet neparnych cifier je " + str(suc))