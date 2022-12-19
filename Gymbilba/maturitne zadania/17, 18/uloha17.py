f = [line.strip().split(" ") for line in open("jedla.txt", "r")]

menu_counts = {}

for p in f:
    if p[1] not in menu_counts.keys():
        menu_counts[p[1]] = 1
    else:
        menu_counts[p[1]] += 1
        
print(len(f))
print("\n".join([f"{key}: {val}" for key, val in menu_counts.items()]))
for menu in menu_counts.keys():
    if menu_counts[menu] < 20:
        print(f"Jedlo {menu} sa bohuzial nebude varit :(")
        ppl = []
        for p in f:
            if p[1] == menu:
                ppl.append(p[0])
        print(f"Stravnici s cislami {', '.join(ppl)} dostanu iny obed.")
