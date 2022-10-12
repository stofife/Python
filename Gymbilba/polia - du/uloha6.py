from random import sample

tymA = sample(range(1,10), 8)
tymB = sample(range(1,10), 8)

print(f"Skore jednotlivcov tymu A: {tymA}")
print(f"Skore jednotlivcov tymu B: {tymB}")
print(f"Primerne skore tymu A je {sum(tymA) / len(tymA)} a Priemerne skore tymu B je {sum(tymB) / len(tymB)}")
print((sum(tymA) > sum(tymB)) * "Vyhral tym A" + (sum(tymA) < sum(tymB)) * "Vyhral tym B")