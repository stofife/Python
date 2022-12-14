sifra = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
inp = input("Veta?: ")
out = ""
for char in inp:
    for v in sifra:
        if char in v:
            print(v.index(char), sifra.index(v))
            out = out + str(sifra.index(v)) * (v.index(char) + 1) + " "
print(out)
maximum,max_list = 0, []
for s in out.split(" ")[:-1]:
    print(s)
    if len(s) > maximum:
        maximum = len(s)
for s in out.split(" ")[:-1]:
    if len(s) == maximum:
        max_list.append(s[0])

print(f"Najcastejsie zvolene policka: {', '.join(max_list)}")