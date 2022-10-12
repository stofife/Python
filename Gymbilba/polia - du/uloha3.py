from random import randint

keno = []

for i in range(10):
    keno.append(randint(1,99))
    
guess = input("Zadaj cisla oddelene ciarkou (C, C, C...):")
vklad = int(input("Vklad?: "))

guess = guess.split(", ")

right = 0
for i in range(10):
    if int(guess[i]) in keno:
        right += 1

print("Tvoja vyhra: " + str((right == 0) * 1 + (right == 5) * 3 + (right == 6) * 10 + (right == 7) * 20 + (right == 8) * 500 + (right == 9) * 10000 + (right == 10) * 200000 * vklad) + "€")