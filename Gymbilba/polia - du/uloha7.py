from random import sample

ls = sample(range(1,1000), 10)

print(ls)

for i in range(len(ls)):
    if ls[i] % 5 == 0 or ls[i] % 10 == 0:
        print(i)
        break