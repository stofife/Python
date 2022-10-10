from random import sample

effectivness = 0
for i in range(10):
    pole = sample(range(1,100000), 10000)
    #print (pole)

    iterations = 0
    cislo = sample(pole, 1)[0]

    for num in pole:
        if num == cislo:
            print(f"Cislo sa v poli nachadza na indexe {pole.index(num)}")
            print(f"Preslo {iterations} opakovani.")
            break
        iterations += 1
    temp = iterations
    pole.sort()
    print(pole)
    iterations = 0
    while True:
        if cislo > pole[len(pole) // 2]:
            pole = pole[(len(pole) // 2):]
        elif pole[len(pole) // 2] == cislo:
            print(f"Cislo sa nachadza na indexe {pole.index(cislo)}")
            print(f"Preslo {iterations} opakovani")
            break
        else:
            pole = pole[0:(len(pole) // 2)]
        iterations += 1
    effectivness += temp / iterations

print(f"Efektivita polenia je {effectivness / 10}x rychlejsia")