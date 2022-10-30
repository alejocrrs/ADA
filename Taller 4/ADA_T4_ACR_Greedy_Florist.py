def getMinimumCost(k, c):
    c.sort(reverse=True)
    costo = 0
    for i in range(len(c)):
        costo += (int(i/k) + 1) * c[i]
    return costo


print(getMinimumCost(3, [1,3,5,7,9]))