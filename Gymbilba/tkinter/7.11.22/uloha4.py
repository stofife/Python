from tkinter import *

root = Tk()
root.title("Uloha 2")

c = Canvas(root, width="500", height="500")
c.pack()

c.create_rectangle(100, 50, 200, 400, fill="grey")
c.create_oval(110, 60, 190, 140, fill="red")
c.create_oval(110, 160, 190, 240, fill="orange")
c.create_oval(110, 260, 190, 340, fill="green")

root.mainloop()