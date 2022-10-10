from random import randint
ls = []
for i in range(5): ls.append(randint(1,100))
max1 = 0
max2 = 0
for i in range(5):
    if ls[i] > max1: 
        max1 = ls[i]
for i in range(5):
    if max1 > ls[i] > max2: 
        max2 = ls[i]
print(ls)
print(max1, max2)