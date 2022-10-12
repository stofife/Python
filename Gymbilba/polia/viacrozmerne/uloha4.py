pole0 = [__import__("random").sample(range(1,11), 5) for _ in range(10)]
pole1 = []
for j in range(5):
    pole1.append([pole0[i][j] for i in range(10)])
print(pole1)