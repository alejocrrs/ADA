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
    #filtrar el conjunto potencia por el valor r (opcion 1)
    #return list(filter(lambda x: (len(x)==r), conjunto_potencia(lista))) 
    #filtrar el conjunto potencia por el valor r (opcion 2)
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

def nombres_personas(personas):
    lista_grande_personas = []
    for lista in personas:
        lista_personas=[]
        for persona in lista:
            lista_personas.append(persona.nombre)
        lista_grande_personas.append(lista_personas)
    return lista_grande_personas


def main():
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
    
    print(nombres_personas(filtrar_minimo_2_mujeres(combinaciones_3)))
    
main()