pocet = 0
for i in range(1000,10000):
    palindrom = True
    for j in range(len(str(i))):
        if str(i)[j] != str(i)[len(str(i)) - 1 - j]:
            palindrom = False
    if palindrom:
        print(f"Palindrom: {i}")
        pocet += 1
print(f"Pocet palindromov: {pocet}")

        
        