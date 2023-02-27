f = [line.strip() for line in open("anketa.txt").readlines()]

for i in range(0, len(f), 2):
    print(f[i])
    vals = list(map(int, f[i+1].split(" ")))
    print(vals)
    print(max(vals))
    for i, v in enumerate(vals):
        if i == 0:
            print("1) Áno - " + str(vals[i]), end="   ")
        elif i == 1:
            print("2) Nie - " + str(vals[i]), end="   ")
        elif i == 2:
            print("3) Neviem - " + str(vals[i]), end="   ")
        if v == max(vals):
            print((vals[i]) * ('\033[91m' + '■' + '\x1b[0m'))
        else:
            print((vals[i]) * ('\u001b[32m' + '■' + '\x1b[0m'))