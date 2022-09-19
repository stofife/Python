from time import process_time_ns


h, m = float(input()), int(input())
bmi = m / h**2
if bmi <= 18.5:
    print('Si podvyziveny')
if bmi > 18.5 and bmi < 25:
    print('Si normalny')
if bmi >= 25 and bmi < 30: 
    print('Mierna nadvaha')
if bmi >= 30 and bmi < 40:
    print("Obesita")
if bmi > 40:
    print('Tazka obesita')