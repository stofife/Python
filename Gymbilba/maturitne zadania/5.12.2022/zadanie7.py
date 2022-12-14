file = open("hada.txt", "r")

lines = [line.strip() for line in file.readlines()]

print(len(lines))
print(max([len(line) for line in lines]))

out = ""

for line in lines:
    char_i = 0
    count = 1
    while True:
        if line[char_i + 1] == line[char_i]:
            count += 1
            char_i += 1
        else:
            out += f"{line[char_i]} {count} "
            print(out)
            count = 1
            char_i += 1
        if char_i + 1 == len(line):
            out += f"{line[char_i]} {count}"
            out += "\n"
            break
            
out_file = open("hada_komprimovane.txt", "w")
out_file.write(out)