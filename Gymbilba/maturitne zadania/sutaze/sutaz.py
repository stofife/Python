file = [line.strip() for line in open("hada.txt").readlines()]

print(len(file))
print(max([len(line) for line in file]))
out_file = ""
for line in file:
    cchar = line[0]
    count = 0
    for char in line: 
        if char != cchar:
            out_file += f"{char} {count} "
            count = 1
            cchar = char
        else:
            count += 1
    out_file += "\n"

print(out_file)