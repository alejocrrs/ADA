# =============================================================================
# Análisis y Diseño de Algoritmos
# Taller 1: Complejidad algorítmica
# Alejandro Córdoba Ríos
# =============================================================================
import time
import matplotlib.pyplot as grafico

def main():
    
    def p1(i, n):
        tiempos = []
        
        while (i < n):
            tinicial = time.time()
            
            print(i)
            i += 1
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
            
        
    def p2(i, n):
        tiempos = []
        
        while (i < n):
            tinicial = time.time()
            
            c = i
            while (c > 0):
                print(i)
                c /= 2
            i += 1
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    def p3(i, n):
        tiempos = []
        
        while (i < n):
            tinicial = time.time()
            
            print(i)
            i = i * 2
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    def p4(i, n):
        tiempos = []
        
        while (i < n):
            tinicial = time.time()
            
            j = 1
            while (j < n):
                print(i)
                j += 1
            i += 1
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    def p5(i, n):
        tiempos = []
        
        while (i < n):
            tinicial = time.time()
            
            j = 1
            while (j < n):
                print(i)
                j = j * 2
            i += 1
            
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
            
        grafico.plot(tiempos)
        print(f"Duración: {duracion}")
    
    i = 1
    n = 1000
    #n = 10000
    #n = 100000
    
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
        p1(i, n)
    elif(opcion == 2):
        p2(i, n)
    elif(opcion == 3):
        p3(i, n)
    elif(opcion == 4):
        p4(i, n)
    elif(opcion == 5):
        p5(i, n)
    elif(opcion == 0):
        print("FINALIZANDO...")
    else:
        print("[!] Opción inválida.")

           
main()