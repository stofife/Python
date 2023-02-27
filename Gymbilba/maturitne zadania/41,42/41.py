with open("elektricky.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    
print(len(lines))
for i, e in enumerate(lines):
    if e[0] != e[-1]:
        print(f"Elektricka cislo {i + 1} nekonci na rovnakej zastavke.")
    if e[0:(len(e) + 1 //2)] != e[(len(e) + 1 //2):]:
        print(f"Elektricka cislo {i + 1} sa nevracia po rovnakej trase.")