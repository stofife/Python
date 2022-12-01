import tkinter
root = tkinter.Tk()
c = tkinter.Canvas(root, width="700", height="600")
c.pack()
coords = [list(map(int, line.strip().split(" "))) for line in open("sr.txt", "r").readlines()]
sneh = [line.strip() for line in open("sneh.txt", "r").readlines()]
globals().update(n = 0)

def show_info():
    c.delete("all")
    for x,y in coords:
        c.create_line(x, y, x+1, y)
    stredisko = sneh[n].split(" ")
    c.create_oval(int(stredisko[0]), int(stredisko[1]) - 100, int(stredisko[0]) + 10, int(stredisko[1]) + 10 - 100, fill="red") 
    c.create_text(150, 350, text=" ".join(sneh[n].split(" ")[2:]))
    globals().update(n = n + 1)

root.bind("<space>", lambda _: show_info())
root.mainloop()