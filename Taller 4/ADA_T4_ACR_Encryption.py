import math


def generateMatrix(code, rows, columns):
    listcode = list(code)
    matrix = []
    [matrix.append([""] * columns) for r in range(rows)]
    
    for r in range(rows):
        for c in range(columns):
            if len(listcode) > 0:
                matrix[r][c] = listcode.pop(0)
    return matrix


def interpretMatrix(matrix, rows, columns):
    message = ""
    for c in range(columns):
        for r in range(rows):
            character = matrix[r][c]
            if character != "":
                message += character
        message += " "
    return message.rstrip()


def encryption(s):
    code = s.replace(" ", "")
    L = len(code)
    rL = math.sqrt(L)
    
    if rL % 1 == 0:
        rows = int(rL)
        columns = int(rL)
    else:
        rows = math.floor(rL)
        columns = math.ceil(rL)
        
        if rows * columns < L:
            rows = math.ceil(rL)
            columns = math.ceil(rL)
            
    
    matrix = generateMatrix(code, rows, columns)
    return interpretMatrix(matrix, rows, columns)
    
    
s = "if man was meant to stay on the ground god would have given us roots"
print(encryption(s))
