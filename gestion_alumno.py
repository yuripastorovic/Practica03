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
            done = True

def dame_uno(conn):
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        print('Buscar Alumno')
        salida = False
        respuesta = None
        candidato = None
        print('Desea buscar por:\n1. Nombre\n2. Apellido\n3. Nombre y Apellido.')
        respuesta = utiles_validaciones.entrada_teclado()
        if respuesta == '1':
            print('Introduzca el nombre del alumno a buscar.')
            candidato= utiles_validaciones.check_campo('nombre', 25)
            alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'nombre', candidato)  # Cogemos el alumno que corresponde con el nombre
            if len(alumno) == 0:
                print('No se encontro ningun alumno con el nombre '+candidato)
                return None, None
            elif len(alumno) == 1:
                return alumno[0], respuesta
            else:
                print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                contador = 0
                for alum in alumno:
                    contador += 1
                    print(str(contador)+'. '+alum[1]+" "+alum[2])
                eliminado = utiles_validaciones.check_index(len(alumno))
                if eliminado is not None:
                    esgresado = alumno[(eliminado)]
                    return esgresado, respuesta
                else:
                    print('Saliendo')
                    return None, None
        elif respuesta == '2':
            print('Introduzca el apellido del alumno a buscar.')
            candidato = utiles_validaciones.check_campo('apellido', 25)
            alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'apellido', candidato)  # Cogemos el alumno que corresponde con el apellido
            if len(alumno) == 0:
                print('No se encontro ningun alumno con el apellido ' + candidato)
                return None, None
            elif len(alumno) == 1:
                return alumno[0], respuesta
            else:
                print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                contador = 0
                for alum in alumno:
                    contador += 1
                    print(str(contador) + '. ' + alum[1] + " " + alum[2])
                eliminado = utiles_validaciones.check_index(len(alumno))
                if eliminado is not None:
                    esgresado = alumno[(eliminado)]
                    return esgresado, respuesta
                else:
                    print('Saliendo')
                    return None, None
        elif respuesta == '3':
            print('Introduzca el nombre completo del alumno a buscar.\nPrimero introduzca el nombre:')
            name = utiles_validaciones.check_campo('nombre completo, nombre', 25)
            print('Introduzca el nombre completo del alumno a buscar.\nAhora introduzca el apellido:')
            apellido = utiles_validaciones.check_campo('nombre completo, apellido', 25)
            candidato=name+'&&'+apellido
            alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'doble', candidato)  # Cogemos el alumno que corresponde con el nombre+apellido
            if len(alumno) == 0:
                elementos = candidato.split('&&')
                nom = elementos[0]
                ape = elementos[1]
                print('No se encontro ningun alumno con el nombre completo: ' + nom+' '+ape)
                return None, None
            elif len(alumno) == 1:
                return alumno[0], respuesta
            else:
                print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                contador = 0
                for alum in alumno:
                    contador += 1
                    print(str(contador) + '. ' + alum[1] + " " + alum[2])
                eliminado = utiles_validaciones.check_index(len(alumno))
                if eliminado is not None:
                    esgresado = alumno[(eliminado)]
                    return esgresado, respuesta
                else:
                    print('Saliendo')
                    return None, None
    else:
        print("No hay alumnos que mostar\nSaliendo")
        return None, None

def baja20(conn):
    print('Baja Alumno')
    finale = False
    while not finale:
        alumno, respuesta = dame_uno(conn)
        if alumno is not None and respuesta is not None:
            if utiles_validaciones.confirmacion(
                    "Seguro que desea dar de baja a " +  alumno[1] + " " + alumno[2] + " del sistema?"):
                gestion_BBDD.delete(conn, "alumnos", alumno[0])  # Mandamos el delete
                print("Baja realizada con existo")
                finale = True
            else:
                print("Alumno no encontrado")
                fallos = utiles_validaciones.fails(fallos)
            if fallos == 5:
                print('Se ha superado el numero maximo de inetntos, volviendo al menu anterior')
                finale = True


