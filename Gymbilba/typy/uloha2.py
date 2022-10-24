#skok do dialky, nahodna diskvalifikacia -->
import random, math
from traceback import print_tb

def generuj_meno() -> list:
    meno_f, meno_m = ["Ema", "Nina", "Sofia", "Eliška", "Viktória", "Sára", "Natália", "Nela", "Mia", "Hana"], ["Jakub", "Adam", 'Samuel', 'Michal', 'Oliver', 'Tomáš', 'Filip', 'Matej', 'Lukáš', 'Martin']
    priezvisko_f, priezvisko_m  = ['Horváthová', 'Kováčová', 'Vargová', 'Tóthová', 'Nagyová', 'Balážová', 'Molnárová', 'Balogová', 'Lukáčová', 'Nováková'], ['Horváth', 'Kováč', 'Varga', 'Tóth', 'Nagy', 'Baláž', 'Szabó', 'Molnár', 'Balog', 'Kovács']
    pohlavie = random.randint(0,1)
    meno = random.choice(meno_f) if pohlavie == 1 else random.choice(meno_m)
    priezvisko = random.choice(priezvisko_f) if pohlavie == 1 else random.choice(priezvisko_m)
    return [meno, priezvisko]

class Skokan:
    def __init__(self, meno, priezvisko, dlzka_skoku):
        self.meno = meno
        self.priezvisko = priezvisko
        self.dlzka_skoku = dlzka_skoku

skokani = list()       

for i in range(5):
    meno = generuj_meno()
    skokan = Skokan(meno[0], meno[1], 0.0)
    skokani.append(skokan)

def vytried_tabulku(tab):
    for _ in range(math.factorial(len(tab) - 1)):
        for i in range(len(tab) - 1):
            if tab[i].dlzka_skoku < tab[i+1].dlzka_skoku:
                tab[i], tab[i+1] = tab[i+1], tab[i]
    return tab

tabulka = skokani.copy()

#1. kolo
for i in range(len(skokani)):
    skokani[i].dlzka_skoku = float(input(f"Napis dlzku skoku v metroch pre {i+1}. skokana: "))
    tabulka = vytried_tabulku(tabulka)
    for clovek in tabulka:
        print(f"{tabulka.index(clovek) + 1}. {clovek.meno} {clovek.priezvisko} ({skokani.index(clovek) + 1}) {clovek.dlzka_skoku}m")
        
#2. kolo
print("\nDruhe kolo: \n")
for i in range(len(skokani)):
    skok = float(input(f"Napis dlzku skoku v metroch pre {i+1}. skokana: "))
    skokani[i].dlzka_skoku = skokani[i].dlzka_skoku if skokani[i].dlzka_skoku > skok else skok
    tabulka = vytried_tabulku(tabulka)
    for clovek in tabulka:
        print(f"{tabulka.index(clovek) + 1}. {clovek.meno} {clovek.priezvisko} ({skokani.index(clovek) + 1}) {clovek.dlzka_skoku}m")

doping = random.choice(skokani)

print(f"\nDopoval {doping.meno} {doping.priezvisko}, bude diskvalifikovany")

tabulka.pop(tabulka.index(doping))
tabulka = vytried_tabulku(tabulka)

for clovek in tabulka:
    print(f"{tabulka.index(clovek) + 1}. {clovek.meno} {clovek.priezvisko} ({skokani.index(clovek) + 1}) {clovek.dlzka_skoku}m")
