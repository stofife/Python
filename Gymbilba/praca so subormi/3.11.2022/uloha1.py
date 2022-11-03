f = open("uloha1.txt", "r")
lines = f.readlines()
res = []

for line in lines:
    ln = ""
    for char in line:
        if ord(char) < 97 or ord(char) > 123:
            pass
        else:
            if ord(char) + 1 >= 123:
                char = chr(ord(char) + 1 - 26)
            else:
                char = chr(ord(char) + 1)
        ln += char
    res.append(ln)
print(res)