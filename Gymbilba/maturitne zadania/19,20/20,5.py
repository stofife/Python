inp = input(": ").split(" ")
num = inp[0] 
base = int(inp[1])
sec_base = int(inp[2])
ind = [str(i) for i in range(0, 10)] + [chr(i) for i in range(65, 71)]

num_base_ten = sum([ind.index(num[i]) * base**(len(num) - 1 - i) for i in range(0, len(num))])
rem = num_base_ten
print(num_base_ten)
num_2nd_base = ""
while rem > 0:
    num_2nd_base += str(ind[rem % sec_base])
    rem = rem // sec_base
print(num_2nd_base[::-1])