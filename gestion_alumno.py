"""
Este fichero Python se encarga de la gestion de alumnos
"""
import utiles_validaciones
import gestion_BBDD


def alta(conn):
    """
    Funcion que gestiona el alta de un alumno
    :param conn: Cursor de la BBDD
    :return: None
    """
    print('Alta Alumno')
    salida = False
    while not salida:

        apellido = None
        telefono = None
        direccion = None
        fech_nacimiento = None
        #Siempre vamos a funcionar a modo escalera, es decir si se verifica que el campo es vorrecto pasamos al siguiente nivel, en caso contrario, descendemos al inicio
        nombre = utiles_validaciones.check_campo('nombre', 25)
        if nombre is not None:
            apellido = utiles_validaciones.check_campo('apellido', 25)
        if apellido is not None:
            if utiles_validaciones.unique_nombre_completo(conn, nombre, apellido):
                telefono = utiles_validaciones.check_telefono()
            if telefono is not None:
                direccion = utiles_validaciones.check_campo('direccion', 50)
            if direccion is not None:
                fech_nacimiento = utiles_validaciones.check_fecha()
            if fech_nacimiento is not None:
                datos = {'nombre': nombre, 'apellido': apellido, 'telefono': telefono, 'direccion': direccion,
                         'fech_nacimiento': fech_nacimiento}  # Creaccion de un diccionario con los datos del alumno

                gestion_BBDD.insert(conn, "alumnos", datos)  # Realizamos el insert en la tabla alumnos

                print("Alta realizada con existo"+"\n")

        if not utiles_validaciones.confirmacion("Quieres tratar de dar de alta otro alumno?"):  # Preguntamos si quiere dar otro alumno de alta
            salida = True
            print("-"*20+"\n")
        else:
            print("\n")


