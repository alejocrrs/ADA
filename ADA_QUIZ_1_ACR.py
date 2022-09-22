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
        for x in range(1,n+1):
            abono = 20000
            saldo += abono
            interes = saldo * 0.0104 # Interes anual de 0.125
            saldo += interes # Se incrementa el interes
        return saldo
            
    print(f"[2] Dinero en la fiducia tras 6 años: {round(a(72), 2)}")
   
punto1()
punto2()
