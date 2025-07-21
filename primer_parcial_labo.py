import random
from funciones_parcial import *
from os import system
system('cls')

menu = ['1.Traer datos desde archivo','2.Listar cantidad por raza','3.Listar personajes por raza',
        '4.Listar personajes por habilidad y mostrar datos','5.Jugar batalla','6.Guardar Json','7.Leer Json',
        '8.Incrementar poderes','9.Mostrar caracteristicas con datos','10.Salir']

flag_traer_lista = False
flag_jason = False

while True:
    respuesta = mostrar_menu(menu)

    match respuesta:
        case 1:
            lista_personajes = parser_csv('DBZ.csv')
            normalizar_caracteres(lista_personajes, 'raza')
            normalizar_caracteres(lista_personajes, 'habilidades')
            flag_traer_lista = True
            print("Datos extraidos")
        case 2:
            if flag_traer_lista == True:
                resultado = contar_caracteristica(lista_personajes, 'raza')
                mostrar_lista(resultado)
            else:
                print("Primero tiene que traer los datos desde el archivo")
        case 3:
            if flag_traer_lista == True:
                resultado = listar_personajes_por_caracateristica(lista_personajes, 'raza', 'nombre', 'poder_ataque')
                mostrar_lista_separada(resultado)
            else:
                print("Primero tiene que traer los datos desde el archivo")
        case 4:
            if flag_traer_lista == True:
                mostrar_caracteristica_usuario(lista_personajes, 'habilidades', ' | ')
                caracteristica_validada = validar_ingreso_caracteristica(lista_personajes, 'habilidades')
                mostrar_personajes_por_caracteristica_con_datos(lista_personajes, caracteristica_validada, 'habilidades', ' | ')
            else:
                print("Primero tiene que traer los datos desde el archivo")
        case 5:
            if flag_traer_lista == True:
                mostrar_caracteristica_usuario(lista_personajes, 'nombre', ' | ')
                nombre_personaje_seleccionado_validado = validar_ingreso_caracteristica(lista_personajes, 'nombre')
                poder_de_ataque_seleccionado = buscar_poder(lista_personajes, nombre_personaje_seleccionado_validado, 'poder_ataque')
                id_personaje_aleatorio = random.randint(1, len(lista_personajes))
                nombre_personaje_aleatorio = buscar_igualdad_nombre(lista_personajes, id_personaje_aleatorio)
                poder_de_ataque_aleatorio = buscar_poder(lista_personajes, id_personaje_aleatorio, 'poder_ataque')
                guardar_pelea(poder_de_ataque_seleccionado, poder_de_ataque_aleatorio, nombre_personaje_seleccionado_validado,
                            nombre_personaje_aleatorio)
                print('La pelea a sido guardada')
            else:
                print("Primero tiene que traer los datos desde el archivo")
        case 6:
            if flag_traer_lista == True:
                mostrar_caracteristica_usuario(lista_personajes, 'raza', ' | ')
                raza_validada = validar_ingreso_caracteristica(lista_personajes, 'raza')
                mostrar_caracteristica_usuario(lista_personajes, 'habilidades', ' | ')
                habilidad_validada = validar_ingreso_caracteristica(lista_personajes, 'habilidades')
                diccionario_personajes_especificos = crear_json(lista_personajes, raza_validada, habilidad_validada)
                if diccionario_personajes_especificos != None:
                    flag_jason = True
                else:
                    print("No hay personajes que coincidan con esa raza y con esa habilidad. No se guardo ningun archivo")
            else:
                print("Primero tiene que traer los datos desde el archivo")
        case 7:
            if flag_traer_lista == True and flag_jason == True:
                leer_json(diccionario_personajes_especificos, ' + ')
            else:
                print("Primero tiene que traer los datos desde el archivo y ademas tiene que haber guardado el Json")
        case 8:
            if flag_traer_lista == True:
                nueva_lista_nombres_modificados = incrementar_poderes(lista_personajes, 'raza', 'saiyan')
                hacer_csv_modificados(nueva_lista_nombres_modificados, ' | ')
                print('Poderes incrementados')
            else:
                print("Primero tiene que traer los datos desde el archivo")
        case 9:
            if flag_traer_lista == True:
                diccionario = crear_diccionario_caracteristica_personajes(lista_personajes, 'raza')
                mostrar_diccionario_completo(diccionario)
            else:
                print("Primero tiene que traer los datos desde el archivo")
        case 10:
            break