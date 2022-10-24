def pp(n):
    if n == 1:
        return n ** 1/2
    if n > 1:
        return pp(n-1) ** 1/2

print(pp(5))
        