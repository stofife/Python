from tkinter import *
import random
root = Tk()

w, h = 1000, 500
c = Canvas(root, width=w, height=h)
c.pack()

auta = []
for i in range(4):
    auta.append([c.create_rectangle(0,0 + (i+1) * 100,100,50  + (i+1) * 100, fill="".join(["#"]+[random.choice([str(i) for i in range(0,10)]+[chr(i) for i in range(97, 103)]) for _ in range(6)])), c.create_oval(0,40  + (i+1) * 100,25,65  + (i+1) * 100, fill="grey"), c.create_oval(75,40  + (i+1) * 100,100,65  + (i+1) * 100, fill="grey")])


def posun_auta():
    for auto in auta:
        vel = random.randint(20,50)
        for part in auto:
            c.move(part, vel, 0)
        print(c.coords(auto[0]))
        if c.coords(auto[0])[0] > w:
            for i in range(len(auta)):
                if c.coords(auto[0])[1] == i * 100:
                    won = f"Car {i}" 
            win = Label(text=won + " won")
            c.create_window(100,200, window=win)
            return
    root.after(100, posun_auta)
        

root.after(100, posun_auta)
root.mainloop()