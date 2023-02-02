from random import shuffle

with open("poprehadzovany_text1_vstup.txt", "r") as f:
    lines = [line.strip().split(" ") for line in f]

out = []
for line in lines:
    l_shuffled = []
    for word in line:
        if len(word) > 3:
            mid = list(word[1:-2])
            shuffle(mid)
            shuffled = "".join([word[0]] + mid + [word[-1]])
            l_shuffled.append(shuffled)
        else:
            l_shuffled.append(word)
    out.append(l_shuffled)

for line in out:
    print(" ".join(line))