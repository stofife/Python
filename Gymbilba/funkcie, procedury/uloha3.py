import random

p1 = [random.randint(1,100) for _ in range(10)]
p2 = [random.randint(1,100) for _ in range(10)]

def sum_poli(pole1, pole2):
    return[pole1[i] + pole2[i] for i in range(len(pole1))]

print(sum_poli(p1, p2))