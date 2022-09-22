# Análisis y Diseño de Algoritmos
# Quiz 1
# Alejandro Córdoba Ríos


def punto1():
    def a(n):
        if n == 1:
            return 1
        else:
            return a(n-1) + 4*n - 3
        
    print(f"[1] Elemento 13 de la secuencia: {a(13)}")
    
    
def punto2():
    def a(n):
        saldo = 110000
        for i in range(0,n):
            abono = 20000
            interes = abono*1.0104
            saldo += interes
        return saldo
            
    print(f"[2] Dinero en la fiducia tras 6 años: {round(a(72), 2)}")
   
punto1()
punto2()
