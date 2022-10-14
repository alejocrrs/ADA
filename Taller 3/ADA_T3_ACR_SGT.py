#TALLER 3 - MÉTODOS DE ORDENAMIENTO

#ALEJANDRO CÓRDOBA RÍOS
#SEBASTIÁN GONZÁLEZ TRUJILLO

from urllib.request import urlopen
import json
from metodos_ordenamiento import *

#Incluir archivo metodos_ordenamiento.py en la misma carpeta
#Enlace del archivo: https://github.com/alejocrrs/ADA/blob/main/Taller%203/metodos_ordenamiento.py

def datos():
    respuesta = urlopen("https://raw.githubusercontent.com/dwn84/ADA2022-2/main/little_data")
    return json.loads(respuesta.read())

def solo_enteros(lista):
    for e in lista:
        if type(e) is not int:
            return False
    return True


def solo_positivos(lista):
    if solo_enteros(lista):
        for e in lista:
            if e < 0:
                return False
        return True
    else:
        return False


def esta_ordenado(lista):
    if solo_enteros(lista):
        i = 1
        while i < len(lista): 
            if lista[i] < lista[i - 1]: 
                return False
            i += 1
          
        return True
    else:
        return False


def main():
    funcs = {"Bubble": bubble_sort, 
             "Insertion": insertion_sort, 
             "Selection": selection_sort, 
             "Quick": quick_sort,
             "Merge": merge_sort, 
             "Heap": heap_sort, 
             "Counting": counting_sort,
             "Radix": radix_sort}
    
    for key in datos():
        print(f"\nPARA LA LISTA '{key}' CON {len(datos()[key])} ELEMENTOS:")
        
        if solo_enteros(datos()[key]):
            for keyf in funcs:
                if (keyf == "Counting" or keyf == "Radix") and (not solo_positivos(datos()[key])):
                    print(f"    # {keyf}: [!] ERROR: Lista con enteros negativos")
                elif (keyf == "Quick" and (len(datos()[key]) > 2000)):
                    lista = (datos()[key])[:2000]
                    ordi = esta_ordenado(lista)
                    tiempo = round(tiempo_ejecucion(funcs[keyf], lista), 5)
                    ordf = esta_ordenado(lista)
                    print(f"    # {keyf}: {tiempo} (Antes: {ordi} | Después: {ordf}) [PRIMEROS 2000 ELEMENTOS]")
                else:
                    lista = datos()[key]
                    ordi = esta_ordenado(lista)
                    tiempo = round(tiempo_ejecucion(funcs[keyf], lista), 5)
                    ordf = esta_ordenado(lista)
                    print(f"    # {keyf}: {tiempo} (Antes: {ordi} | Después: {ordf})")
        else:
            print("  [!] ERROR: La lista tiene valores que no son enteros")

main()