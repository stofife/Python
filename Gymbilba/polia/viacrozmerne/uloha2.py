pole, inp = [__import__("random").sample(range(1,101), 10) for _ in range(10) ], input("Ktore dva vymenit ({0 - y-1}, {0 - y-1} ): ").split(", ")
pole[int(inp[0])], pole[int(inp[1])] = pole[int(inp[1])], pole[int(inp[0])]