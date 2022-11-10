from tkinter import *
root = Tk()

c = Canvas(root, width="500", height="500")
c.pack()

auto = [c.create_rectangle(0,0,100,50, fill="blue"), c.create_oval(0,40,25,65, fill="grey"), c.create_oval(75,40,100,65, fill="grey")]

def posun_auto():
    for part in auto:
        c.move(part, 50, 0)
    print(c.coords(auto[0]))
    if c.coords(auto[0])[0] > 500:
        for part in auto:
            c.move(part, -600,0)
    root.after(100, posun_auto)
        

root.after(100, posun_auto)
root.mainloop()