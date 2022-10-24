import random

ziak = {
    "meno": str,
    "priezvisko": str,
    "priemer": float, 
}

def generuj_meno() -> list:
    meno_f, meno_m = ["Ema", "Nina", "Sofia", "Eliška", "Viktória", "Sára", "Natália", "Nela", "Mia", "Hana"], ["Jakub", "Adam", 'Samuel' 'Michal' 'Oliver' 'Tomáš' 'Filip' 'Matej' 'Lukáš' 'Martin']
    priezvisko_f, priezvisko_m  = ['Horváthová', 'Kováčová', 'Vargová', 'Tóthová', 'Nagyová', 'Balážová', 'Molnárová', 'Balogová', 'Lukáčová', 'Nováková'], ['Horváth' 'Kováč' 'Varga' 'Tóth' 'Nagy' 'Baláž' 'Szabó' 'Molnár' 'Balog' 'Kovács']
    pohlavie = random.randint(0,1)
    meno = random.choice(meno_f) if pohlavie == 1 else random.choice(meno_m)
    priezvisko = random.choice(priezvisko_m) if pohlavie == 1 else random.choice(priezvisko_f)
    return [meno, priezvisko]