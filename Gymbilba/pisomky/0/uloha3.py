ls = []
#max = 0
#min = 0
while True:
    inp = int(input("Zadaj skore: "))
    if inp == 0:
        break
    else:
        ls.append(inp)
ls.sort()
ls.pop(0)
ls.pop(len(ls)-1)
sucet = 0
for num in ls:
    sucet += num
print(sucet / len(ls))