def busqueda20(conn):
    fallos = 0
    finale = False
    while not finale:
        alumno, basura  = dame_uno(conn)
        if alumno is not None:
            print(alumno)
            finale = True
        else:
            fallos = utiles_validaciones.fails(fallos)
        if fallos==5:
            print("Alumno no encontrado")
            print('Se ha superado el numero maximo de inetntos, volviendo al menu anterior')
            finale = True


def modificar(conn):
    fallos = 0
    finale = False
    while not finale:
        alumno, basura = dame_uno(conn)
        if alumno is not None:
            print("Estos son los datos del alumno")
            print(alumno)
            print("Que desea modificar:\n1. Nombre\n2. Apellido\n3. Telefono\n4. Direccion\n5.Fecha de nacimiento\n6. Modificar todos los datos\n0. Para salir")
            modif = utiles_validaciones.check_index(5)
            if modif is None:
                print("Modificacion abortada")
                finale = True
            elif modif == "0":
                finale = True
                print("Modificacion abortada")
            elif modif== "1":
                fallitos = 0
                confirmado = False
                while not confirmado:
                    print("Modificacion Nombre\nIntroduzca el nuevo Nombre:")
                    name = utiles_validaciones.check_campo("nombre", 25)
                    if name is not None and utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                        if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                            nuevo = {"nombre": name, "apellido": alumno[2], "telefono": alumno[3], "direccion": alumno[4], "fech_nacimiento": alumno[5]}
                            gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                            confirmado = True
                        else:
                            print("Modificacion abortada")
                            confirmado = True
                    else:
                        fallitos = utiles_validaciones.fails(fallitos)
                    if fallitos == 5:
                        print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                        confirmado = True

            elif modif== "2":
                fallitos = 0
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
                    else:
                        fallitos = utiles_validaciones.fails(fallitos)
                    if fallitos == 5:
                        print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                        confirmado = True

            elif modif== "3":
                fallitos = 0
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
                    else:
                        fallitos = utiles_validaciones.fails(fallitos)
                    if fallitos == 5:
                        print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                        confirmado = True

            elif modif== "4":
                fallitos = 0
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
                    else:
                        fallitos = utiles_validaciones.fails(fallitos)
                    if fallitos == 5:
                        print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                        confirmado = True

            elif modif== "5":
                fallitos = 0
                confirmado = False
                while not confirmado:
                    print("Modificacion Fecha de Nacimiento\nIntroduzca la nueva Fecha de Nacimiento:")
                    fech = utiles_validaciones.check_campo("direccion", 50)
                    if fech is not None:
                        if utiles_validaciones.confirmacion(
                                "Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                            nuevo = {"nombre": alumno[1], "apellido": alumno[2], "telefono": alumno[3], "direccion": alumno[4], "fech_nacimiento": fech}
                            gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                            confirmado = True
                        else:
                            print("Modificacion abortada")
                            confirmado = True
                    else:
                        fallitos = utiles_validaciones.fails(fallitos)
                    if fallitos == 5:
                        print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                        confirmado = True
            elif modif == "6":
                print("Modificacion Completa\nIntroduzca el nuevo Nombre:")
                fallos = 0
                progreso = False
                while not progreso:
                    name = utiles_validaciones.check_campo("nombre", 25)
                    if name is not None and utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                        progreso = True
                    if not  utiles_validaciones.unique_nombre_completo(conn, name, alumno[2]):
                        print("Nombre ya en uso")
                        fallos = utiles_validaciones.fails(fallos)
                    if name is None:
                        fallos = utiles_validaciones.fails(fallos)
                    if fallos == 5:
                        print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                        confirmado = True
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
                            fallos = utiles_validaciones.fails(fallos)
                        if fallos == 5:
                            print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                            confirmado = True
                if fallos < 5:
                    fallos=0
                    progreso = False
                    while not progreso:
                        telef = utiles_validaciones.check_telefono()
                        if telef is None:
                            fallos = utiles_validaciones.fails(fallos)
                        if fallos == 5:
                            print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                            confirmado = True
                if fallos < 5:
                    fallos=0
                    progreso = False
                    while not progreso:
                        dir = utiles_validaciones.check_campo("direccion", 50)
                        if dir is None:
                            fallos = utiles_validaciones.fails(fallos)
                        if fallos == 5:
                            print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                            confirmado = True
                if fallos < 5:
                    fallos=0
                    progreso = False
                    while not progreso:
                        fech = utiles_validaciones.check_fecha()
                        if fech is None:
                            fallos = utiles_validaciones.fails(fallos)
                        if fallos == 5:
                            print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                            confirmado = True
                if fallos < 5:
                    if utiles_validaciones.confirmacion("Seguro que desea modificar al alumno " + alumno[1] + " " + alumno[2] + "?"):
                        nuevo = {"nombre": name, "apellido": ape, "telefono": telef, "direccion": dir, "fech_nacimiento": fech}
                        gestion_BBDD.update(conn, "alumnos", nuevo, alumno[0])
                        confirmado = True
                    else:
                        print("Modificacion abortada")
                        confirmado = True
                finale= True
        else:
            fallos = utiles_validaciones.fails(fallos)
        if fallos==5:
            print("Alumno no encontrado")
            print('Se ha superado el numero maximo de inetntos, volviendo al menu anterior')
            finale = True


def mostrar_todos(conn):
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun alumno
        print("Mostrar todos los alumnos:")
        alumnos = selec_all_from_tabla(conn, "alumnos")
        for row in alumnos:  #Recorremos las row de profesores mostrando los profesores
            print("ID: ", row[0])
            print("Nombre: ", row[1])
            print("Apellido: ", row[2])
            print("Telefono: ", row[3])
            print("Direccion: ", row[4])
            print("Fecha de nacimineto: ", row[5],"\n")
    else:
        print("No existen alumnos que mostrar")




"""
Busqueda legado
"""
def busqueda(conn): #se puede optimizar
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun profesor
        print('Buscar Alumno')
        salida = False
        while not salida:
            fallos=0
            respuesta = None
            candidato = None
            print('Desea buscar por:\n1. Nombre\n2. Apellido\n3. Nombre y Apellido.')
            respuesta = utiles_validaciones.entrada_teclado()
            if respuesta == '1':
                print('Introduzca el nombre del alumno a bucar.')
                candidato= utiles_validaciones.check_campo('nombre', 25)
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'nombre', candidato)  # Cogemos el alumno que corresponde con el nombre
                if len(alumno) == 0:
                    print('No se encontro ningun alumno con el nombre '+candidato)
                    salida = True
                elif len(alumno) == 1:
                    print(alumno[0])
                    salida = True
                else:
                    print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                    contador = 0
                    for alum in alumno:
                        contador += 1
                        print(str(contador)+'. '+alum[1]+" "+alum[2])
                    eliminado = utiles_validaciones.check_index(len(alumno))
                    if eliminado is not None:
                        esgresado = alumno[(eliminado)]
                        print(esgresado)
                        salida = True
                    else:
                        print('Saliendo')
                        salida = True
            elif respuesta == '2':
                print('Introduzca el apellido del alumno a bucar.')
                candidato = utiles_validaciones.check_campo('apellido', 25)
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'apellido', candidato)  # Cogemos el alumno que corresponde con el apellido
                if len(alumno) == 0:
                    print('No se encontro ningun alumno con el apellido ' + candidato)
                    salida = True
                elif len(alumno) == 1:
                    print(alumno[0])
                    salida = True
                else:
                    print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                    contador = 0
                    for alum in alumno:
                        contador += 1
                        print(str(contador) + '. ' + alum[1] + " " + alum[2])
                    eliminado = utiles_validaciones.check_index(len(alumno))
                    if eliminado is not None:
                        esgresado = alumno[(eliminado)]
                        print(esgresado)
                        salida = True
                    else:
                        print('Saliendo')
                        salida = True

            elif respuesta == '3':
                print('Introduzca el nombre completo del alumno a dar de baja.\nPrimero introduzca el nombre:')
                name = utiles_validaciones.check_campo('nombre completo, nombre', 25)
                print('Introduzca el nombre completo del alumno a dar de baja.\nAhora introduzca el apellido:')
                apellido = utiles_validaciones.check_campo('nombre completo, apellido', 25)
                candidato=name+'&&'+apellido
                alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'doble', candidato)  # Cogemos el alumno que corresponde con el nombre+apellido
                if len(alumno) == 0:
                    elementos = candidato.split('&&')
                    nom = elementos[0]
                    ape = elementos[1]
                    print('No se encontro ningun alumno con el nombre completo: ' + nom+' '+ape)
                    salida = True
                elif len(alumno) == 1:
                    print(alumno[0])
                    salida = True
                else:
                    print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                    contador = 0
                    for alum in alumno:
                        contador += 1
                        print(str(contador) + '. ' + alum[1] + " " + alum[2])
                    eliminado = utiles_validaciones.check_index(len(alumno))
                    if eliminado is not None:
                        esgresado = alumno[(eliminado)]
                        print(esgresado)
                        salida = True
                    else:
                        print('Saliendo')
                        salida = True
            else:
                print('Introduzca un valor valido')
                fallos = utiles_validaciones.fails(fallos)
            if fallos == 6:
                print("Se han producido 5 fallos, volviendo al menu anterior")
                salida = True


