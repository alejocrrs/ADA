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
    def a1(n): # Calculando interes mensual
        saldo = 110000
        for x in range(1,n+1):
            abono = 20000
            saldo += abono
            interes = saldo * 0.0104166667 # Interes mensual de un interes anual de 0.125
            saldo += interes # Se incrementa el interes
        return saldo
    
    def a2(n): # Calculando interes anual
        saldo = 110000
        for x in range(1,n+1):
            abono = 20000
            saldo += abono
            if x % 12 == 0:
                interes = saldo * 0.125 # Interes anual de 0.125
                saldo += interes # Se incrementa el interes
        return saldo
            
    print(f"[2.1] Dinero en la fiducia tras 6 años (interés mensual): {round(a1(72), 2)}")
    print(f"[2.2] Dinero en la fiducia tras 6 años (interés anual): {round(a2(72), 2)}")
   
punto1()
punto2()
