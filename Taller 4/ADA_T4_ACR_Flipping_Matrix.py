def flippingMatrix(matrix):
    n2 = len(matrix)
    mid = n2 // 2
    n = n2 - 1
    suma = 0
    
    for i in range(mid):
        for j in range(mid):
            comp = []
            comp.append(matrix[i][j]) # Elemento actual (extremo superior izquierdo)
            comp.append(matrix[i][n - j]) # Espejo en el extremo superior derecho
            comp.append(matrix[n - i][j]) # Espejo en el extremo inferior izquierdo
            comp.append(matrix[n - i][n - j]) # Espejo en el extremo inferior derecho
            suma += max(comp)
    return suma
    

matrix = [
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108]
        ]


print(flippingMatrix(matrix))