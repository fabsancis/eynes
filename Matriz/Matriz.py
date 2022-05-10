import random
import numpy as np



# FUNCIONES ACCESORIAS

def carga_matriz(m):
    filas,columnas = np.shape(m)
    for f in range (filas):
        for c in range (columnas):
            m[f,c] = random.randint(1,4)


def carga_secuencia(m):
    m[0,0] = 1
    m[0,1] = 2
    m[0,2] = 3
    m[0,3] = 4
    m[0,4] = 1
        


def muestra_matriz(m):
    filas,columnas = np.shape(m)
    for f in range (filas):
        for c in range (columnas):
            print(m[f,c], end = " ")
        print()
    print()


def secuencia_horizontal_id(m):     # izquierda a derecha       OKKKKKKK
    filas,columnas = np.shape(m)

    for f in range (filas):
        consecutivos = 0
        v = [""]*4
        for c in range (columnas-1): 
            if c == 0:
                if m[f,c] + 1 == m[f, c + 1]:
                    v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                    consecutivos = consecutivos + 1
            else:
                if consecutivos == 0:
                    if m[f,c] + 1 == m[f, c + 1]:
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                        consecutivos = consecutivos + 1
                else:
                    if m[f,c] + 1 == m[f, c + 1] and m[f,c] - 1 == m[f, c - 1]:
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                        consecutivos = consecutivos + 1
                        if consecutivos == 3:
                            v[consecutivos] =  "(" + str(f) + "," + str(c+1) + ")"
                            return v


                

    return "No hay secuencia"
                
                    


def secuencia_horizontal_di(m):       # derecha a izquierda
    filas,columnas = np.shape(m)

    for f in range (filas-1,-1,-1):
        consecutivos = 0
        v = [""]*4
        for c in range(columnas-1,0,-1):
            if c == 4:
                if m[f,c] + 1 == m[f, c - 1]:
                    v[consecutivos] = "(" + str(f) + "," + str(c) + ")" 
                    consecutivos = consecutivos + 1
            else:
                if consecutivos == 0:
                    if m[f,c] + 1 == m[f, c - 1]:
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")" 
                        consecutivos = consecutivos + 1
                else:
                    if m[f,c] + 1 == m[f, c - 1] and m[f,c] - 1 == m[f, c + 1]:
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")" 
                        consecutivos = consecutivos + 1
                        if consecutivos == 3:
                            v[consecutivos] = "(" + str(f) + "," + str(c-1) + ")" 
                            return v



    return "No hay secuencia."




def secuencia_vertical_ab(m):         # arriba a abajo  
    filas, columnas = np.shape(m)

    for c in range(columnas):
        consecutivos = 0
        v = [""]*4
        for f in range (filas-1):
            if f == 0:
                if m[f,c] + 1 == m[f + 1, c]:
                    v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                    consecutivos = consecutivos + 1
            else:
                if consecutivos == 0:
                    if m[f,c] + 1 == m[f + 1, c] :
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                        consecutivos = consecutivos + 1
                else:
                    if m[f,c] + 1 == m[f + 1, c] and m[f,c] - 1 == m[f-1,c]:
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                        consecutivos = consecutivos + 1
                        if consecutivos == 3: 
                            v[consecutivos] = "(" + str(f+1) + "," + str(c) + ")"
                            return v

    return "No hay secuencia."



def secuencia_vertical_ba(m):           # abajo a arriba    
    filas, columnas = np.shape(m)

    for c in range(columnas-1,-1,-1):
        consecutivos = 0
        v = [""]*4
        for f in range (filas-1,0,-1):
            if f == 4:
                if m[f,c] + 1 == m[f - 1, c]:
                    v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                    consecutivos = consecutivos + 1
            else:
                if consecutivos == 0:
                    if m[f,c] + 1 == m[f - 1, c]:
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                        consecutivos = consecutivos + 1
                else:
                    if m[f,c] + 1 == m[f - 1, c] and m[f,c] - 1 == m[f + 1, c]:
                        v[consecutivos] = "(" + str(f) + "," + str(c) + ")"
                        consecutivos = consecutivos + 1
                        if consecutivos == 3:
                            v[consecutivos] = "(" + str(f-1) + "," + str(c) + ")"
                            return v

    return "No hay secuencia."




def muestra_vector(v):
    for i in range (len(v)):
        print(v[i])




# PROGRAMA PRINCIPAL

matriz = np.array([[0]*5]*5)

print()
carga_matriz(matriz)
print("Matriz randomizada 5 x 5.")
print()
muestra_matriz(matriz)
#carga_secuencia(matriz)
print()


print("Secuencia Horizontal de Izquierda a Derecha: " + str(secuencia_horizontal_id(matriz)))
print()
print("Secuencia Horizontal de Derecha a Izquierda: " + str(secuencia_horizontal_di(matriz)))
print()
print("Secuencia Vertical de Arriba a Abajo:        " + str(secuencia_vertical_ab(matriz)))
print()
print("Secuencia Vertical de Abajo a Arriba:        " + str(secuencia_vertical_ba(matriz)))
print()

    
