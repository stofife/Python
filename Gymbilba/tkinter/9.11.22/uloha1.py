from tkinter import *

root = Tk()
root.title("Uloha 2")

c = Canvas(root, width="500", height="500")
c.pack()

inp = Entry(root)
c.create_window(70, 20, window=inp)
circle = None

def draw_circle():
    r = inp.get()
    if r != "":
        r = int(r)
        circle = c.create_oval(150 - r, 120 - r, 150 + r, 120 + r)

button1 = Button(text='Draw circle', command=draw_circle)
c.create_window(50, 50, window=button1)

root.mainloop()
