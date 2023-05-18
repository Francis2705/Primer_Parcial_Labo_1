import re
import datetime
import json
from unidecode import unidecode

#Case 1
def sacar_espacios_caracteristica_minusculas(lista: list):
    """ Brief: Le saca los posibles espacios a la izquierda y/o derecha del string. El codigo solo se ejecuta si la lista pasada por parametro tiene al menos
    un elemento"""
    """ Parameters: lista """
    """ Return: Devuelve la nueva lista, y sus valores ya no tienen espacios a sus costados. """
    if len(lista) != 0:
        for i in range(len(lista)): #le saco el espacio a la caracteristica y la reemplazo
            caracteristica_sin_espacios = lista[i].strip().lower()
            lista[i] = caracteristica_sin_espacios
        return lista
def parser_csv(archivo: str):
    """ Brief: Toma un archivo.csv el cual va a ser descompuesto por partes. Se analiza linea por linea, y por cada linea se hace un split cuando
    se encuentre la ','. Eso genera que se separe en una lista, cada carateristica especifica. Luego, se crea un diccionario para cada personaje, el cual
    va a contener determinadas keys. Se castean los datos numericos y las razas y las habilidades son analizadas en base a si existe mas de una. Se utilizan 
    expresiones regulares para lograr un correcto resultado de las razas y habilidades. El codigo solo se ejecuta, si el archivo contiene la secuencia '.csv' """
    """ Parameters: archivo """
    """ Return: Se retorna la lista completa, la cual contiene todos los datos del archivo indicado. En base a esta lista, se trabajara en los siguientes puntos. """
    if '.csv' in archivo:
        lista_completa = []
        with open(archivo, 'r', encoding = 'utf-8') as un_archivo:
            for linea in un_archivo:
                lista = re.split(',', linea)
                un_diccionario = {}
                un_diccionario['id'] = int(lista[0])
                un_diccionario['nombre'] = lista[1].strip().lower()
                lista_razas = re.split('-', lista[2])
                nueva_lista_razas = sacar_espacios_caracteristica_minusculas(lista_razas)
                un_diccionario['raza'] = nueva_lista_razas
                un_diccionario['poder_pelea'] = int(lista[3])
                un_diccionario['poder_ataque'] = int(lista[4])
                lista_habilidades_separadas = re.split(r"[|$%]+", lista[5]) #separo habilidades por esa secuencia
                string_sin_contrabarra = re.sub(r'\\n','', lista_habilidades_separadas[-1]) #elimino el '\n' que aparece en la ult posicion
                lista_habilidades_separadas[-1] = string_sin_contrabarra
                nueva_lista = sacar_espacios_caracteristica_minusculas(lista_habilidades_separadas)
                un_diccionario['habilidades'] = nueva_lista
                lista_completa.append(un_diccionario)
        return lista_completa
#Case 2
def contar_caracteristica(lista: list, key: str):
    """ Brief: Se crea un diccionario, el cual va a contener como keys, los valores de cada key pasada como parametro, respecto de los diccionarios que esten dentro
    de la lista pasada como parametro. Se toma el valor de cada key, y se itera a traves de ese valor, el cual es una lista. Se pregunta si el/los datos 
    pertenecientes a ese valor, ya existen en el diccionario. Si es asi, se le suma uno, y sino, se crea una key con ese nombre y se le asigna como valor un 1. 
    El codigo solo se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, key """
    """ Return: Devuelve un diccionario con sus respectivas keys y un valor numerico representando la cantidad de personajes que cumplen con esa key. """
    if len(lista) != 0:
        diccionario_caracteristica = {}
        for personaje in lista:
            valor_de_caracteristica = personaje[key]
            for dato in valor_de_caracteristica:
                if dato not in diccionario_caracteristica:
                    diccionario_caracteristica[dato] = 1
                else:
                    diccionario_caracteristica[dato] += 1
        return diccionario_caracteristica
def mostrar_lista(diccionario_prints: dict):
    """ Brief: Se recorre el diccionario, haciendo un print el cual muestra cuantos valores coinciden con la key evaluada. Esta funcion, esta en relacion de la
    funcion 'contar_caracteristia'. El codigo solo se ejecuta si el diccionario pasado por parametro no esta vacio """
    """ Parameters: diccionario_prints """
    """ Return: No tiene """
    if len(diccionario_prints) != 0:
        for key in diccionario_prints:
            print(f"'{key}': {diccionario_prints[key]}")
