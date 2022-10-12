deti = 20 * [1]
v = int(input("Vypadnut: "))
m = int(input("Kolke v poradi?: "))
o = int(input("Od ktoreho zaciname (1-20): ")) - 1

count = 0

for i in range(o, 20, m):
    if count < v:
        if i != o:
            deti[i] = 0
            count += 1
    else:
        break
    
print(deti)