from tkinter import *

root = Tk()

inp = input("exp to eval: ")

c = Canvas(root, width="320", height="128")

colors, color = ["blue", "violet", "orange" "yellow", "green", "cyan", "pink"], ["black"] * len(inp)
par = []
for index, char in enumerate(list(inp)):
    print(f'"{char}", index: {index}, par_list: {par}')
    if char == "(":
        par.append(index)
    if char == ")":
        if par != []: 
            color[index] = colors[len(par) - 1]
            color[par.pop()] = color[index]
        else:
            color[index] = "red"

for i in par:
    color[i] = "red"

for index, char in enumerate(list(inp)):
    c.create_text(12 + 18 * index, 16, text=char, fill=color[index], font="Arial 20")

if par != []:
    c.create_text(40, 60, text="Si kokot.")

c.pack()

root.mainloop()  