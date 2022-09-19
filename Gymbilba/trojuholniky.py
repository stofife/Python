a,b,c = int(input("a: ")), int(input("b: ")), int(input("c: "))
t = [a,b,c]
t.sort()
t = t[::-1]
if t[1] + t[2] < t[0]:
    print("nie je trojuholnik")
else:
    if t[0] == t[1] == t[2]:
        print("rovnostranny")
    if t[0] != t[1] and t[1]== t[2]:
        print("rovnoramenny")
    if t[0]**2 == t[1]**2 + t[2]**2:
        print("pravouhly")