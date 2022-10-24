from random import randint

ls = [randint(1,100) for _ in range(10)]

def naj(pole):
    rast = longest = list()
    for i in range(len(pole)-1):
        if pole[i] < pole[i+1]:
            rast.append(pole[i])
        else:
            rast.append(pole[i])
            if len(rast) > len(longest): longest = rast
            rast = []
    return len(longest)

print(ls)
print(naj(ls))
    