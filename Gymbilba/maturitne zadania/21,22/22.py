from datetime import date
knihy = [line.strip() for line in open("knihy.txt", "r").readlines()]
knihy = [[knihy[i], knihy[i+1].split(" ")] for i in range(0, len(knihy), 2)]
#print(knihy)
datum = date(2022, 12, 20)
pocet_vypozicani = []
prip = []
for kniha in knihy:
    #print(kniha)
    if len(kniha[1]) % 2 != 0:
        #print(int(kniha[1][-1][:2]))
        diff = datum - date(2022, int(kniha[1][-1][2:]), int(kniha[1][-1][:2]))
        #print(diff)
        if diff.days > 30:
            prip.append(kniha[0])
    pocet_vypozicani.append(len(kniha[1][0:len(kniha[1]):2]))
print(f"Musime poslat pripomienku ku kniham:  {', '.join(prip)}")
max = 0
for i in range(len(pocet_vypozicani)):
    if pocet_vypozicani[i] > max:
        max = pocet_vypozicani[i]
naj = []
for i in range(len(pocet_vypozicani)):
    k = pocet_vypozicani[i]
    if k == max:
        naj.append(knihy[i][0])
print("Najvypozicanejsie su:  " + ", ".join(naj))
