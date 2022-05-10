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
    
        for c in range (5):
            m[4,c] = 5 - c


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
                if consecutivos == 4:
                    return v

    return "No hay secuencia horizontal"
                
                    


def secuencia_horizontal_di(m,v):       # derecha a izquierda
    filas,columnas = np.shape(m)

    for f in range (filas-1,0,-1):
        consecutivos = 0
        v = [""]*4
        for c in range(columnas-1,0,-1):
            if m[f,c] + 1 == m[f, c - 1]:
                v[consecutivos] = "(" + str(f) + "," + str(c) + ")" 
                consecutivos = consecutivos + 1
                if consecutivos == 4:
                    return v

    return "No hay secuencia horizontal"


def secuencia_vertical_ab(m,v):
    pass

                
def muestra_vector(v):
    for i in range (len(v)):
        print(v[i])




# PROGRAMA PRINCIPAL


#Rpos = Record.create_type("Rpos","fila","columna",fila=0,columna=0)
#rvector = np.array([Rpos]*4)
vector = [""]*4
matriz = np.array([[0]*5]*5)


carga_matriz(matriz)
muestra_matriz(matriz)
carga_ultc(matriz)
print()
muestra_matriz(matriz)
print()


#print(secuencia_horizontal_id(matriz,vector))
print(secuencia_horizontal_di(matriz,vector))

    
