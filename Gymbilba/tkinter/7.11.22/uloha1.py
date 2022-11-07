from tkinter import *

root = Tk()
root.title("")

c = Canvas(root, bg="blue", height=900, width=1600)

c.create_rectangle(50, 50, 250, 250)
c.create_rectangle(75, 75, 225, 225)
c.create_rectangle(100, 100, 200, 200, width="5")
c.create_rectangle(125, 125, 175, 175)
c.create_rectangle(137, 137, 162, 162)

c.pack()
root.mainloop()