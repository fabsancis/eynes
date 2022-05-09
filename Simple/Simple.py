import os, random


# FUNCIONES ACCESORIAS


def genera_lista(list):
    nombre = ['Juan','Maria','Pedro','Claudia','Belen','Veronica','Nahuel','Nicolas','Frank','Judith']
    for i in range (len(list)):
        dic = {nombre[i]:random.randrange(1,100)}
        list[i] = dic 
        #print (list[i])
    return list


def mostrar_lista(list):
    for i in list:
        print(i)

        

# PROGRAMA PRINCIPAL

elementos = 10
diccionario = {"":0}
dic_lista = [diccionario]*elementos


genera_lista(dic_lista)
mostrar_lista(dic_lista)