import os

jazyk = "sk"
slovnik = {}

def nacitaj_slovnik(lang):
    f = open("slovnik.txt", "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        lines[lines.index(line)] = line.strip()
    for i in range(0, len(lines), 2):
        if lang == "sk":
            slovnik[lines[i]] = lines[i+1]
        else:
            slovnik[lines[i+1]] = lines[i]

nacitaj_slovnik(jazyk)

last_out = ""

while True:
    os.system("cls")
    print(f"Slovnik\n([j] na zmenu jazyka, momentalne {jazyk})\n([v] na vyhladanie slova)\n([z] na zapisanie noveho slova)\n([u] na ukoncenie programu)")
    if last_out != "": print(f"    {last_out}")
    act = input(f"Co chcete spravit?: ")
    
    if act == "j":
        if jazyk == "sk":
            jazyk = "en"
        else:
            jazyk = "sk"
        nacitaj_slovnik(jazyk)

    elif act == "v":
        nacitaj_slovnik(jazyk)
        inp = input("Zadajte slovo na vyhladanie: ")
        if inp not in slovnik.keys():
            last_out = "Slovo nie je v slovniku, chcete ho pridat?"
        else:
            jz = (jazyk == 'sk') * "anglictiny" + (jazyk == 'en') * "slovenciny"
            last_out = f"Preklad slova {inp} do {jz} je {slovnik[inp]}."

    elif act == "z":
        nacitaj_slovnik(jazyk)
        inp = input("Zadaj nove slovo a jeho preklad oddelene ciarkou a medzerou ([slovo], [preklad]): ").split(", ")
        if not inp[0] in slovnik.keys():
            last_out = f"Novy preklad ({inp[0]} <-> {inp[1]}) bol uspesne zapisany!"
            f = open("slovnik.txt", "a")
            [f.write("\n" + inp[0])] + [f.write("\n" + inp[1])]
            f.close()
        else:
            last_out = "Slovo uz sa v slovniku nachadza!"
        
    elif act == "u":
        break
    
    else:
        last_out = "Prepacte, tento prikaz nepoznam :("
    
f.close()