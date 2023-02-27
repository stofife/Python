with open("cyklovylety.txt") as f:
    lines = [line.strip() for line in f.readlines()]

vylety = [line.split(" ") for line in lines]
for v in vylety:
    print(f'{v[0]} {v[1]} {int(v[2]) // 60}:{int(v[2]) % 60} {float(v[1]) / float(str(int(v[2]) // 60) + "." + str((int(v[2]) % 60)))}')