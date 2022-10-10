from cgi import print_directory


typ = input("Aky utvar? (\"plny stv\", \"stv\", \"obdl\", \"prav troj\", \"op prav troj\", \"rovno\", \"schody\", \"hodiny\", \"koso\"): ")

if typ == "plny stv":
    size = int(input("Velkost: "))
    print(size*(size*"*" + "\n"))
elif typ == "stv":
    size = int(input("Velkost: "))
    print(size*"*")
    for i in range(size):
        print("*" + (size-2)*" " + "*")
    print(size*"*")
elif typ == "obdl":
    size_a = int(input("Velkost strany a: "))
    size_b = int(input("Velkost strany b: "))
    print(size_a*"*")
    for i in range(size_b):
        print("*" + (size_a-2)*" " + "*")
    print(size_a*"*")
elif typ == "prav troj":
    size_a = int(input("Velkost strany a: "))
    for i in range(size_a):
        print("*" * i)
elif typ == "op prav troj":
    size_a = int(input("Velkost strany a: "))
    for i in range(size_a):
        print("*" * (size_a - i))
elif typ == "rovno":
    size = int(input("Velkost strany : "))
    for i in range(size):
        print(" " * (size // 2 - i) + "*" * i )
elif typ == "schody":
    size = int(input("Pocet schodov: "))
    for i in range(size):
        print(" " * i + "***\n")
elif typ == "koso":
    for i in range(0,3):
        print(" " * i + "****")