inp = input(": ").split(" ")
num, base, index = inp[0], int(inp[1]), [str(i) for i in range(0, 10)] + [chr(i) for i in range(65, 71)]

print(f"Num in base 10: {sum([index.index(num[i]) * base**(len(num) - 1 - i) for i in range(0, len(num))])}")
