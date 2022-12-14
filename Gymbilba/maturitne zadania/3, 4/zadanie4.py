sutaziaci = [i for i in range(5220, 5230)] 
for s in sutaziaci:
    file = open(f"{s}.txt", "w")
    res = "\n".join(list(map(str, [i for i,v in enumerate(list(map(int, [line.strip() for line in open("hlasovanie_1.txt").readlines()]))) if v == s])))
    file.write(res)