#Case 3
def listar_personajes_por_caracateristica(lista: list, caracateristica: str, key1: str, key2: str):
    """ Brief: Se crea un diccionario, el cual va a contener como keys, los valores de cada caracteristica pasada como parametro, respecto de los diccionarios 
    que esten dentro de la lista pasada como parametro. Se toma el valor de cada key, y se itera a traves de ese valor el cual es una lista. Se pregunta si 
    el/los datos pertenecientes a ese valor, ya existen en el diccionario. Si ya existe, se agrega como valor de la key, el valor de la key1 y key2 pasadas 
    por parametro. Si no existe, se crea una key con ese valor y se le asigna el valor de la key1 y key2 pasadas por parametro. El codigo solo se ejecuta 
    si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, caracteristica, key1, key2 """
    """ Return: Devuelve un diccionario con sus respectivas keys como valor de esas keys, los valores solicitados """
    if len(lista) != 0:
        diccionario_por_caracteristica = {}
        for personaje in lista:
            valor_de_caracteristica = personaje[caracateristica] #siempre va a ser una lista
            for dato in valor_de_caracteristica:
                if dato in diccionario_por_caracteristica:
                    diccionario_por_caracteristica[dato].append(personaje[key1]) #el append se va a poder hacer, porque ya se ejecuto el else
                    diccionario_por_caracteristica[dato].append(personaje[key2])
                else:
                    diccionario_por_caracteristica[dato] = [personaje[key1], personaje[key2]] #el valor de esa key, siempre es una lista
        return diccionario_por_caracteristica
def mostrar_lista_separada(diccionario_a_separar: dict):
    """ Brief: Se recorre el diccionario, haciendo un print el cual muestra los personajes que cumplen con esa key, y a parte, como se sabe que el nombre esta en
    la primer posicion, y el poder de ataque en la segunda, se usa otro for para printear esos datos. El codigo solo se ejecuta si el diccionario 
    pasado por parametro no esta vacio """
    """ Parameters: diccionario_a_separar """
    """ Return: No tiene """
    if len(diccionario_a_separar) != 0:
        for dato in diccionario_a_separar:
            print(f"\n'{dato}':")
            for valor in diccionario_a_separar[dato]:
                if type(valor) == str:
                    nombre = valor
                    print(f"{nombre}", end = "")
                else:
                    poder = valor
                    print(f" | {poder}")
#Case 4
def promediar_dos_datos(num1: float, num2: float):
    """ Brief: Se hace el promedio de dos numeros """
    """ Parameters: num1, num2 """
    """ Return: Retorna el promedio realizado """
    suma = num1 + num2
    promedio = suma / 2
    return promedio
def mostrar_personajes_por_caracteristica_con_datos(lista: list, caracteristica_especifica_validada: str, key: str, separador: str):
    """ Brief: Se recorre el diccionario, haciendo un print el cual muestra cuantos valores coinciden con la key evaluada. Se pregunta si la caracteristica
    ingresada existe dentro de los diccionarios que estan dentro de la lista, en determinanda key, y si existe se ejecutan los prints con la informacion solicitada.
    El codigo solo se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, caracteristica_especifica_validada, key, separador """
    """ Return: No tiene """
    if len(lista) != 0:
        for personaje in lista:
            if caracteristica_especifica_validada in personaje[key]:
                print(f"\nNombre: {personaje['nombre']}")
                print(f"Raza: {separador.join(personaje['raza'])}")
                promedio = promediar_dos_datos(personaje['poder_pelea'], personaje['poder_ataque'])
                print(f"Promedio entre poder de pelea y poder de ataque: {promedio}\n")
#Case 5
def buscar_igualdad_nombre(lista: list, id: int):
    """ Brief: Se busca el nombre por el id del personaje. El codigo solo se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, id """
    """ Return: Retorna el nombre del personaje """
    if len(lista) != 0:
        for personaje in lista:
                if id == personaje['id']:
                    nombre = personaje['nombre']
        return nombre
def buscar_poder(lista: list, nombre_o_id: str|int, key_poder: int):
    """ Brief: Se busca el poder de ataque por el id del personaje o por el nombre. Se pregunta si 'nombre_o_id' es un str, ya que en ese caso se busca por el 
    nombre. Caso contrario, se busca por el id. El codigo solo se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, nombre_o_id, key_poder """
    """ Return: Retorna el poder de algun personaje """
    if len(lista) != 0:
        for personaje in lista:
            if type(nombre_o_id) == str:
                if nombre_o_id == personaje['nombre']:
                    poder_de_ataque = personaje[key_poder]
            else:
                if nombre_o_id == personaje['id']:
                    poder_de_ataque = personaje[key_poder]
    return poder_de_ataque
