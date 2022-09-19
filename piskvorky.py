grid, player, win, end, onend = 25*["#"], "0", False, compile('if win == True: print(f"-------> Vyhral {player} <-------")', 'do', 'exec'), None
while win != True:
    x,y,grid[x + y*5],win = int(input(" 12345\n1" + "".join(grid[0:5]) + "\n2" + "".join(grid[5:10]) + "\n3" + "".join(grid[10:15]) + "\n4" + "".join(grid[15:20]) + "\n5" + "".join(grid[20:25]) + "\n" + f"\nNa rade je hrac {player}\n" + "\nZadaj x-ovu suradnicu: ")), int(input("Zadaj y-ovu suradnicu: ")), player,(lambda x: input("Vyhra? (a/n): ") == "a" if grid.count("#") <= 24 else False)(win)
    player, onend = (lambda x: "X" if x == "0" else "0")(player), exec(end)
