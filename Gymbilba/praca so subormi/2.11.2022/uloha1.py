freq = {}
file = open("uloha1.txt", "r")

for line in file.readlines():
    print(line)
    for char in list(line):
        if char not in freq.keys():
            freq[char] = 1
        else:
            freq[char] += 1

print(freq)
    