def guardar_pelea(poder_selec: int, poder_ale: int, string_selec: str, string_ale: str):
    """ Brief: Evalua tres casos posibles; si el poder perteneciente al nombre que eligio el usuario, es mayor al poder perteneciente al id aleatorio que se
    genero, se anexa un archivo (o se crea si es la primera vez que se ingresa), el cual contiene, la fecha de la pelea, y quien gano y quien perdio. El otro caso
    posible, es que sea menor, en este caso se repite el proceso explicado anteriormente, y se registra el ganador y el perdedor. Por ultimo, se evalua un empate,
    y se guarda en el archivo quienes empataron. """
    """ Parameters: poder_selec, poder_ale, string_selec, string_ale """
    """ Return: No tiene retorno """
    if poder_selec > poder_ale:
        with open('peleas.txt', 'a', encoding = 'utf-8') as un_archivo:
            un_archivo.write(f'{datetime.datetime.now()} - Gano {string_selec} contra {string_ale}\n')
    elif poder_selec < poder_ale:
        with open('peleas.txt', 'a', encoding = 'utf-8') as un_archivo:
            un_archivo.write(f'{datetime.datetime.now()} - Gano {string_ale} contra {string_selec}\n')
    else:
        with open('peleas.txt', 'a', encoding = 'utf-8') as un_archivo:
            un_archivo.write(f'{datetime.datetime.now()} - Empataron {string_selec} y {string_ale}\n')
#Case 6 y 7
def crear_nombre_json(raza_ingresada1: str, habilidad_ingresada1: str):
    """ Brief: Se crea el nombre del archivo con el formato solicitado. """
    """ Parameters: raza_ingresada1, habilidad_ingresada1 """
    """ Return: Retorna el nombre del archivo con el formato requerido """
    string_unido = raza_ingresada1 + ' ' + habilidad_ingresada1
    lista_nuevo_string = re.split(' ', string_unido)
    for i in range(len(lista_nuevo_string)):
        primera_mayus = lista_nuevo_string[i].capitalize()
        lista_nuevo_string[i] = primera_mayus
    separador = '_'
    nombre_archivo = separador.join(lista_nuevo_string)
    return  nombre_archivo
def crear_json(lista: list, raza_ingresada: str, habilidad_ingresada: str):
    """ Brief: Se crea un diccionario, el cual va a tener como key 'data', y 'data' va a tener como valor una lista. Dentro de esa lista, si la raza ingresada 
    y la habilidad ingresada coinciden en el mismo personaje, se crea un diccionario para este y se guardan los datos pedidos, exeptuando la habilidad ingresada. 
    Si sucede el caso de que exista una sola habilidad, esta se elimina y no se crea ninguna key 'habilidades_especificas'. Finalmente, se crea 
    (o se sobreescribe sino es la primera vez que se ingreso) un archivo .json en el cual se guarda el diccionario creado con el/los diccionarios agregados,
    los cuales estan dentro de una lista. El codigo solo se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, raza_ingresada, habilidad_ingresada """
    """ Return: Solo se retorna el diccionario si existe la raza ingresada y la habilidad ingresada en el mismo personaje. Sino, se retorna None """
    if len(lista) != 0:
        nombre_del_archivo = crear_nombre_json(raza_ingresada, habilidad_ingresada)
        diccionario_general = {}
        diccionario_general['data'] = []
        flag_ingreso = False
        for personaje in lista:
            diccionario_especifico = {} #este va aca porque nose cuantos personajes se van a agregar, es decir, cuantos diccionarios voy a necesitar
            if raza_ingresada in personaje['raza'] and habilidad_ingresada in personaje['habilidades']:
                flag_ingreso = True
                diccionario_especifico['nombre_especifico'] = personaje['nombre']
                diccionario_especifico['poder_ataque_especifico'] = personaje['poder_ataque']
                if len(personaje['habilidades']) > 1: #si tiene mas de una habilidad, creo la key habilidades, sino no
                    diccionario_especifico['habilidades_especificas'] = []
                    for habilidad in personaje['habilidades']:
                        if habilidad != habilidad_ingresada:
                            diccionario_especifico['habilidades_especificas'].append(habilidad)
                diccionario_general['data'].append(diccionario_especifico)
                with open(f'{nombre_del_archivo}.json', 'w', encoding = 'utf-8') as mi_archivo:
                    json.dump(diccionario_general, mi_archivo, indent = 4)
        if flag_ingreso == False:
            return None
        else:
            print("Archivo guardado con exito")
            return diccionario_general
