f = open("smsky.txt", "r")
f1 = open("vypadli.txt", "r")

vypadli = []

for line in f1.readlines():
    line = int(line)
    vypadli.append(line)

print(vypadli)

hlasy = {}

for line in f.readlines():
    line = int(line)
    if not line in vypadli:
        if not line in hlasy.keys():
            hlasy[line] = 1
        else:
            hlasy[line] += 1
            
print("Celkove pocty hlasov:")
for sutaziaci in hlasy.keys():
    print(f"{int(str(sutaziaci)[-1]) + 1}. sutaziaci: {hlasy[sutaziaci]} hlasov")

print(f"Vypadava sutaziaci cislo {int(str(list(hlasy.keys())[list(hlasy.values()).index(min(list(hlasy.values())))])[-1]) + 1}. s poctom hlasov {min(list(hlasy.values()))}.")
print(hlasy) 
    