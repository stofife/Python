import random

last_num = 0
num = 0
suc = 0
for i in range(1000):
    num = random.randint(1,6)
    if num == 6 and last_num == 6:
        suc += 1
    last_num = num
print(f"a) Pocet sestiek po sebe: {suc}")

kocka1 = 0
kocka2 = 0
suc = 0
for i in range(1000):
    kocka1 = random.randint(1,6)
    kocka2 = random.randint(1,6)
    if kocka1 == 6 and kocka1 == kocka2:
        suc += 1
print(f"b) Pravdepodobnost dvoch sestiek naraz: {suc / 1000 * 100}%")