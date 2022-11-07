from tkinter import *

root = Tk()
root.title("Uloha 2")

c = Canvas(root, width="500", height="500")
c.pack()

for i in range(10):
    c.create_oval(100 - i * 10, 100 - i * 10, 150 + i * 10, 150 + i * 10)

root.mainloop()