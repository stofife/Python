global chlapci
global dievky

chlapci, dievky = ['Roman', 'Jozo', 'Adam', 'Michal', 'Palo'], ['Monika', 'Andrea', 'Anka', 'Lucia', 'Petra']

def vypis(ls) -> None:
    print("   ".join(ls))

def utried() -> None:
    for i in range(len(chlapci)-1):
        for i in range(len(chlapci)-1):
            if ord(chlapci[i][0]) > ord(chlapci[i+1][0]):
                chlapci[i], chlapci[i+1] = chlapci[i+1], chlapci[i]
                dievky[i], dievky[i+1] = dievky[i+1], dievky[i]
    vypis(chlapci)
    vypis(dievky)
    
def dlzka(ls):
    return sum([len(ls[i]) for i in range(len(ls))])
    
def pary():
    return [f"{dievky[i]}+{chlapci[i]}" for i in range(len(chlapci))]

def je_par(char):
    cond = False
    for i in range(len(chlapci)):
        if char == chlapci[i][0] and chlapci[i][0] == dievky[i][0]:
            cond = True
    return cond


utried()
print(dlzka(chlapci))
print(pary())
print(je_par("A"))
