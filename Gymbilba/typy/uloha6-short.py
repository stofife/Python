while not (globals().update(merania = []) if not "merania" in globals().keys() else False) and (merania := merania + [input(": ")]) and merania[-1] != "": pass
[print(f"Pocet merani: {len(merania)-1}")] + [print("Teploty: ")] + [print(f"{i+1}. meranie: {merania[i].split(' ')[3]}°C") for i in range(len(merania)-1)] + [print(f"Najvyssia teplota: {max([float(merania[i].split(' ')[3]) for i in range(len(merania)-1)])}°C")]