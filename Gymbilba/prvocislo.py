from operator import truediv


inp = int(input("Cislo: "))
prvocislo = True
for i in range(2, inp//2):
    if inp % i == 0:
        prvocislo = False 
print(prvocislo * "Je prvocislo" + (not prvocislo)* "Nie je prvocislo")
new = inp
prvocislo = True
while True:
    new += 1
    for i in range(2, new//2):
        if new % i == 0:
            break
    
    print(prvocislo * "Je prvocislo" + (not prvocislo)* "Nie je prvocislo")