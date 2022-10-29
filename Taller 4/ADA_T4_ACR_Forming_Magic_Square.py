def obtenerCosto(matrix, magic):
    costo = 0
    for i in range (3):
        for j in range(3):
            costo += abs(matrix[i][j] - magic[i][j])
    return costo
            

def formingMagicSquare(s):
    magical = [
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[8,3,4],[1,5,9],[6,7,2]]
        ]
    
    costos = []
    for magic in magical:
        costos.append(obtenerCosto(s, magic))
    return min(costos)


s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s))