veta = input("Veta?: ")

v = veta.split(" ")

columns = 1
while True:    
    print(round(len(veta) / columns))
    out = "\n".join(veta[i:i+round(len(veta) / columns)] for i in range(0, len(veta), round(len(veta) / columns)))
    if len(out.split("\n")[0]) not in [i for i in range(columns - 2, columns + 2)]:
        columns += 1
    else:
        break

print("\n".join(veta[i:i+round(len(veta) / columns)] for i in range(0, len(veta), round(len(veta) / columns))))
print(f"pocet stlpcov: {columns}")

out = out.split("\n")
stlpce = []
for i in range(len(out[0])):
    stlpec = []
    for j in range(len(out)):
        try:
            stlpec.append(out[j][i])
        except:
            stlpec.append(" ")
    print(stlpec)
    stlpce.append(stlpec)