def busqueda_unica(conn):
    """
    Funcion de apoyo que devuelve un alumno inequivocamente
    :param conn: conexion con BBDD
    :return: alumno: El alumno que se buscaba
    :return: None: Si no encuentra un alumno en 5 intentos
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        candidato = None
        #Primero preguntamos como quiere buscar nom, ape, nom+ape
        print('Desea buscar por:\n1. Nombre\n2. Apellido\n3. Nombre y Apellido.')
        respuesta = utiles_validaciones.entrada_teclado()
        #Buscando por nombre
        if respuesta == '1':
            print('Introduzca el nombre del alumno a buscar.')
            candidato= utiles_validaciones.check_campo('nombre', 25)
            if candidato is not None:
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'nombre', candidato)  # Cogemos el alumno que corresponde con el nombre
                #No hay coincidencias
                if len(alumno) == 0:
                    print('No se encontro ningun alumno con el nombre '+candidato+"\n")
                    return None
                #Hay una coincidencia
                elif len(alumno) == 1:
                    return alumno[0]
                #Hay varias coincidencias
                else:
                    print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                    contador = 0
                    for alum in alumno:
                        contador += 1
                        print(str(contador)+'. '+alum[1]+" "+alum[2])
                    #Seleccionamos la opcion que queremos
                    eliminado = utiles_validaciones.check_index(len(alumno))
                    if eliminado is not None:
                        esgresado = alumno[(eliminado)]
                        return esgresado
                    else:
                        print('Saliendo')
                        return None
        #Buscar por apellido
        elif respuesta == '2':
            print('Introduzca el apellido del alumno a buscar.')
            candidato = utiles_validaciones.check_campo('apellido', 25)
            if candidato is not None:
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'apellido', candidato)  # Cogemos el alumno que corresponde con el apellido
                #No hay coincidencias
                if len(alumno) == 0:
                    print('No se encontro ningun alumno con el apellido ' + candidato)
                    return None
                #Resultado unico
                elif len(alumno) == 1:
                    return alumno[0]
                #Varios resultados
                else:
                    print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                    contador = 0
                    for alum in alumno:
                        contador += 1
                        print(str(contador) + '. ' + alum[1] + " " + alum[2])
                    eliminado = utiles_validaciones.check_index(len(alumno))
                    #Seleccionamos la opcion que queremos
                    if eliminado is not None:
                        esgresado = alumno[(eliminado)]
                        return esgresado
                    else:
                        print('Saliendo')
                        return None

        elif respuesta == '3':
            print('Introduzca el nombre completo del alumno a buscar.\nPrimero introduzca el nombre:')
            apellido = None
            name = utiles_validaciones.check_campo('nombre completo, nombre', 25)
            if name is not None:
                print('Introduzca el nombre completo del alumno a buscar.\nAhora introduzca el apellido:')
                apellido = utiles_validaciones.check_campo('nombre completo, apellido', 25)
            if apellido is not None:
                candidato=name+'&&'+apellido
            if candidato is not None:
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'doble', candidato)  # Cogemos el alumno que corresponde con el nombre+apellido
                if len(alumno) == 0:
                    elementos = candidato.split('&&')
                    nom = elementos[0]
                    ape = elementos[1]
                    print('No se encontro ningun alumno con el nombre completo: ' + nom+' '+ape)
                    return None
                elif len(alumno) == 1:
                    return alumno[0]
                #ESTO NUNCA PUEDE OCURRIR_________
                else:
                    print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                    contador = 0
                    for alum in alumno:
                        contador += 1
                        print(str(contador) + '. ' + alum[1] + " " + alum[2])
                    eliminado = utiles_validaciones.check_index(len(alumno))
                    if eliminado is not None:
                        esgresado = alumno[(eliminado)]
                        return esgresado
                    else:
                        print('Saliendo')
                        return None
                #___________________________________
        else:
            print("Recuerde solo numeros"+"\n")
            return None
    else:
        print("No hay alumnos que mostar\nSaliendo")
        return None


def baja(conn):
    """
    Funcion para dar de baja a un alumno
    :param conn:    Conexion con BBDD
    :return:    None:
    """
    print('Baja Alumno')
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        salida = False
        while not salida:
            alumno = busqueda_unica(conn)
            #Existe un resultado
            if alumno is not None:
                #confirmacion
                if utiles_validaciones.confirmacion("Seguro que desea dar de baja a " + alumno[1] + " " + alumno[2] + " del sistema?"):
                    gestion_BBDD.delete(conn, "alumnos", alumno[0])  # Mandamos el delete
                    print("Baja realizada con existo"+"\n")
                else:
                    print("Baja abortada."+"\n")

            #No existen resultados
            else:
                print("No se encontro al alumno que desea borrar"+"\n")
            #Continuamos en el menu
            if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:
                if not utiles_validaciones.confirmacion("Desea dar de baja otro alumno?"):
                    salida = True
                    print("Voviendo al menu anterior")
                    print("-"*20+"\n")
                else:
                    print("\n")
            #No hay mas alumnos
            else:
                salida = True
                print("No quedan alumnos que borrar")
                print("-"*20+"\n")
    #No hay alumnos
    else:
        print("No hay alumnos que mostar\nSaliendo")
        print("-"*20+"\n")


def busqueda(conn):
    """
    Funcion para buscar alumno, imprime por panatalla sus datos
    :param conn:    Conexion con BBDD
    :return:    None:
    """
    print('Buscar Alumno')
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        salida = False
        while not salida:
            finale = False
            while not finale:
                alumno = busqueda_unica(conn)
                if alumno is not None:
                    alumno = gestion_BBDD.selec_join(conn, "alumnos", alumno[0])
                    nombre_alum = ""
                    #Mostramos alumnos que no tienen cursos
                    if len(alumno[0]) == 6:
                        print("ID: ", alumno[0][0])
                        print("Nombre: ", alumno[0][1])
                        print("Apellido: ", alumno[0][2])
                        print("Telefono: ", alumno[0][3])
                        print("Direccion: ", alumno[0][4])
                        print("Fecha de nacimineto: ", alumno[0][5], "\n")
                        finale = True
                    #Mostramos alumnos que tienen curso
                    elif len(alumno[0]) == 7:
                        for i in range(0, len(alumno)):
                            if nombre_alum != alumno[i][1]:
                                nombre_alum = alumno[i][1]
                                print("ID: ", alumno[i][0])
                                print("Nombre: ", alumno[i][1])
                                print("Apellido: ", alumno[i][2])
                                print("Telefono: ", alumno[i][3])
                                print("Direccion: ", alumno[i][4])
                                print("Fecha de nacimineto: ", alumno[i][5])
                                if alumno[i][6] is not None:
                                    print("Cursos: ", alumno[i][6], end="")
                            else:
                                print(" | ", alumno[i][6], end="")
                        print()
                        finale = True
                #No hay resultados
                else:
                    print("El alumno que desea buscar no existe en el centro")
                    finale = True
            #Seguimos en el menu
            if not utiles_validaciones.confirmacion("Desea buscar otro alumno?"):
                print("Voviendo al menu anterior")
                salida = True
                print("-"*20+"\n")
            else:
                print("\n")
    #No hay alumnos
    else:
        print("No hay alumnos que mostar\nSaliendo")
        print("-"*20+"\n")


def modificar(conn):
    """
    Funcion que permite modificar un alumno
    :param conn: Conexion con BBDD
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:
        fallos = 0
        finale = False
        while not finale:
            #buscamos el alumno a modificar
            alumno = busqueda_unica(conn)
            if alumno is not None:
                #mostramos los datos actuales del alumno
                print("Estos son los datos del alumno")
                print(alumno)
                #preguntamos que desea buscar
                print("Que desea modificar:\n1. Nombre\n2. Apellido\n3. Telefono\n4. Direccion\n5. Fecha de nacimiento\n6. Modificar todos los datos\n0. Para salir")
                modif = ""
                cont = 0
                done = False
                while not done:
                    modif = input()
                    #verificamos que se ha introducido un dato correcto
                    if modif == "0" or modif == "1" or modif == "2" or modif == "3" or modif == "4" or modif == "5" or modif == "6":
                        done = True
                    else:
                        cont += 1
                        print("Seleccione un numero del 0 al 6")
                    if cont == 5:
                        done = True
                        modif = "0"
                #Opcion salir
                if modif == "0":
                    print("Modificacion abortada")
                    finale = True
                #Opcion Nombre
                elif modif == "1":
                    confirmado = False
                    while not confirmado:
                        print("Modificacion Nombre\nIntroduzca el nuevo Nombre:")
                        #Verificamos Nombre
                        name = utiles_validaciones.check_campo("nombre", 25)
                        print(alumno)
                        if name is not None:
                            #Verificamos Nombre es unico, es decir el nuevo nombre no se repite en condicion de nombre completo: nom+ape
                            if utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                                #Confirmacion
                                if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                                    nuevo = {"nombre": name, "apellido": alumno[2], "telefono": alumno[3], "direccion": alumno[4], "fech_nacimiento": alumno[5]}
                                    gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                                    confirmado = True
                                else:
                                    print("Modificacion abortada")
                                    confirmado = True
                #Apellido
                elif modif== "2":
                    confirmado = False
                    while not confirmado:
                        print("Modificacion Apellido\nIntroduzca el nuevo Apellido:")
                        # verificar campo
                        name2 = utiles_validaciones.check_campo("apellido", 25)
                        # Verificamos Apellido es unico, es decir el nuevo nombre no se repite en condicion de nombre completo: nom+ape
                        if name2 is not None and utiles_validaciones.unique_nombre_completo(conn, alumno[1], name2):
                            # Confirmacion
                            if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                                nuevo = {"nombre": alumno[1], "apellido": name2, "telefono": alumno[3], "direccion": alumno[4], "fech_nacimiento": alumno[5]}
                                gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                                confirmado = True
                            else:
                                print("Modificacion abortada")
                                confirmado = True
                #Telefono
                elif modif== "3":
                    confirmado = False
                    while not confirmado:
                        print("Modificacion Telefono\nIntroduzca el nuevo Telefono:")
                        #verificar campo
                        telef = utiles_validaciones.check_telefono()
                        if telef is not None:
                            # Confirmacion
                            if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                                nuevo = {"nombre": alumno[1], "apellido": alumno[2], "telefono": telef, "direccion": alumno[4], "fech_nacimiento": alumno[5]}
                                gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                                confirmado = True
                            else:
                                print("Modificacion abortada")
                                confirmado = True
                elif modif== "4":
                    confirmado = False
                    while not confirmado:
                        print("Modificacion Direccion\nIntroduzca la nueva Direccion:")
                        # verificar campo
                        dir = utiles_validaciones.check_campo("direccion", 50)
                        if dir is not None:
                            # Confirmacion
                            if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                                nuevo = {"nombre": alumno[1], "apellido": alumno[2], "telefono": alumno[3], "direccion": dir, "fech_nacimiento": alumno[5]}
                                gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                                confirmado = True
                            else:
                                print("Modificacion abortada")
                                confirmado = True
                elif modif== "5":
                    confirmado = False
                    while not confirmado:
                        print("Modificacion Fecha de Nacimiento\nIntroduzca la nueva Fecha de Nacimiento:")
                        # verificar campo
                        fech = utiles_validaciones.check_fecha()
                        if fech is not None:
                            # Confirmacion
                            if utiles_validaciones.confirmacion(
                                    "Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                                nuevo = {"nombre": alumno[1], "apellido": alumno[2], "telefono": alumno[3], "direccion": alumno[4], "fech_nacimiento": fech}
                                gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                                confirmado = True
                            else:
                                print("Modificacion abortada")
                                confirmado = True
                elif modif == "6":
                    print("Modificacion Completa\nIntroduzca el nuevo Nombre:")
                    fallos = 0
                    progreso = False
                    while not progreso:
                        # verificar campo
                        name = utiles_validaciones.check_campo("nombre", 25)
                        if name is not None and utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                            progreso = True
                        # Verificamos Nombre es unico, es decir el nuevo nombre no se repite en condicion de nombre completo: nom+ape
                        if not utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                            print("Nombre ya en uso")
                            fallos = utiles_validaciones.fails(fallos)
                        if name is None:
                            fallos = 5
                        if fallos == 5:
                            print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                            progreso = True
                    if fallos < 5:
                        fallos=0
                        progreso = False
                        while not progreso:
                            # verificar campo
                            ape = utiles_validaciones.check_campo("apellido", 25)
                            if ape is not None and utiles_validaciones.unique_nombre_completo(conn, name, ape):
                                progreso = True
                            # Verificamos Apellido es unico, es decir el nuevo nombre no se repite en condicion de nombre completo: nom+ape
                            if not utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                                fallos = utiles_validaciones.fails(fallos)
                            if ape is None:
                                fallos = 5
                            if fallos == 5:
                                print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                                progreso = True
                    if fallos < 5:
                        fallos=0
                        progreso = False
                        while not progreso:
                            # verificar campo
                            telef = utiles_validaciones.check_telefono()
                            if telef is not None:
                                fallos=0
                                progreso=True
                            else:
                                fallos = 5
                            if fallos == 5:
                                print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                                progreso = True
                    if fallos < 5:
                        progreso = False
                        while not progreso:
                            # verificar campo
                            dir = utiles_validaciones.check_campo("direccion", 50)
                            if dir is not None:
                                fallos = 0
                                progreso=True
                            else:
                                fallos = 5
                            if fallos == 5:
                                print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                                progreso = True
                    if fallos < 5:
                        progreso = False
                        while not progreso:
                            # verificar campo
                            fech = utiles_validaciones.check_fecha()
                            if fech is not None:
                                fallos = 0
                                progreso = True
                            if fech is None:
                                fallos=5
                                progreso=True
                            if fallos == 5:
                                print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                                progreso=True
                    if fallos < 5:
                        if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                            nuevo = {"nombre": name, "apellido": ape, "telefono": telef, "direccion": dir, "fech_nacimiento": fech}
                            gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                            print("Modificacion realizada.")
                        else:
                            print("Modificacion abortada")
                # Confirmacion
                if not utiles_validaciones.confirmacion("Desea modificar otro alumno?"):
                    finale = True
            else:
                fallos = utiles_validaciones.fails(fallos)
            if fallos==5:
                print("Alumno no encontrado")
                print('Se ha superado el numero maximo de inetntos, volviendo al menu anterior')
                finale = True
    else:
        print("No existen alumnos que modificar")
        print("-"*20+"\n")


def mostrar_todos(conn):
    """
    Permite mostrar todos los alumnos de la BBDD
    :param conn: Conexion con BBDD
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        print("Mostrar todos los alumnos:")
        alumnos = gestion_BBDD.select_all_left_join(conn, "alumnos")
        nombre_alumno = ""
        for row in alumnos:  #Recorremos las row de alumnos mostrando los alumnos
            #Alumnos sin cursos asociasdos
            if len(row) == 6:
                print("\n")
                print("ID: ", row[0])
                print("Nombre: ", row[1])
                print("Apellido: ", row[2])
                print("Telefono: ", row[3])
                print("Direccion: ", row[4])
                print("Fecha de nacimineto: ", row[5], "\n")
            #Alumnos con cursos
            elif len(row) == 7:
                if nombre_alumno != row[1]:
                    nombre_alumno = row[1]
                    print("\n")
                    print("ID: ", row[0])
                    print("Nombre: ", row[1])
                    print("Apellido: ", row[2])
                    print("Telefono: ", row[3])
                    print("Direccion: ", row[4])
                    print("Fecha de nacimineto: ", row[5])
                    if row[6] is not None:
                        print("Cursos: ", row[6], end="")
                    else:
                        print("\n\t"+"-"*15,end="")
                else:
                    print(" | ", row[6], end="")
        print("\n")
    else:
        print("No existen alumnos que mostrar")
        print("-"*20+"\n")
