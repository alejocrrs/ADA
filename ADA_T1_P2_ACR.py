# =============================================================================
# Análisis y Diseño de Algoritmos
# Taller 1: Complejidad algorítmica
# Alejandro Córdoba Ríos
# =============================================================================
import time
import matplotlib.pyplot as grafico

def main():
    
    def p1():
        tiempos = []
        tinicial = time.time()
        for n in range(1,10000):
            i = 0
            while (i < n):
                print(n, i)
                i += 1
                
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
                
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
            
        
    def p2():
        tiempos = []
        tinicial = time.time()
        for n in range(1,1000):
            i = 0
            while (i < n):
                c = i
                while (c > 0):
                    print(n, i)
                    c /= 2
                i += 1
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    def p3():
        tiempos = []
        tinicial = time.time()
        
        for n in range(1,10000000):
            i = 1
            while (i < n):
                
                print(n, i)
                i = i * 2
                
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    def p4():
        tiempos = []
        tinicial = time.time()
        
        for n in range(1,1000):
            i = 0
            while (i < n):
                
                j = 1
                while (j < n):
                    print(n, i)
                    j += 1
                i += 1
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    def p5():
        tiempos = []
        tinicial = time.time()
        
        for n in range(1,1000):
            i = 1
            while (i < n):
                
                j = 1
                while (j < n):
                    print(n, i)
                    j = j * 2
                i += 1
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    print(
        "\n=== OPCIONES ===\n",
        "[1] Bloque de código 1\n",
        "[2] Bloque de código 2\n",
        "[3] Bloque de código 3\n",
        "[4] Bloque de código 4\n",
        "[5] Bloque de código 5\n",
        "[0] SALIR\n",
          )
    
    opcion = int(input("Ingresa una opción: "))
    if(opcion == 1):
        p1()
    elif(opcion == 2):
        p2()
    elif(opcion == 3):
        p3()
    elif(opcion == 4):
        p4()
    elif(opcion == 5):
        p5()
    elif(opcion == 0):
        print("FINALIZANDO...")
    else:
        print("[!] Opción inválida.")

           
main()