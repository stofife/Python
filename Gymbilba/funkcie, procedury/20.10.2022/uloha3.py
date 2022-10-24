from random import choice

def pprint(arr):
    for row in arr:
        print(row)

global more
more = []

for i in range(10):
    more.append([choice(["0", "0", "*"]) for _ in range(10)])

def largest_island():
    land = [[] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if more[i][j] == "*":
                land[i].append(j)
    print(land)

        
    
pprint(more)

largest_island()