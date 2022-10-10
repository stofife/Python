from operator import indexOf
from random import sample

min = 1
max = 100

pole = sample(range(min,max), 1000)
print (pole)

iterations = 0
cislo = sample(pole, 1)[0]

for num in pole:
    if num == cislo:
        print(f"Cislo sa v poli nachadza na indexe {pole.index(num)}")
        print(f"Preslo {iterations} opakovani.")
        break
    iterations += 1
    
pole = pole.sort()

while True:
    if cislo > pole[(min + max - 1) // 2]:
        min += 1
    else:
        max += 1