def leer_json(diccionario: dict, separador: str):
    """ Brief: Se recorrer el diccionario, priteando con el formato solicitado la informacion existente. El codigo solo se ejecuta si el diccionario 
    pasado por parametro tiene al menos un elemento """
    """ Parameters: lista, separador """
    """ Return: No tiene """
    if len(diccionario) != 0:
        for personaje in diccionario['data']:
            if 'habilidades_especificas' in personaje:
                print(f"{personaje['nombre_especifico']} - {personaje['poder_ataque_especifico']} - {separador.join(personaje['habilidades_especificas'])}")
            else:
                print(f"{personaje['nombre_especifico']} - {personaje['poder_ataque_especifico']}")
#Case 8
def incrementar_poderes(lista: list, key: str, string_existente: str):
    """ Brief: Incrementa los poderes de los personajes de cierta caracteristica y agrega una habilidad especifica. El codigo solo se ejecuta si la 
    lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, key, string_existente """
    """ Return: Retorna los personajes que fueron modificados y sus datos """
    if len(lista) != 0:
        lista_nuevos_nombres = []
        for personaje in lista:
            if string_existente in personaje[key]:
                personaje_diccionario = {}
                personaje_diccionario['id'] = personaje['id']
                personaje_diccionario['nombre'] = personaje['nombre']
                personaje_diccionario['raza'] = personaje['raza']
                personaje['poder_pelea'] = personaje['poder_pelea'] + personaje['poder_pelea'] * 0.5
                personaje_diccionario['poder_pelea'] = personaje['poder_pelea']
                personaje['poder_ataque'] = personaje['poder_ataque'] + personaje['poder_ataque'] * 0.7
                personaje_diccionario['poder_ataque'] = personaje['poder_ataque']
                personaje['habilidades'].append('transformación nivel dios')
                personaje_diccionario['habilidades'] = personaje['habilidades']
                lista_nuevos_nombres.append(personaje_diccionario)
        return lista_nuevos_nombres
def hacer_csv_modificados(lista: list, separador: str):
    """ Brief: Crea un archivo csv en el cual van a estar los datos de los personajes que sufrieron una modificacion de sus poderes y habilidades.
    El codigo solo se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, separador """
    """ Return: No tiene """
    if len(lista) != 0:
        with open('personajes_agregados.csv', 'w', encoding = 'utf-8') as mi_archivo:
            for personaje in lista:
                nuevo_registro = '\n{0},{1},{2},{3},{4},{5}'.format(personaje['id'],personaje['nombre'],personaje['raza'][0],
                                                                    personaje['poder_pelea'],personaje['poder_ataque'], separador.join(personaje['habilidades']))
                mi_archivo.write(nuevo_registro)
#Case 9
def crear_diccionario_caracteristica_personajes(lista: list, key_principal: str):
    """ Brief: Crea un diccionario, el cual va a tener como keys, los valores principales que identifican a los personajes. Esas keys, a su vez, van a tener
    como valor, una lista, la cual va a tener como unico valor, un diccionario, en el cual se va a almacenar la informacion requerida. Se toma el valor del
    personaje en la key_principal, y se recorre; a su vez, se evalua si ya existe en el diccionario principal (es decir, el que va a almacenar toda la informacion).
    Si no existe, se crea una lista, la cual va a contener un diccionario con los datos pedidos del personaje. Si ya existe, esos datos van a ser modificados y
    sobreescritos. Se hace uso de diccionarios y listas para un correcto orden de la informacion, y se usa un modelo similiar al formato JSON. El codigo solo 
    se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: lista, key_principal """
    """ Return: Retorna el diccionario con todos los datos """
    if len(lista) != 0:
        diccionario_de_key_principal = {}
        for personaje in lista:
            datos_varios = personaje[key_principal]
            for dato in datos_varios:
                if dato not in diccionario_de_key_principal:
                    diccionario_de_key_principal[dato] = []
                    un_diccionario = {}
                    un_diccionario['cantidad'] = 1
                    un_diccionario['nombres'] = []
                    un_diccionario['nombres'].append(personaje['nombre'])
                    un_diccionario['poder_y_ataque'] = []
                    un_diccionario['poder_y_ataque'].append(personaje['poder_ataque'])
                    diccionario_de_key_principal[dato].append(un_diccionario)
                else:
                    for diccionario in diccionario_de_key_principal[dato]:
                        diccionario['cantidad'] += 1
                        diccionario['nombres'].append(personaje['nombre'])
                        diccionario['poder_y_ataque'].append(personaje['poder_ataque'])
        return diccionario_de_key_principal
