with open("kompresia_obrazka_1.txt") as f:
    lines = [line.strip() for line in f]

dims = lines[0]

out = []

for line in lines[1:]:
    line_out = ""
    cur_char = "0"
    count = 0
    for index, char in enumerate(line):
        if index == 0 and char == "1":
            line_out += "0 "
            cur_char = "1"
        if char != cur_char:
            if count != 0:
                line_out += f"{count} "
                cur_char = char
                count = 1
        elif index == len(line) - 1:
            count += 1
            line_out += str(count)
        else:
            count += 1
    out.append(line_out)

with open("kompresia_obrazka_vystup.txt", "w") as f:
    out_str = dims + "\n" + "\n".join(out)
    f.write(out_str)