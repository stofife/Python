from random import choice
slovo, guesses = choice([line.strip() for line in open("obesenec.txt").readlines()]), 10
print(slovo)
guessed = len(slovo)*["."]
while guesses > 0 and "." in guessed:
    char = input("Hadaj pismenko: ")
    find = [index for index, ltr in enumerate(slovo) if ltr == char]
    if find == []: guesses -= 1 
    for i in find: guessed[i] = char
    print("".join(guessed))