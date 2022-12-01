import tkinter, random
root = tkinter.Tk()
c = tkinter.Canvas(root, width="1000", height="700")
c.pack()

zatoka = [list(map(int, line.strip().split(" "))) for line in open("lodicky.txt").readlines()][1:]
for i in range(len(zatoka)):
    for j in range(len(zatoka[i])):
        if int(zatoka[i][j]) == 1: 
            c.create_rectangle(j*100, i*100, j*100 + 100, i*100 + 100, fill="green")
        else:
            c.create_rectangle(j*100, i*100, j*100 + 100, i*100 + 100, fill="blue")

def new_ship():
    for y in range(7):
        for x in range(8): 
            if (zatoka[y][x] == 0 and zatoka[y][x+1] == 0 and zatoka[y][x+2] == 0) and zatoka[y][x-1] != "x":   
                c.create_rectangle(x*100, y*100, x*100 + 300, y*100 + 100, fill="yellow")
                for i in range(3):
                    zatoka[y][x+i] = "x"
                return True
    return c.create_text(150, 350, text="Pristav je plny")

root.bind("<space>", lambda _: new_ship())
root.mainloop()