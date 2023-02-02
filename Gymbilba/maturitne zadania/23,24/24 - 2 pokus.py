from tkinter import *

root = Tk()

c = Canvas(width=500, height=500, master=root)
c.pack()

mapa = [list(map(int, line.strip().split(" "))) for line in open("mapa.txt", "r")]
stripped = []
for line in mapa:
    stripped += line
size = 10
print(stripped)
for index, tile in enumerate(stripped):
    if tile == 0:
        c.create_rectangle(size * index,index // 10 * size, size + size * index,size + index // 10 * size, fill="blue")
    else:
        c.create_rectangle(size * index,index // 10 * size, size + size * index,size + index // 10 * size, fill="green")

islands = {}
for tile in stripped:
    if tile != 0:
        if tile not in islands.keys():
            islands[tile] = stripped.count(tile)
print(f"Pocet ostrovov: {len(islands.keys())}")
print(f"Velkost najvacsieho ostrova: {max(islands.values())}")

root.mainloop()