grid, player, end, win = 25*["#"], "0", False, compile("print(f'-------> Vyhral {player} <-------')", "tfuj", "exec")                                    
while not end: x, y, grid[x + y*5], end, win, player = int(input(" 12345\n1" + "".join(grid[0:5]) + "\n2" + "".join(grid[5:10]) + "\n3" + "".join(grid[10:15]) + "\n4" + "".join(grid[15:20]) + "\n5" + "".join(grid[20:25]) + "\n" + f"\nNa rade je hrac {player}\n" + "\nZadaj x-ovu suradnicu: ")), int(input("Zadaj y-ovu suradnicu: ")), player, True if input("\nVyhra? (a/n): ") == "a" else False, exec(win) if True else False, (lambda x: "X" if x == "0" else "0")(player)