def mostrar_diccionario_completo(diccionario_completo: dict):
    """ Brief: Muestra el diccionario recibido con sus datos. Se hace uso de listas paralelas, ya que la cantidad de nombres es igual a la cantidad de poderes.
    El codigo solo se ejecuta si el diccionario pasado por parametro tiene al menos un elemento """
    """ Parameters: diccionario_completo """
    """ Return: No tiene """
    if len(diccionario_completo) != 0:
        for dato in diccionario_completo:
            print(f'\n{dato} -> ', end = "")
            for key in diccionario_completo[dato]:
                print(f"{key['cantidad']}")
                for i in range(len(key['nombres'])):
                    print(f"{key['nombres'][i]} --- ", end = "")
                    print(f"{key['poder_y_ataque'][i]}")
#Generales
def mostrar_menu(recorro_menus: list):
    """ Brief: Muestra cada opcion del menu y ademas valida lo que se ingreso.
    El codigo solo se ejecuta si la lista pasada por parametro tiene al menos un elemento """
    """ Parameters: recorro_menus """
    """ Return: Retorna la opcion seleccionada y casteada """
    if len(recorro_menus) != 0:
        for opcion in recorro_menus:
            print(opcion)
        respuesta = input("Ingrese una opcion ")
        while (respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4' 
            and respuesta != '5' and respuesta != '6' and respuesta != '7' and respuesta != '8' and respuesta != '9' and respuesta != '10'):
            respuesta = input("Error. Ingrese una opcion valida: ")
        return int(respuesta)
def mostrar_caracteristica_usuario(lista: list, caracteristca: str, separador: str):
    """ Brief: Muestra las caracteristicas indicadas para que el usuario sepa que opciones tiene. En caso de que haya que mostrar las razas o las habilidades,
    se usa un 'extend' para agregar a la variable 'lista_mostrar_carcteristica' las caracteristicas que estan dentro de otra lista. En cambio, en caso de que
    se tenga que mostrar los nombres, se utiliza un append. Se usa un separador. El codigo solo se ejecuta si la lista pasada por parametro 
    tiene al menos un elemento"""
    """ Parameters: lista, caracteristica, separador """
    """ Return: No tiene """
    if len(lista) != 0:
        lista_mostrar_carcteristica = []
        for personaje in lista:
            if type(personaje[caracteristca]) == list:
                lista_mostrar_carcteristica.extend(personaje[caracteristca]) #para razas y habilidades
            else:
                lista_mostrar_carcteristica.append(personaje[caracteristca]) #para nombres
        s = set(lista_mostrar_carcteristica)
        nueva_lista_separada = separador.join(s)
        print('Datos para seleccionar:')
        print(nueva_lista_separada)
def validar_ingreso_caracteristica(lista: list, key: str):
    """ Brief: Valida que la caracteristica que se ingresa exista. Se usa un while que se va a ejecutar siempre y cuando el usuario ingrese algo inexistente.
    El for que esta dentro del while, recorre cada personaje preguntando si existe esa caracteristica en determinada key. El codigo solo se ejecuta 
    si la lista pasada por parametro tiene al menos un elemento"""
    """ Parameters: lista, key """
    """ Return: Retorna caracteristica ingresada y validada """
    if len(lista) != 0:
        flag_existe = False
        flag_primer_ingreso = False
        while flag_primer_ingreso == False or flag_existe == False:
            if flag_primer_ingreso == False:
                caracteristica_ingresada = input("Seleccione el dato: ").lower()
                flag_primer_ingreso = True
            else:
                caracteristica_ingresada = input("Error, seleccione un dato valido: ").lower()
            for personaje in lista:
                if caracteristica_ingresada in personaje[key]:
                    flag_existe = True
        return caracteristica_ingresada
def normalizar_caracteres(lista: list, key: str):
    """ Brief: normaliza los datos, es decir, se convierten los caracteres especiales, a normales. La funcion 'unidecode' realiza una operacion
    matematica para poder convertir x valor con tilde o con algun caracter especial, a su equivalente sin tilde o sin ese caracter especial. El codigo solo se 
    ejecuta, si la lista pasada como parametro tiene al menos un elemento"""
    """ Parameters: lista, key """
    """ Return: No tiene retorno """
    if len(lista) != 0:
        for personaje in lista:
            for i in range(len(personaje[key])): #no hace falta que pregunte si hay uno solo porque minimo va a haber uno y como minimo el for va a iterar una vez
                nuevo_dato = unidecode(personaje[key][i])
                personaje[key][i] = nuevo_dato