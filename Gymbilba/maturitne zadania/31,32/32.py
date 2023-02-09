with open("skoky.txt", "r") as f:
    f = f.readlines()
    lines = [line.strip().split(" ") for line in f]

skokani = [[line[0], list(map(int, line[1:]))] for line in lines]
[line[1].sort(reverse=True) for line in skokani]
skokani.sort(key=lambda x: x[1][0], reverse=True)
print(f"Zvitazil pretekar s cislom {skokani[0][0]} s dlzkou skoku {skokani[0][1][0]}cm.")