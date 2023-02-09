
with open("kamosi.txt", "r") as f:
    f = f.readlines()
    ppl = [[f[i].strip(), f[i+1].strip().split(" ")] for i in range(0, len(f)-1, 2)]
    
ppl.sort(key=lambda x: x[0])
print(ppl)

def maju_nar(month):
    for person in ppl:
        if int(person[1][2]) == month:
            print(f"{person[0]} {person[1][1]}. {2023 - int(person[1][3])} rokov.")

maju_nar(2)