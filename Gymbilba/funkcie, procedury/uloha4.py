from random import randint

p1 = [randint(1,100) for _ in range(int(input("Veľkosť prvého poľa: ")))]
p2 = [randint(1,100) for _ in range(int(input("Veľkosť druhého poľa: ")))]

def spoj_polia(pole1, pole2):
    pole1.sort()
    pole2.sort()
    vys = pole2
    print(f"{pole1}\n{pole2}")

    for i in range(len(pole1)):
        for j in range(len(pole2)-1):
            if pole1[i] > pole2[j] and pole1[i] < pole2[j+1]:
                vys.insert(j+1, pole1[i])
        if pole1[i] > pole2[-1]:
            vys.insert(len(vys), pole1[i])
        if pole1[i] < pole2[0]:
            vys.insert(0, pole1[i])
    return vys

print(spoj_polia(p1,p2))