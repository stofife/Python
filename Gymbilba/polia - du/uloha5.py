from random import randint

ls = []

for i in range(100):
    ls.append(randint(1,100))

usek = []
old = []
index = 0
for i in range(len(ls)-1):
    if ls[i] < ls[i+1]:
        usek.append(ls[i])
    else:
        usek.append(ls[i])
        if len(usek) > len(old):
            old = usek
        usek = []
print(old)