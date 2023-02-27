with open("sms.txt") as f:
    lines = f.readlines()

out_str = ""
for line in lines:
    line.replace(" ", "")
    print(line)