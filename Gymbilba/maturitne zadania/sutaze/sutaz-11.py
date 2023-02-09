from collections import Counter
inp = input(": ")
dicti = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]

out_str = ""
for char in inp:
    for index, val in enumerate(dicti):
        if char in val:
           out_str += str(index) * (val.index(char) + 1) + " "
print(out_str) 
c = Counter(out_str)
print(f"{c.most_common()[1][0]}: pouzite {c.most_common()[1][1]} krat")