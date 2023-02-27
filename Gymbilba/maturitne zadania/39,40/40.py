digits = ["nula", "jeden", "dva", 'tri', 'styri', 'pat', 'sest', 'sedem', 'osem', 'devat']
special = ['nast', "desat", 'dvadsat', 'tridsat', 'styridsat']
mul = ['desiat', 'sto', 'tisic']



inp = input(": ")


if int(inp) in [i for i in range(11,20)]:
    print(str(digits[int(inp[1])]) + special[0])
else:
    for i,d in enumerate(inp):
        if int(d) != 0 and int(d) * (10 ** (len(inp) - i - 1)) not in [10,20,30,40]:
            if len(inp) - 2 - i > -1:
                if int(inp) < 1001:
                    print(digits[int(d)] + mul[len(inp) - 2 - i])
                else:
                    print(digits[int(d)] + mul[-1])
            else:
                print(digits[int(d)])
        else:
            print(special[int(d)])