from tkinter import *
import random, time

root = Tk()

c = Canvas(root, width="500", height="500")
c.pack()

inp = Entry(root)
c.create_window(70, 20, window=inp)

def three_dim_text():
    txt = inp.get()
    if txt != "":
        for i in range(5):    
            #text = Label(text="test", font=("Arial", 15 + i*5), fg=(("grey" * (i < 4)) + ("blue" * (i == 4))))
            #c.create_window( window=text)
            c.create_text(100 - i, 200 + i, text=txt, font="Arial 20", fill=("grey" * (i < 4)) + ("blue" * (i == 4)))

button1 = Button(text='Draw text', command=three_dim_text)
c.create_window(50, 50, window=button1)

root.mainloop()