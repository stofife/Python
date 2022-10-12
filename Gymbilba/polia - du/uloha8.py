from random import sample

a = sample(range(1,100), 10)
b = sample(range(1,100), 10)

for num in b:
    if not (num in a):
        print(num) 