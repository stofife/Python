from random import randint

def sort(ls):
    max = 0
    for j in range(len(ls)*(len(ls) - 1) // 2):
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i] 
    return ls
    
ls = []

for i in range(10):
    ls.append(randint(1,100))

inp = int(input("Nove cislo: "))

ls.append(inp)

print(sort(ls))


                
            