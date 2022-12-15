f = [line.strip().split(" ") for line in open("cesty.txt", "r").readlines()]

mat = []

for line in f:
    mat += list(map(int, line))

print(max(mat))
print(sum(mat))