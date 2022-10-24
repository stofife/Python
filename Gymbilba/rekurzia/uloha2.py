def xnan(x,n):
    if n <= 1:
        return x
    else:
        return xnan(x, n-1) * x 

print(xnan(5,3))