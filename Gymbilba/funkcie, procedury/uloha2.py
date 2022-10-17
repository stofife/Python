def mocnina(cislo, n):
    num = cislo
    for _ in range(n-1):
        num = num * cislo
    print(num)

mocnina(10,5)