inp = [line.strip().split(' ') for line in open("rc.txt").readlines()]
mesiace = ['j', 'f', 'm', 'a', 'm', 'j', 'j', 'a', 's', 'o', 'n', 'd']
for i, val in enumerate(mesiace):
    ppl = []
    for p in inp:
        if int(p[0][2:4]) > 12:
            if int(p[0][2:4]) - 50 == i + 1:
                ppl.append([p[0][0:2] + str(int(p[0][2:4]) - 50) + p[0][4:], p[1], p[2]])
        else:
            if int(p[0][2:4]) == i + 1:
                ppl.append(p)
    print(f"{val}: {ppl}")