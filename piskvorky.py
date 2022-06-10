from cupshelpers import Printer


grid, player = 5*"######\n", "0"
while True:
    print(grid)
    print(f"Na rade je hrac {player}\n")
    x = int(input("Zadaj x-ovu suradnicu: "))
    y = int(input("Zadaj y-ovu suradnicu: "))
    grid = grid.split()[x + y*5] = player
    
    if player == "X": 
        if input("Vyhra? (a/n): ") == "a": break
    
    if player == "0": 
        player = "X"
    else: 
        player = "0"
print(f"-------> Vyhral {player} <-------")