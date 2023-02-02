from tkinter import *

root = Tk()

c = Canvas(width=500, height=500, master=root)
c.pack()

file = open("krizovka1-1.txt", "r").readlines()
kriz = [[int(line.strip().split(" ")[0]), line.strip().split(" ")[1]] for line in file]

def krizovka(k, offy, chars=False):
    for index, word in enumerate(k):
        print(word)
        offset = -word[0] + 1
        word = list(word[1])
        print(word)
        for pos, char in enumerate(word):
            print(pos, char)
            if pos != -offset:
                c.create_rectangle(200 + offset * 20 + pos * 20, offy + 10 + index * 20, 200 + offset * 20 + 20 + pos * 20, offy + 30 + index * 20)
            else:
                c.create_rectangle(200 + offset * 20 + pos * 20, offy + 10 + index * 20, 200 + offset * 20 + 20 + pos * 20, offy + 30 + index * 20, fill="grey")
            if chars:
                c.create_text(200 + offset * 20 + pos * 20 + 10, 10 + index * 20 + 10, text=char)
        #if chars:

krizovka(kriz, 0, chars=True)
krizovka(kriz, 200, chars=True)

root.mainloop()