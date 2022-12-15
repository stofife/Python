from random import randint

f = open("virus.txt", "r").readlines()

if bool(randint(0,1)):
    for i in range(len(f)):
        swap = randint(0, len(f)-1)
        f[i], f[swap] = f[swap], f[i]
for j in range(len(f)):
    f[j] = f[j].split(" ")
    for i in range(len(f[j])):
        if bool(randint(0,1)):
            f[j][i] = f[j][i][::-1]
    f[j] = " ".join(f[j])

open("virus_vystup.txt", "w").write("".join(f))
    