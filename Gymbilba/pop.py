ls, inp, count = [], input("doprava abo lava? (p || l): "), int(input("O kolko: "))
for i in range(5): ls.append(__import__("random").randint(1,100))
print(ls)
if inp == "p": print(f"{ls[1:len(ls)] + [ls[0]]}")