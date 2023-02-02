from random import randint

dims = list(map(int, input("Rozmery (w h): ").split(" ")))

pozemok = []
for h in range(dims[0]):
    row = []
    for w in range(dims[1]):
        row.append(randint(-5,5))
    pozemok.append(row)

def pprint(ls):
    for item in ls:
        print(item)

pprint(pozemok)

inp = input("(x, y, pocet_furikov -||-):").split(" ")
for i in range(0, len(inp), 3):
    x, y, num = int(inp[i]), int(inp[i+1]), int(inp[i+2])
    pozemok[y][x] += num

if sum([sum(i) for i in pozemok]) == 0:
    print("Zarovnane")    

pprint(pozemok)