from tkinter import *
from random import sample

root = Tk()

c = Canvas(root, width=800, height=600, bg="white")
c.pack()

delete = []

def vykresli():
    f = [line.strip().split(";") for line in open("zasadaci_poriadok.txt").readlines()]
    if delete != []:
        for item in delete:
            c.delete(item)
    r, l = int(rady.get()), int(lavice.get())
    if r*l < len(f):
        delete.append(c.create_text(350, 250, text="MATE MALO LAVIC!!!!", fill="red"))
    else:
        for i in range(l):
            for j in range(r):
                delete.append(c.create_rectangle(20 + j * 110, 10 + i * 70, 120 + j * 110, 70 + i * 70))
                if (i+1) * j < len(f):
                    delete.append(c.create_text(20 + j * 110 + 50, 10 + i * 70 + 20, text=sample(f, 1)[0][0], fill="red"))
                    delete.append(c.create_text(20 + j * 110 + 50, 10 + i * 70 + 40, text=sample(f, 1)[0][1], fill="blue"))
        
c.create_rectangle(0, 450, 800, 600, fill="#ededf0", width=0)
rady = Entry(root)
c.create_window(380, 500, window=rady)
lavice = Entry(root)
c.create_window(380, 550, window=lavice)
potvrd = Button(root, text="Potvrd vstup", command=vykresli)
c.create_window(380, 580, window=potvrd)
c.create_text(380, 480, text="Pocet radov:")
c.create_text(380, 525, text="Lavic v rade:")

root.mainloop()
