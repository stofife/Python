from tkinter import *

root = Tk()

c = Canvas(width=800, height=600, master=root)
c.pack()

with open("vytazenost_autobusovej_linky.txt") as f:
    lines = [line.strip() for line in f]
global ppl, c_stop, cap  
cap = int(lines[0])
ppl = 0
c_stop = 0
stops = lines[1:]

def draw_stop(e) -> None:
    global ppl, c_stop, cap
    stop = stops[c_stop].split(" ")
    print(f"Nastupilo: {int(stop[0])}\nVystupilo: {int(stop[1])}")
    ppl += int(stop[0]) - int(stop[1])
    print(ppl)
    print("Size: ", ppl / cap)
    c.create_text(100, 100 + c_stop * 50, text=stop[2])
    if ppl != 0:
        c.create_rectangle(160, 100 + c_stop * 50, 360, 140 + c_stop * 50)
        if ppl > cap:
            c.create_rectangle(160, 100 + c_stop * 50, 160 + 200 * (ppl / cap), 140 + c_stop * 50, outline=None, fill="red")
        else:
            c.create_rectangle(160, 100 + c_stop * 50, 160 + 200 * (ppl / cap), 140 + c_stop * 50, outline=None, fill="green")
    print("kokot????")
    c_stop += 1

root.bind("<space>", func=draw_stop)

root.mainloop()
