ret = input("String: ")
podr = input("Substring: ")

print(len([i for i in range(len(ret)) if ret.startswith(podr, i)]))