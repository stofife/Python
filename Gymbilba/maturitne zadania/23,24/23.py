#print([chr(i) for i in range(97,123)])
nums = list(map(int, input(": ").split(" ")))[:-1]
text = input("Text: ")

cur_ind = 0
out = ""
for char in text:
    print(f"{cur_ind} - {nums[cur_ind]}: {char}")
    if ord(char) not in [i for i in range(97,123)]:
        out += char
    else:
        if ord(char) + nums[cur_ind] > 122:
            out += chr(97 + (ord(char) + nums[cur_ind] - 123))
        else:
            out += chr(ord(char) + nums[cur_ind])
        cur_ind = cur_ind + 1 if cur_ind + 1 < len(nums) else 0

print(out)