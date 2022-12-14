from tkinter import *

root = Tk()

c = Canvas(root, width=800, height=600)
c.pack()


f = [line.strip().split(" ") for line in open("zastavba_na_ulici.txt", "r").readlines()]

def vykresli():
    budovy()
    lines = []
    if lines != []:
        for line in lines:        
            c.delete(line)
    offset_s = 0
    height_diff, last_height = int(rozdiel.get()), 0
    for budova in f:
        sirka, vyska = int(budova[0]), int(budova[1])
        if last_height != 0:
            if vyska - last_height > height_diff or vyska - last_height < -1 * height_diff:
                lines.append(c.create_line(20 + offset_s, 400 - last_height, 20 + offset_s, 400 - vyska, width=4, fill="red"))
        offset_s += sirka
        last_height = vyska

def budovy():
    offset_s = 0
    for budova in f:
        sirka, vyska = int(budova[0]), int(budova[1])
        if vyska == 0:
            c.create_rectangle(20 + offset_s, 400, 20 + sirka + offset_s, 400 - vyska, outline="green", width=4)
        else:
            c.create_rectangle(20 + offset_s, 400, 20 + sirka + offset_s, 400 - vyska, fill="grey")
        offset_s += sirka

budovy()
rozdiel = Entry(root) 
c.create_window(350, 500, window=rozdiel)
vykresli_button = Button(root, command=vykresli)
c.create_window(380, 550, window=vykresli_button)

root.mainloop()
