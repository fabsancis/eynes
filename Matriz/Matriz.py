


# FUNCIONES ACCESORIAS

def carga_matriz(m):
    filas,columnas = np.shape(m)
    for f in range (filas):
        for c in range (columnas):
            m[f,c] = random.randint(1,4)


def muestra_matriz(m):
    filas,columnas = np.shape(m)
    for f in range (filas):
        for c in range (columnas):
            print(m[f,c], end = " ")
        print()
    print()





# PROGRAMA PRINCIPAL
import random
import numpy as np
matriz = np.array([[0]*5]*5)

carga_matriz(matriz)
muestra_matriz(matriz)

