import os

class Zastavka:
    def __init__(self, nastup, vystup, nazov) -> None:
        self.nastup, self.vystup, self.nazov = nastup, vystup, nazov

linka = []

#10;0;Štúrovo nám.
#5;0;Mestský park
#50;1;Dargovská
#2;0;Nemocnica
#10;3;Bratská
#1;1;Mestský úrad

def zastavky():
    cestujuci = 0
    print("Zoznam zastavok:")
    for i in range(len(linka)):
        cestujuci += linka[i].nastup
        cestujuci -= linka[i].vystup
        print(f"{linka[i].nazov}\nPočet cestujúcich: {cestujuci}")
    print()

def odporuc():
    #dlha > 40; standard > 20 & standard < 40; kratka > 0 & kratka < 20
    max = 0
    cestujuci = 0
    for i in range(len(linka)):
        cestujuci += linka[i].nastup
        cestujuci -= linka[i].vystup
        if cestujuci > max: max = cestujuci
    print("Odporúčam " + (max > 40) * "dlhú" + (max > 20 * max < 40) * "štandardnú" + (max < 20) * "krátku" + " električku :)\n")


def automat():
    print("Zastavky, ktoré budú mať automat:")
    for zastavka in linka: 
        if zastavka.nastup >= 10:
            print(zastavka.nazov)
    print()

def na_znamenie():
    print("Zastavky, ktoré budú na znamenie:")
    for zastavka in linka: 
        if zastavka.nastup < 10 and zastavka.vystup < 10:
            print(zastavka.nazov)
    print()


while True:
    os.system("cls")
    print("Na ukoncenie zadavania stlac |E|")
    for zastavka in linka: 
        print("    ", zastavka.nazov, zastavka.nastup, zastavka.vystup)
    inp = input("Zadaj zastavky: ")
    if inp != "e":
        inp = inp.split(";")
        zas = Zastavka(int(inp[0]), int(inp[1]), inp[2])
        linka.append(zas)
    else: break

zastavky()
odporuc()
automat()
na_znamenie()