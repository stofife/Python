from random import randint

druzstva = int(input("Pocet druzstiev: "))

teams = [i for i in range(1, druzstva + 1)]

vyhry = []

for i in range(druzstva):
    vyhry.append([randint(0,10), randint(0,10), randint(0,10)])
    
def body(ls):
    return ls[0] * 5 + ls[1] * 4 + ls[2] * 3

for i in range(10):
    for i in range(druzstva - 1 ):
        if body(vyhry[i + 1]) > body(vyhry[i]):
            vyhry[i], vyhry[i+1] = vyhry[i+1], vyhry[i]
            teams[i], teams[i+1] = teams[i+1], teams[i]
            
for vyhra in vyhry:
    print(body(vyhra), end=" ")
print()

for i in range(3):
    print(f"{i+1}. miesto: {teams[i]}. družstvo, s počtom bodov {body(vyhry[i])}")