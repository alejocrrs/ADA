# =============================================================================
# Análisis y Diseño de Algoritmos
# Taller 1: Complejidad algorítmica
# Alejandro Córdoba Ríos
# =============================================================================
import time
import matplotlib.pyplot as mpl

def main():
    
    def p1(l):
        tiempos = []
        def add_data_to_list(n,my_list,i):
            return my_list[:i] + [n] + my_list[i:]
            
        
        def add_data_to_all_positions(n,my_list):
            return [add_data_to_list(n,my_list,i) for i in range(len(my_list)+1)]
        
        def permutation(my_list):
            tinicial = time.time()
            if(len(my_list)==0):
                return [[]]
            else:
                a = sum(
                    [add_data_to_all_positions(my_list[0],lista_previa) 
                         for lista_previa in permutation(my_list[1:])],[])
                tfinal = time.time()
                duracion = tfinal - tinicial
                tiempos.append(duracion)
                return a
        
           
        [print(clave) for clave in permutation(l)]
        mpl.plot(tiempos)
        
    def p2(l):
        tiempos = []
        def heap_permutation(data, size):
            tinicial = time.time()
            if size == 1:
                print(data)
                return
            
            for i in range(size):
                heap_permutation(data, size-1)
                    
                if size & 1:
                    data[0], data[size-1] = data[size-1],data[0] 
                else:
                    data[i], data[size-1] = data[size-1],data[i]
            tfinal = time.time()
            duracion = tfinal - tinicial
            tiempos.append(duracion)
        
        heap_permutation(l, len(l))
        mpl.plot(tiempos)

    
    def p3(l):
        tiempos = []
        def permutations(iterable, r=None):
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = list(range(n))
            cycles = list(range(n, n-r, -1))
            yield tuple(pool[i] for i in indices[:r])
            while n:
                tinicial = time.time()
                for i in reversed(range(r)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:r])
                        break
                else:
                    return
                tfinal = time.time()
                duracion = tfinal - tinicial
                tiempos.append(duracion)
                
        [print(clave) for clave in permutations(l)]
        mpl.plot(tiempos)
    
    l = [1,2,3,4,5,6,7,8]
    
    print(
        "\n=== OPCIONES ===\n",
        "[1] Permutation\n",
        "[2] Heap Permutation\n",
        "[3] Permutations (Itertools)\n",
        "[0] SALIR\n",
          )
    
    opcion = int(input("Ingresa una opción: "))
    if(opcion == 1):
        p1(l)
    elif(opcion == 2):
        p2(l)
    elif(opcion == 3):
        p3(l)
    elif(opcion == 0):
        print("FINALIZANDO...")
    else:
        print("[!] Opción inválida.")

           
main()