"""
Baja legado
"""

def baja(conn):
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun profesor
        print('Baja Alumno')
        salida = False
        while not salida:
            fallos=0
            pregunta = False
            respuesta = None
            candidato = None
            while not pregunta:
                print('Desea buscar por:\n1. Nombre\n2. Apellido\n3. Nombre y Apellido.')
                respuesta = utiles_validaciones.entrada_teclado()
                if respuesta == '1':
                    print('Introduzca el nombre del alumno a dar de baja.')
                    candidato= utiles_validaciones.check_campo('nombre', 25)
                    pregunta = True
                elif respuesta == '2':
                    print('Introduzca el apellido del alumno a dar de baja.')
                    candidato = utiles_validaciones.check_campo('apellido', 25)
                    pregunta = True
                elif respuesta == '3':
                    print('Introduzca el nombre completo del alumno a dar de baja.\nPrimero introduzca el nombre:')
                    name = utiles_validaciones.check_campo('nombre completo', 25)
                    print('Introduzca el nombre completo del alumno a dar de baja.\nAhora introduzca el apellido:')
                    apellido = utiles_validaciones.check_campo('nombre completo', 25)
                    candidato=name+'&&'+apellido
                    pregunta = True
                else:
                    print('Introduzca un valor valido')
                    fallos = utiles_validaciones.fails(fallos)
                if fallos == 6:
                    print("Se han producido 5 fallos, volviendo al menu anterior")
                    pregunta = True
                    salida = True
            if respuesta is not None:
                #Caso buscar por NOMBRE
                if respuesta == '1':
                    alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'nombre', candidato)  # Cogemos el alumno que corresponde con el nombre
                    if len(alumno) == 0:
                        print('No se encontro ningun alumno con el nombre '+candidato)
                        salida = True
                    elif len(alumno) == 1:
                        if utiles_validaciones.confirmacion("Seguro que desea dar de baja a " + alumno[0][1]+" "+ alumno[0][2]+ " del sistema?"):  # pedimos confirmacion
                            gestion_BBDD.delete(conn, "alumnos", alumno[0][0])  # Mandamos el delete
                            print("Baja realizada con existo")
                            salida = True
                        else:
                            print('Baja cancelada')
                            salida = True
                    else:
                        print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                        contador = 0
                        for alum in alumno:
                            contador += 1
                            print(str(contador)+'. '+alum[1]+" "+alum[2])
                        eliminado = utiles_validaciones.check_index(len(alumno))
                        if eliminado is not None:
                            esgresado = alumno[(eliminado)]
                            print(esgresado, type(esgresado))
                            if utiles_validaciones.confirmacion("Seguro que desea dar de baja a " + esgresado[1] + " " + esgresado[2] + " del sistema?"):
                                gestion_BBDD.delete(conn, "alumnos", esgresado[0])  # Mandamos el delete
                                print("Baja realizada con existo")
                                salida = True
                            else:
                                print('Baja cancelada')
                                salida = True
                        else:
                            print('Saliendo')
                            salida = True

                #Caso Buscar por APELLIDO
                elif respuesta =='2':
                    alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'apellido', candidato)  # Cogemos el alumno que corresponde con el apellido
                    if len(alumno) == 0:
                        print('No se encontro ningun alumno con el apellido '+candidato)
                        salida = True
                    elif len(alumno) == 1:
                        if utiles_validaciones.confirmacion("Seguro que desea dar de baja a " + alumno[0][1]+" "+ alumno[0][2]+ " del sistema?"):  # pedimos confirmacion
                            gestion_BBDD.delete(conn, "alumnos", alumno[0][0])  # Mandamos el delete
                            print("Baja realizada con existo")
                            salida = True
                        else:
                            print('Baja cancelada')
                            salida = True
                    else:
                        print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                        contador = 0
                        for alum in alumno:
                            contador += 1
                            print(str(contador)+'. '+alum[1]+" "+alum[2])
                        eliminado = utiles_validaciones.check_index(len(alumno))
                        if eliminado is not None:
                            esgresado = alumno[(eliminado)]
                            print(esgresado, type(esgresado))
                            if utiles_validaciones.confirmacion("Seguro que desea dar de baja a " + esgresado[1] + " " + esgresado[2] + " del sistema?"):
                                gestion_BBDD.delete(conn, "alumnos", esgresado[0])  # Mandamos el delete
                                print("Baja realizada con existo")
                                salida = True
                            else:
                                print('Baja cancelada')
                                salida = True
                        else:
                            print('Saliendo')
                            salida = True

                # Caso Buscar por NOMBRE+APELLIDO
                else:
                    alumno = gestion_BBDD.busqueda(conn, 'alumnos', 'doble', candidato)  # Cogemos el alumno que corresponde con el nombre + apellido
                    elementos = candidato.split('&&')
                    nom = elementos[0]
                    ape = elementos[1]
                    if len(alumno) == 0:
                        print('No se encontro ningun alumno con el combre completo ' + nom+' '+ape)
                        salida = True
                    elif len(alumno) == 1:
                        if utiles_validaciones.confirmacion(
                                "Seguro que desea eliminar a " + alumno[0][1] + " " + alumno[0][2] + " del sistema?"):  # pedimos confirmacion
                            gestion_BBDD.delete(conn, "alumnos", alumno[0][0])  # Mandamos el delete
                            print("Baja realizada con existo")
                            salida = True
                        else:
                            print('Baja cancelada')
                            salida = True
                    else:
                        print('Varios resultados.\nSeleccione el alumno que desea buscar:')
                        contador = 0
                        for alum in alumno:
                            contador += 1
                            print(str(contador) + '. ' + alum[1] + " " + alum[2])
                        eliminado = utiles_validaciones.check_index(len(alumno))
                        if eliminado is not None:
                            esgresado = alumno[(eliminado)]
                            print(esgresado, type(esgresado))
                            if utiles_validaciones.confirmacion("Seguro que desea dar de baja a " + esgresado[1] + " " + esgresado[2] + " del sistema?"):
                                gestion_BBDD.delete(conn, "alumnos", esgresado[0])  # Mandamos el delete
                                print("Baja realizada con existo")
                                salida = True
                            else:
                                print('Baja cancelada')
                                salida = True
                        else:
                            print('Saliendo')
                            salida = True
            else:
                print("Estoy aqui")
                salida = True
    else:
        print('Nada que mostrar, no existen alumnos aun')