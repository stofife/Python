from tkinter import *

root = Tk()
root.title("Uloha 5")

c = Canvas(root, width="500", height="500")
c.pack()

for i in range(1,6):
    c.create_rectangle(100 + (i - 1 * 20), 400, 100 + i * 20, 400 + i * 20)

root.mainloop()