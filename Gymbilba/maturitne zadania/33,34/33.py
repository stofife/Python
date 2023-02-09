from random import shuffle
from copy import deepcopy
studenti = [i for i in range(int(input(": ")))]
otazky = deepcopy(studenti)
shuffle(otazky)
shuffle(studenti)

[print(f"{studenti[i]+1}.: {otazky[i] + 1}. otazka") for i in range(0,len(studenti))]