stanovistia = [i.strip() for i in open("stanovistia.txt", "r").readlines()]
for sutaziaci in open("pretekari.txt", "r").readlines():
    sutaziaci = sutaziaci.strip().split(" ")
    cislo, cas, stan = sutaziaci[0], sutaziaci[1], sutaziaci[2:]
    vsetky = True
    for s in stanovistia:
        if s not in stan:
            vsetky = False
    print("Sutaziaci cislo " + cislo + " " + (not vsetky) * "ne" + "presiel vsetky stanovistia.")
casy = [float(sutaziaci.strip().split(" ")[0].replace(":", ".")) for sutaziaci in open("pretekari.txt", "r").readlines()]
casy.sort()
for i in range(0, len(casy)):
    print(str(i+1) + ". - " + open("pretekari.txt", "r").readlines()[i].split(" ")[0])