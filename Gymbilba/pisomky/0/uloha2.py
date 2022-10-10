import random

suc = [1,2,3,4,5,6,7,8,9,10]
inp = int(input("Pocet prikladov: "))
spravne = 0
for i in range(inp):
    suc1 = suc[random.randint(0, len(suc)-1)]
    suc2 = suc[random.randint(0, len(suc)-1)]
    print(f"Priklad {i+1}: {suc1} * {suc2} = ?")
    vys = int(input("?: "))
    if vys == suc1*suc2:
        spravne += 1
print(f"Uspesnost: {spravne / inp * 100}%")
    