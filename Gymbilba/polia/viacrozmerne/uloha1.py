from random import sample

x = int(input("X: "))
y = int(input("Y: "))

pole = []

for i in range(y):
    pole.append(sample(range(1,1000), x))

max = 0
min = 1000

min_pos = []
max_pos = []

for i in range(y):
    for j in range(x):
        if pole[i][j] > max:
            max = pole[i][j]
            max_pos = [i,j]
        if pole[i][j] < min:
            min = pole[i][j]
            min_pos = [i,j]

print(f"Min: {min}\nMax: {max}\nMax index: {max_pos}\nMin index: {min_pos}")

min_pos, max_pos = max_pos, min_pos