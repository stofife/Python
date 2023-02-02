from tkinter import *
from random import randint

root = Tk()

c = Canvas(width=900, height=200, master=root)
c.pack()

menu = randint(0,8)
c.create_rectangle(40 + menu * 100,40,60 + menu * 100,80, fill="green")
out_str = ""
textbox = c.create_text(400, 150, font="Arial 20",text=out_str)

def clicked(event):
    print(f"clicked a plate, pos: {event.x // 100}")
    print(event)
    pos = event.x // 100
    if pos > menu:
        c.itemconfig(textbox, text="<---")
    elif pos < menu:
        c.itemconfig(textbox, text="--->")
    else:
        print("Vyhral si!")
        root.quit()
        
def draw_plates():
    for w in range(9):
        c.create_oval(0 + w * 100, 0, 100 + w * 100, 100, fill="lightblue", width=5, tags="plate")
        c.create_oval(25 + w * 100, 25, 75 + w * 100, 75, width=5)
    c.tag_bind("plate","<Button-1>",clicked)
c.after(500, draw_plates)

root.mainloop()