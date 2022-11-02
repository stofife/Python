file = open("uloha2.txt", "r")

long = ""
count = 0

lines = file.readlines()

for line in lines:
    line = line.split()
    for word in line:
        if len(word) > len(long):
            long = word

for line in lines:
    line = line.split()
    for word in line:
        if len(word) == len(long):
            count += 1
            
print(f"Najdlhšie slovo je: {long}\nSlov rovnakej dĺžky ({len(long)}) je v texte {count}.")