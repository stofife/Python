from random import randint

#barcode = str(randint(10000000, 99999999))
for barcode in open("kod_a.txt", "r").readlines():
    barcode = barcode.strip()
    control = barcode[-1]
    barcode = barcode[:-1]
    print(f"Code: {barcode}")
    control_dig = ""
    control_dig += str(sum(list(map(int, list(barcode[:4])))) % 2)
    control_dig += str(sum(list(map(int, list(barcode[2:6])))) % 2)
    control_dig += str(sum(list(map(int, list(barcode[4:])))) % 2)
    print(control_dig)
    out = 0
    for index, bit in enumerate(control_dig[::-1]):
        out += int(bit) * 2 ** index
    if int(control) != out:
        print(f"Pri kontrole kodu {barcode} nastala chyba ({out} != {control})")