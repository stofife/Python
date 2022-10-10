n = int(input("Zadajte n na overenie: "))
exists = False
for i in range(n, 2*n - 2):
    prvocislo = True
    for j in range(2, i//2):
        if i % j == 0:
            prvocislo = False
    if prvocislo:
        print(f"Veta plati, najblizsie prvocislo je vzdialene {i - n} a je to {i}.")
        break