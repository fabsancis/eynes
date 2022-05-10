import random
from sre_constants import NOT_LITERAL
import numpy as np
from pyrecord import Record


# FUNCIONES ACCESORIAS

def carga_matriz(m):
    filas,columnas = np.shape(m)
    for f in range (4):
        for c in range (columnas):
            m[f,c] = random.randint(1,4)


def carga_ultc(m):
    m[4,0] = 4
    m[4,1] = 3
    m[4,2] = 2 
    m[4,3] = 1
    m[4,4] = 6
        


def muestra_matriz(m):
    filas,columnas = np.shape(m)
    for f in range (filas):
        for c in range (columnas):
            print(m[f,c], end = " ")
        print()
    print()


def secuencia_horizontal_id(m,v):     # izquierda a derecha
    filas,columnas = np.shape(m)

    for f in range (filas):
        consecutivos = 0
        v = [""]*4
        for c in range (columnas-1):
            if m[f,c] + 1 == m[f, c + 1]:
                v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                consecutivos = consecutivos + 1
                if consecutivos == 3:
                    v[consecutivos] =  "(" + str(f) + "," + str(c+1) + ")"
                    return v

    return "No hay secuencia horizontal de izquierda a derecha"
                
                    


def secuencia_horizontal_di(m,v):       # derecha a izquierda
    filas,columnas = np.shape(m)

    for f in range (filas-1,0,-1):
        consecutivos = 0
        v = [""]*4
        for c in range(columnas-1,0,-1):
            if m[f,c] + 1 == m[f, c - 1]:
                v[consecutivos] = "(" + str(f) + "," + str(c) + ")" 
                consecutivos = consecutivos + 1
                if consecutivos == 3:
                    v[consecutivos] = "(" + str(f) + "," + str(c-1) + ")" 
                    return v

    return "No hay secuencia horizontal de derecha a izquierda"




def secuencia_vertical_ab(m,v):
    filas, columnas = np.shape(m)

    for c in range(columnas):
        consecutivos = 0
        v = [""]*4
        for f in range (filas-1):
            if m[f,c] + 1 == m[f + 1, c]:
                v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                consecutivos = consecutivos + 1
                if consecutivos == 3: 
                    v[consecutivos] = "(" + str(f+1) + "," + str(c) + ")"
                    return v

    return "No hay secuencia vertical de arriba a abajo"




def muestra_vector(v):
    for i in range (len(v)):
        print(v[i])




# PROGRAMA PRINCIPAL

vector = [""]*4
matriz = np.array([[0]*5]*5)


carga_matriz(matriz)
muestra_matriz(matriz)
carga_ultc(matriz)
print()
muestra_matriz(matriz)
print()


print(secuencia_horizontal_id(matriz,vector))
print(secuencia_horizontal_di(matriz,vector))
print(secuencia_vertical_ab(matriz,vector))

    
