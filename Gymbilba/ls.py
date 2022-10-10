from operator import truediv
from random import random


from random import randint
ls = []

for i in range(5):
    ls.append(randint(1,100))

def maximum(ls):
    max = 0
    max_index = 0
    for i in range(len(ls) - 1):
        if ls[i] > max: max, max_index = ls[i], i
    return [max, max_index]

def minimum(ls):
    min = maximum(ls)[0]
    min_index = 0
    for i in range(len(ls) - 1):
        if ls[i] < min: min, min_index = ls[i], i 
    
    return [min, min_index]

print(ls)
print(f"Maximum: {maximum(ls)[0]}\nMinimum: {minimum(ls)[0]}\n Pozicie: [{maximum(ls)[1]}], [{minimum(ls)[1]}]")
ls[maximum(ls)[1]], ls[minimum(ls)[1]] = ls[minimum(ls)[1]], ls[maximum(ls)[1]]
print(ls)

