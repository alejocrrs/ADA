def getMinimumCost(k, c):
    costo = 0
    n = len(c)
    m = 1
    
    c.reverse()
    
    for i in range(n):
        costo += c[i] * m
        if (i + 1) % k == 0:
            m += 1
            
    return costo