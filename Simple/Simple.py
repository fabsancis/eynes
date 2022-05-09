import os, random


# FUNCIONES ACCESORIAS


def genera_lista(list):
    nombre = ['Juan','Maria','Pedro','Claudia','Belen','Veronica','Nahuel','Nicolas','Frank','Judith']
    for i in range (len(list)):
        dic = {"Id": nombre[i], "Edad":random.randrange(1,100)}
        list[i] = dic 
    return list





def ordena_lista(list):
    diccionario_anterior ={"Id":"","Edad":0}
    diccionario_siguiente = {"Id":"","Edad":0}
    se_cambio = True
    while se_cambio:
        se_cambio = False
        i = 1
        while i < len(list):
            diccionario_anterior = list[i-1]
            diccionario_siguiente = list[i]
            edad_ant = diccionario_anterior["Edad"]
            edad_sig =  diccionario_siguiente["Edad"]

            if edad_ant < edad_sig:
                aux = list[i]
                list[i] = list[i-1]
                list[i-1] = aux
                se_cambio = True
			
            i = i +1
    return list





def mostrar_lista(list):
    for i in list:
        print(i)

        

# PROGRAMA PRINCIPAL

elementos = 10
diccionario = {"id":"","edad":0}
dic_lista = [diccionario]*elementos


genera_lista(dic_lista)
mostrar_lista(dic_lista)
print()
ordena_lista(dic_lista)
mostrar_lista(dic_lista)

