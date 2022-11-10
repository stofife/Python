from tkinter import *
import random, time

root = Tk()

def get_hex_color():
    return "".join(["#"]+[random.choice([str(i) for i in range(0,10)]+[chr(i) for i in range(97, 103)]) for _ in range(6)])

c = Canvas(root, width="500", height="500")
c.pack()

for i in range(200):
    c.create_line(0 + i+1, 0, 0 + i+1, 150, fill=get_hex_color())

root.mainloop()