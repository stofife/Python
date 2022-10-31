
class Vylet:
    def __init__(self, date, dist, dur, dest) -> None:
        self.date, self.dist, self.dur, self.dest = date, dist, dur, dest

vylety = []

while True:
    inp = input(": ")
    
    if inp != "e":
        inp = inp.split("; ")
        vylety.append(Vylet(inp[0], float(inp[1]), int(inp[2]), inp[3]))
    else: break

for vylet in vylety:
    print(f"{vylet.date} {vylet.dist} {str(vylet.dur / 60).split('.')[0]}:{int(float('0.' + str(vylet.dur / 60).split('.')[1]) * 60)} {round(vylet.dist / (vylet.dur / 60), 1)} {vylet.dest}")