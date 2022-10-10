ls = []
for i in range(2,1000):
    prvocislo = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            prvocislo = False
    if prvocislo:
        ls.append(i)
for i in range(0, len(ls), 2):
    print(f"{ls[i]} a {ls[i+1]}")