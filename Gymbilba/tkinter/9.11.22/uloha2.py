from tkinter import *
import random, time

root = Tk()

def get_hex_color():
    return "".join(["#"]+[random.choice([str(i) for i in range(0,10)]+[chr(i) for i in range(97, 103)]) for _ in range(6)])

c = Canvas(root, width="500", height="500")
c.pack()

while True:
    offset, size = [random.randint(1, 500), random.randint(1, 500)], random.randint(10, 500)
    c.create_oval(0 + offset[0], 0 + offset[1], size + offset[0], size + offset[1], fill=get_hex_color())
    root.update()
    #time.sleep(0.2)