from tkinter import *

root = Tk()

c = Canvas(root, width="480", height="520")
c.pack()

hlasy = [line.strip().split(" ") for line in open("spokojnost_1.txt", "r")]
nes_zak = [hlas[0].split(":")[0] for hlas in hlasy if hlas[1] == 'nie']
print(f"Pocet nespokojnych zakaznikov: {len(nes_zak)}")

hodiny = [int(zak.split(":")[0]) if zak.split(":")[0][0] != "0" else int(zak.split(":")[0][1]) for zak in nes_zak]
max = 0
for i in range(24):
    if hodiny.count(i) > max:
        max = hodiny.count(i)
        max_index = i
    if hodiny.count(i) != 0:
        print(f"{i}: {hodiny.count(i)}")

print(f"Najviac nesp. zakaznikov o {max_index}-tej, pocet: {max}")
    
for i in range(24):
    c.create_text(10 + 20 * i, 510, text=[str(i) if i > 9 else f"0{i}"][0])
    c.create_line(12 + 20 * i, 500, 12 + 20 * i, 500 - hodiny.count(i) * 50, width=18, fill="red")

root.mainloop()