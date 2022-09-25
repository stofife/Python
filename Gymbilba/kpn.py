from cgi import print_form
import random
count = int(input("Pocet hier:"))

hrac1 = str
hrac2 = str

moznosti = ["Kamen", "Papier", "Noznice"]

def evaluate(hrac1, hrac2):
    res = int
    if hrac1 == "Kamen":
        if hrac2 == "Kamen":
            res = -1
        if hrac2 == "Noznice":
            res = 0
        if hrac2 == "Papier":
            res = 1
    if hrac1 == "Papier":
        if hrac2 == "Papier":
            res = -1
        if hrac2 == "Kamen":
            res = 0
        if hrac2 == "Noznice":
            res = 1
    if hrac1 == "Noznice":
        if hrac2 == "Noznice":
            res = -1
        if hrac2 == "Papier":
            res = 0
        if hrac2 == "Kamen":
            res = 1
    return res    

score1, score2 = 0, 0

for i in range(0,count):
    hrac1 = moznosti[random.randint(0,2)]
    hrac2 = moznosti[random.randint(0,2)]
    print("Hrac 1 zahral " + hrac1)
    print("Hrac 2 zahral " + hrac2)
    if evaluate(hrac1, hrac2) == -1:
        print("Remiza")
    elif evaluate(hrac1, hrac2) == 0:
        print("Vyhral Hrac 1")
        score1 += 1
    elif evaluate(hrac1, hrac2) == 1:
        print("Vyhral Hrac 2")
        score2 += 1
print("Konecne skore: " + str(score1) + " : " + str(score2))