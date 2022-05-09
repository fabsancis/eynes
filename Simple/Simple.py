import random


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
			
            i = i + 1
    return list



def mas_joven_y_grande(list):
    diccionario = {"Id":"","Edad":0}
    mas_joven = 1000
    mas_grande = 0
    id_mas_joven = ""
    id_mas_grande = ""

    for i in range (len(list)):
        diccionario = list[i]
        edad = diccionario["Edad"]
        id   = diccionario["Id"]

        if mas_joven > edad:
            mas_joven     = edad
            id_mas_joven  = id
            
        if mas_grande < edad:
            mas_grande    = edad
            id_mas_grande = id 

    s = "La persona más grande es {} y la personas mas chica es {}.".format(id_mas_grande,id_mas_joven)

    return s 




def mostrar_lista(list):
    for i in list:
        print(i)

        

# PROGRAMA PRINCIPAL

elementos = 10
diccionario = {"Id":"","Edad":0}
dic_lista = [diccionario]*elementos


genera_lista(dic_lista)
mostrar_lista(dic_lista)
print()
ordena_lista(dic_lista)
mostrar_lista(dic_lista)
print()
print(mas_joven_y_grande(dic_lista))
