def najspoldel(x, y):
    if x == y:
        return x
    if x > y:
        return najspoldel(x - y, y) 
    else:            
        return najspoldel(x, y - x)
    
print(najspoldel(10050,100))