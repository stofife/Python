from random import choice

def calc(tip, mute=True):
    c_guesses, guessed = 0, []

    for num in tip:
        if num in cisla_loterie:
            c_guesses += 1
            guessed += [num]
    if not mute:
        print(f"Vyzrebovane cisla: {', '.join(list(map(str, cisla_loterie)))}")
        print(f"Trafili ste {c_guesses} cisel ({round((c_guesses / 6)*100, 2)}%), a to tieto: {guessed}")
    return c_guesses

cisla_loterie = [choice([i for i in range(1, 50)]) for _ in range(6)]
print(cisla_loterie)

inp = list(map(int, input("Tip?: ").split(" ")))
calc(inp, False)
res = []
for tip in [list(map(int, line.split(" "))) for line in open("loteria_2.txt", "r").readlines()]:
    res.append(calc(tip))

print(f"Prave jedno: {res.count(1)}")
print(f"Prave dve: {res.count(2)}")
print(f"Prave tri: {res.count(3)}")
print(f"Prave pat: {res.count(5)}")
print(f"Prave sest: {res.count(6)}")