def ejercicio_1a(n):
    if n == 1:
        return 1
    else:
        return ejercicio_1a(n-1) + n

def ejercicio_1b(n):
    return n**2

def ejercicio_1c(n):
    if n == 1:
        return 1
    else:
        return ejercicio_1c(n-1) + (3*n) -2

def ejercicio_1d(n):
    if n == 1:
        return 1
    else:
        return ejercicio_1d(n-1) + (12*n) - 12

def ejercicio_3(meses):
    def recursion_years(years):
        if years == 0:
            return 3500000
        else:
            return recursion_years(years-1) + (recursion_years(years - 1) * 0.0271)
    
    return recursion_years(meses//12)
        
        

def main():
    print(f"Ejercicio 1A: {ejercicio_1a(9)}")
    print(f"Ejercicio 1B: {ejercicio_1b(9)}")
    print(f"Ejercicio 1C: {ejercicio_1c(9)}")
    print(f"Ejercicio 1D: {ejercicio_1d(9)}")
    
    print(f"Ejercicio 3: $ {round(ejercicio_3(84), 2)}")
    
    
main()
