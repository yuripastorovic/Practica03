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

        nombre = None
        apellido = None
        telefono = None
        direccion = None
        fech_nacimiento = None
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

                print("Alta realizada con existo")

        if not utiles_validaciones.confirmacion(
                "Quieres tratar de dar de alta otro alumno?"):  # Preguntamos si quiere dar otro alumno de alta
            salida = True


def busqueda_unica(conn):
    """
    Funcion de apoyo que devuelve un alumno inequivocamente
    :param conn: conexion con BBDD
    :return: alumno: El alumno que se buscaba
    :return: None: Si no encuentra un alumno en 5 intentos
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        salida = False
        respuesta = None
        candidato = None
        print('Desea buscar por:\n1. Nombre\n2. Apellido\n3. Nombre y Apellido.')
        respuesta = utiles_validaciones.entrada_teclado()
        if respuesta == '1':
            print('Introduzca el nombre del alumno a buscar.')
            candidato= utiles_validaciones.check_campo('nombre', 25)
            if candidato is not None:
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'nombre', candidato)  # Cogemos el alumno que corresponde con el nombre
                if len(alumno) == 0:
                    print('No se encontro ningun alumno con el nombre '+candidato)
                    return None
                elif len(alumno) == 1:
                    return alumno[0]
                else:
                    print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                    contador = 0
                    for alum in alumno:
                        contador += 1
                        print(str(contador)+'. '+alum[1]+" "+alum[2])
                    eliminado = utiles_validaciones.check_index(len(alumno))
                    if eliminado is not None:
                        esgresado = alumno[(eliminado)]
                        return esgresado
                    else:
                        print('Saliendo')
                        return None
        elif respuesta == '2':
            print('Introduzca el apellido del alumno a buscar.')
            candidato = utiles_validaciones.check_campo('apellido', 25)
            if candidato is not None:
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'apellido', candidato)  # Cogemos el alumno que corresponde con el apellido
                if len(alumno) == 0:
                    print('No se encontro ningun alumno con el apellido ' + candidato)
                    return None
                elif len(alumno) == 1:
                    return alumno[0]
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
        else:
            print("Recuerde solo numeros")
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
        finale = False
        salida = False
        while not salida:
            while not finale:
                alumno = busqueda_unica(conn)
                if alumno is not None:
                    if utiles_validaciones.confirmacion("Seguro que desea dar de baja a " + alumno[1] + " " + alumno[2] + " del sistema?"):
                        gestion_BBDD.delete(conn, "alumnos", alumno[0])  # Mandamos el delete
                        print("Baja realizada con existo")
                        finale = True
                    else:
                        print("Baja abortada.")
                        finale = True
                if not utiles_validaciones.confirmacion("Desea dar de baja otro alumno?"):
                    print("Voviendo al menu anterior")
                    salida = True
    else:
        print("No hay alumnos que mostar\nSaliendo")


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
                    print("ID: ", alumno[0])
                    print("Nombre: ", alumno[1])
                    print("Apellido: ", alumno[2])
                    print("Telefono: ", alumno[3])
                    print("Direccion: ", alumno[4])
                    print("Fecha de nacimineto: ", alumno[5], "\n")
                    finale = True
            if not utiles_validaciones.confirmacion("Desea buscar otro alumno?"):
                print("Voviendo al menu anterior")
                salida = True
    else:
        print("No hay alumnos que mostar\nSaliendo")


def modificar(conn):
    """
    Funcion que permite modificar un alumno
    :param conn: Conexion con BBDD
    :return: None
    """
    fallos = 0
    finale = False
    while not finale:
        alumno = busqueda_unica(conn)
        if alumno is not None:
            print("Estos son los datos del alumno")
            print(alumno)
            print("Que desea modificar:\n1. Nombre\n2. Apellido\n3. Telefono\n4. Direccion\n5. Fecha de nacimiento\n6. Modificar todos los datos\n0. Para salir")
            modif = ""
            cont = 0
            done = False
            while not done:
                modif = input()
                if modif == "0" or modif == "1" or modif == "2" or modif == "3" or modif == "4" or modif == "5" or modif == "6":
                    done = True
                else:
                    cont += 1
                    print("Seleccione un numero del 0 al 6")
                if cont == 5:
                    done = True
                    modif = "0"
            if modif == "0":
                print("Modificacion abortada")
                finale = True
            elif modif == "1":
                confirmado = False
                while not confirmado:
                    print("Modificacion Nombre\nIntroduzca el nuevo Nombre:")
                    name = utiles_validaciones.check_campo("nombre", 25) 
                    print(alumno)                   
                    if name is not None:
                        if utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                            if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                                nuevo = {"nombre": name, "apellido": alumno[2], "telefono": alumno[3], "direccion": alumno[4], "fech_nacimiento": alumno[5]}
                                gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                                confirmado = True
                            else:
                                print("Modificacion abortada")
                                confirmado = True
            elif modif== "2":
                confirmado = False
                while not confirmado:
                    print("Modificacion Apellido\nIntroduzca el nuevo Apellido:")
                    name2 = utiles_validaciones.check_campo("apellido", 25)
                    if name2 is not None and utiles_validaciones.unique_nombre_completo(conn, alumno[1], name2):
                        if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                            nuevo = {"nombre": alumno[1], "apellido": name2, "telefono": alumno[3], "direccion": alumno[4], "fech_nacimiento": alumno[5]}
                            gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                            confirmado = True
                        else:
                            print("Modificacion abortada")
                            confirmado = True
            elif modif== "3":
                confirmado = False
                while not confirmado:
                    print("Modificacion Telefono\nIntroduzca el nuevo Telefono:")
                    telef = utiles_validaciones.check_telefono()
                    if telef is not None:
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
                    dir = utiles_validaciones.check_campo("direccion", 50)
                    if dir is not None:
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
                    fech = utiles_validaciones.check_fecha()
                    if fech is not None:
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
                    name = utiles_validaciones.check_campo("nombre", 25)
                    if name is not None and utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                        progreso = True
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
                        ape = utiles_validaciones.check_campo("apellido", 25)
                        if ape is not None and utiles_validaciones.unique_nombre_completo(conn, name, ape):
                            progreso = True
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
            if not utiles_validaciones.confirmacion("Desea modificar otro alumno?"):
                finale = True
        else:
            fallos = utiles_validaciones.fails(fallos)
        if fallos==5:
            print("Alumno no encontrado")
            print('Se ha superado el numero maximo de inetntos, volviendo al menu anterior')
            finale = True


def mostrar_todos(conn):
    """
    Permite mostrar todos los alumnos de la BBDD
    :param conn: Conexion con BBDD
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        print("Mostrar todos los alumnos:")
        alumnos = gestion_BBDD.selec_all_from_tabla(conn, "alumnos")
        for row in alumnos:  #Recorremos las row de profesores mostrando los profesores
            print("ID: ", row[0])
            print("Nombre: ", row[1])
            print("Apellido: ", row[2])
            print("Telefono: ", row[3])
            print("Direccion: ", row[4])
            print("Fecha de nacimineto: ", row[5], "\n")
    else:
        print("No existen alumnos que mostrar")
