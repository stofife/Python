import math


class Film:
    def __init__(self, nazov, hlv_pos, navs) -> None:
        self.nazov, self.hlv_pos, self.navs = nazov, hlv_pos, navs

filmy = []
#Titanic;Leonardo Dicaprio;11726 5478 8213 8563
#Shrek;Shrek;10000 2563 12356 7894
#Shrek 2;Shrek;10000 2563 12356 7894
#Shrek 3;Shrek;1005 2533 18956 7594
#Shrek 4: Zvonec a konec;Shrek;1563 5465 7846 1262
def celkova_navstevnost():
    for film in filmy:
        print(f"{film.nazov}: {sum(film.navs)}")

def utried():
    for _ in range(math.factorial(len(filmy) - 1)):
        for i in range(len(filmy)-1):
            if sum(filmy[i].navs) < sum(filmy[i+1].navs):
                filmy[i], filmy[i+1] = filmy[i+1], filmy[i]
    
def vypis(n):
    for i in range(n):
        print(f"{i+1}. {filmy[i].nazov}: {sum(filmy[i].navs)} navstevnikov")
                
def pocet_filmov(koho = str):
    for film in filmy:
        if koho == film.hlv_pos:
            print(film.nazov)
    

while True:
    inp = input("Na ukoncenie zadavania stlac |E|\nZadaj film: ")
    if inp != "e":
        inp = inp.split(";")
        navs = inp[2].split(" ")
        for i in range(len(navs)):
            navs[i] = int(navs[i])
        film = Film(inp[0], inp[1], navs)
        filmy.append(film)
    else: break

celkova_navstevnost()
utried()
vypis(3)
pocet_filmov("Shrek")