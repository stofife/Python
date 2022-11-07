from tkinter import *

root = Tk()
root.title("Uloha 2")

c = Canvas(root, width="500", height="500")
c.pack()

for i in range(5):
    c.create_rectangle(100 + (i * 20), 400 - (i * 50), 400 - (i * 20), 350 - (i * 50))

root.mainloop()