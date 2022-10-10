inp = int(input("Cislo pls: "))
palindrom = False
num = inp
cifry = 0
while num > 0:
    num = num % 10
    cifry += 1
print(cifry) 