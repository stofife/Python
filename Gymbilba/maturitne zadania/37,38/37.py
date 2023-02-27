with open("pacienti.txt") as f:
    lines = [line.strip() for line in f.readlines()]

print(lines)

ppl = [line.split(" ") for line in lines]

ter_vahy = []
for p in ppl:
    ter_vahy.append(float(input(f"Terajsia vaha {p[0]}: ")))

print(ter_vahy)
zeny = []
obezita = []
for i, vaha in enumerate(ter_vahy):
    ppl[i][2] = vaha / (float(ppl[i][3].replace(",", "."))**2)
    bmi = ppl[i][2]
    print(ppl[i])
    if ppl[i][0][-2:] == "vá" and bmi < 18.5:
        zeny.append(ppl[i])
    if bmi > 30:
        obezita.append(ppl[i])

print(obezita, zeny)