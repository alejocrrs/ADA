#TALLER 3 - MÉTODOS DE ORDENAMIENTO

#ALEJANDRO CÓRDOBA RÍOS
#SEBASTIÁN GONZÁLEZ TRUJILLO

from urllib.request import urlopen
import json
from metodos_ordenamiento import *

respuesta = urlopen("https://raw.githubusercontent.com/dwn84/ADA2022-2/main/little_data")

datos_json = json.loads(respuesta.read())

data = datos_json['data']
data0 = datos_json['data0']
data1 = datos_json['data1']
data2 = datos_json['data2']
data3 = datos_json['data3']
data4 = datos_json['data4']
data5 = datos_json['data5']
data6 = datos_json['data6']
data7 = datos_json['data7']
data8 = datos_json['data8']
data9 = datos_json['data9']
data10 = datos_json['data10']
data11 = datos_json['data11']


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

def analizar_data():
    pass

print(tiempo_ejecucion(buble_sort, data11))
    
