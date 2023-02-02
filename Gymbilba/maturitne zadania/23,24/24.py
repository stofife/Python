mapa = [list(map(int, line.strip().split(" "))) for line in open("mapa.txt", "r")]
print(mapa)
def check_around(x,y):
    land = []
    if x + 1 <= len(mapa[0])-1:
        if mapa[y][x+1] > 0:
            land.append([x+1,y]) 
    if x - 1 >= 0:
        if mapa[y][x-1] > 0:
            land.append([x-1,y])
    if y + 1 <= len(mapa)-1:
        if mapa[y+1][x] > 0:
            land.append([x,y+1])
    if y - 1 >= 0:
        if mapa[y-1][x] > 0:
            land.append([x,y-1])
    return land
    print(mapa[y-1][x])
    print(mapa[y+1][x])
    print(mapa[y][x+1])
    print(mapa[y][x-1])
    
checked = []
islands = []
cur_island = []

for y in range(0, len(mapa)):
    for x in range(0, len(mapa[0])):
        if mapa[y][x] != 0:
            checked.append([x,y])
            if [x,y] not in cur_island:
                cur_island.append([x,y])
            while True:
                neighbours = check_around(x,y)
                if neighbours == []:
                    break
                else:
                    for n in neighbours:
                        check_around(n)