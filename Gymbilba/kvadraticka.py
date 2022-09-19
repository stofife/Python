from math import sqrt
a, b, c = float(input('a: ')), float(input("b: ")), float(input("c: "))
if input("Je to spravne?\n" + str(a) + "x² + "  + str(b) + "x + " +  str(c) + " =\n(Stlac enter ak ano, naser si ak nie)") == "":
    if a > 1:
        print((b/a)/2 + sqrt(((b/a)/2)**2 - (c/a)), b/2 - sqrt(((b/a)/2)**2) - (c/a))
    if a == 1:
        print("x₁: " + str((b/2 + sqrt((b/2)**2 - c))), "x₂: " + str((b/2 - sqrt((b/2)**2 - c))))