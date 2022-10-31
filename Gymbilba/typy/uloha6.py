class Meranie:
    def __init__(self, kod, dat, cas, tep, obl) -> None:
        self.kod, self.dat, self.cas, self.tep, self.obl = kod, dat, cas, tep, obl

merania = []

while True:
    inp = input(": ")
    if inp == "": break
    
    inp = inp.split(" ")
    merania.append(Meranie(inp[0], inp[1], inp[2], float(inp[3].replace(",",".")), inp[4]))
    
def pocet_merani():
    print(len(merania))

def vypis_teploty():
    for mer in merania:
        print(f"{mer.tep}°C")

def najvyssia_teplota():
    max_tep = 0
    for mer in merania:
        if mer.tep > max_tep: max_tep = mer.tep
    print(f"Najvyssia teplota bola: {max_tep}°C")
    
pocet_merani()
vypis_teploty()
najvyssia_teplota() 