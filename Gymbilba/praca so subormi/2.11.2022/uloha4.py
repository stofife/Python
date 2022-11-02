f = open("uloha1.txt", "r")
lines = f.readlines()

inp = int(input("O koľko písmen mám posunúť?: "))

for line in lines:
    for char in line:
        if ord(char) < 97 or ord(char) > 123:
            pass
        else:
            if ord(char) + inp > 123:
                char = ord(char) + inp - 26
            else:
                char = chr(ord(char) + inp)