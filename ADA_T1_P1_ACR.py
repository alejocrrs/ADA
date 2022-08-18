# =============================================================================
# Análisis y Diseño de Algoritmos
# Taller 1: Complejidad algorítmica
# Alejandro Córdoba Ríos
# =============================================================================

class Persona:
    def __init__(self, nombre, genero, ingles):
        self.nombre = nombre
        self.genero = genero
        self.ingles = ingles
    

def conjunto_potencia(c):
    if(len(c)==0):
        return [[]]
    else:
        ultimo = conjunto_potencia(c[:-1])
        return ultimo + [listaC + [c[-1]] for listaC in ultimo]
        
def combinaciones(lista, r = None):
    if r is None:
        r = len(lista)
    return [p for p in conjunto_potencia(lista) if(len(p)==r)]        

def filtrar_minimo_2_mujeres(combinaciones):
    lista_filtrada = []
    for lista_personas in combinaciones:
        mujeres = 0
        for persona in lista_personas:
            if persona.genero == "F":
                mujeres += 1
        if mujeres >= 2:
            lista_filtrada.append(lista_personas)
    return lista_filtrada

def filtrar_minimo_2_mujeres(combinaciones):
    lista_filtrada = []
    for lista_personas in combinaciones:
        mujeres = 0
        for persona in lista_personas:
            if persona.genero == "F":
                mujeres += 1
        if mujeres >= 2:
            lista_filtrada.append(lista_personas)
    return lista_filtrada

def filtrar_solo_hombres(combinaciones):
    lista_filtrada = []
    for lista_personas in combinaciones:
        hombres = 0
        for persona in lista_personas:
            if persona.genero == "M":
                hombres += 1
        if hombres == len(lista_personas):
            lista_filtrada.append(lista_personas)
    return lista_filtrada

def filtrar_aaron(combinaciones):
    lista_filtrada = []
    for lista_personas in combinaciones:
        aaron = False
        for persona in lista_personas:
            if persona.nombre == "Aaron":
                aaron = True
        if aaron is True:
            lista_filtrada.append(lista_personas)
    return lista_filtrada

def filtrar_aaron_con_nivel_bajo(combinaciones):
    lista_inicial = filtrar_aaron(combinaciones)
    lista_filtrada = []
    
    for lista_personas in lista_inicial:
        personas_nivel_bajo = 0
        for persona in lista_personas:
            if persona.nombre != "Aaron" and persona.ingles == "B":
                personas_nivel_bajo += 1
        if personas_nivel_bajo == 2:
            lista_filtrada.append(lista_personas)
    return lista_filtrada

def nombres_personas(personas):
    lista_grande_personas = []
    for lista in personas:
        lista_personas=[]
        for persona in lista:
            lista_personas.append(persona.nombre)
        lista_grande_personas.append(lista_personas)
    return lista_grande_personas

def main():
    import time
    
    def p1():
        tiempo_inicial = time.time()
        [print(f"<{n+1}> {lista}") for n, lista in enumerate(nombres_personas(filtrar_minimo_2_mujeres(combinaciones_3)))]
        tiempo_final = time.time()
        print(f"TIEMPO DE EJECUCIÓN: {tiempo_final - tiempo_inicial}")
        
    def p2():
        tiempo_inicial = time.time()
        [print(f"<{n+1}> {lista}") for n, lista in enumerate(nombres_personas(filtrar_solo_hombres(combinaciones_3)))]
        tiempo_final = time.time()
        print(f"TIEMPO DE EJECUCIÓN: {tiempo_final - tiempo_inicial}")
    
    def p3():
        tiempo_inicial = time.time()
        [print(f"<{n+1}> {lista}") for n, lista in enumerate(nombres_personas(filtrar_aaron_con_nivel_bajo(combinaciones_3)))]
        tiempo_final = time.time()
        print(f"TIEMPO DE EJECUCIÓN: {tiempo_final - tiempo_inicial}")
    
    personas = [
        Persona("Ana", "F", "A"),
        Persona("Aaron", "M", "A"),
        Persona("Albert", "M", "M"),
        Persona("Amanda", "F", "B"),
        Persona("Alex", "M", "B"),
        Persona("Alexandra", "F", "M"),
        Persona("Abelardo", "M", "A"),
        Persona("Alphonse", "M", "B"),
        Persona("Abril", "F", "B"),
        Persona("Adriana", "F", "M"),
        Persona("Anya", "F", "A")
        ]
    
    combinaciones_3 = combinaciones(personas, 3)
    
    while(True):
        print(
            "\n=== OPCIONES ===\n",
            "[1] Grupos con mínimo dos mujeres\n",
            "[2] Grupos exclusivos de hombres\n",
            "[3] Grupos donde Aaron se relacione con personas con nivel de inglés 'Bajo'\n",
            "[0] SALIR\n",
              )
        opcion = int(input("Ingresa una opción: "))
        
        if(opcion == 1):
            p1()
        elif(opcion == 2):
            p2()
        elif(opcion == 3):
            p3()
        elif(opcion == 0):
            print("FINALIZANDO...")
            break
        else:
            print("[!] Opción inválida.")

           
main()