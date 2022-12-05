lines = [line.strip().replace(",", ".").split(" ") for line in open("meteo_stanice.txt", "r").readlines()]

print(len(lines))
print(" ".join([line[3] for line in lines]))
vsetky_teploty = [float(line[3][1:]) if line[3][0] == "+" else -1 * float(line[3][1:]) for line in lines]
print(vsetky_teploty)
najvyssia_teplota = max(vsetky_teploty)
print(najvyssia_teplota)
print(lines[vsetky_teploty.index(najvyssia_teplota)][0])
print(round(sum(vsetky_teploty) / len(vsetky_teploty), 2))