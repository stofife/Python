res = ""
for j in range(1, 11):
    for i in range(1,11):
        res += f"{str(i * j)} "
    res += "\n"
print(res)
