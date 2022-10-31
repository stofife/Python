class Student:
    def __init__(self, meno, znamky) -> None:
        self.meno = meno
        self.znamky = znamky

studenti = []

while True:
    meno = input("Meno: ")
    if meno == "":
        break
    znamky = list(map(int, input("Znamky: ").split(" ")))
    
    student = Student(meno, znamky)
    studenti.append(student)
    
for student in studenti:
    priemer = round(sum(student.znamky) / len(student.znamky), 2)
    if priemer <= 1.5 and (not [3,4,5] in student.znamky):
        prospech = "prospel s vyznamenanim"
    elif priemer <= 2.0 and (not [4,5] in student.znamky):
        prospech = "prospel velmi dobre"
    elif (not 5 in student.znamky):
        prospech = "prospel"
    else: prospech = "neprospel"
    
    print(f"{student.meno} {len(student.znamky)} znamok, priemer {priemer}, {prospech}")