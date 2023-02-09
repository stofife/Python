from tkinter import *

root = Tk()

c = Canvas(width=800, height=600, master=root)
c.pack()

inp = [line.strip() for line in open("trasa_linky_metra.txt").readlines()]
color = inp[0]
line = c.create_line(100, 300, 720, 300, width=4, fill=color)
c.create_rectangle(720, 290, 740, 310, outline=color, fill=color)
c.create_rectangle(90, 290, 110, 310, outline=color, fill=color)
linka_metra = inp[1:]

for i, z in enumerate(linka_metra[1:-1]):
    pos = (600 // len(linka_metra[1:-1])) * (i + 1)
    if z[0] == "*":
        c.create_oval(100 + pos, 290, 120 + pos, 310, outline=color, fill="white")
    else:
        c.create_oval(100 + pos, 290, 120 + pos, 310, outline=color, fill=color)

for i,z in enumerate(linka_metra):
    pos = (600 // len(linka_metra[1:])) * (i + 1)
    c.create_text(80 + pos, 280, text=z, anchor="nw", angle=45)

root.mainloop()