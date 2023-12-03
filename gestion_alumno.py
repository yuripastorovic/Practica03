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


def dame_uno(conn):
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun profesor
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


def busqueda20(conn):
    fallos = 0
    final = false
    while not final:
        alumno = dame_uno(conn)
        if alumno is not None:
            print(alumno)
            final = True
        else:
            fallos = utiles_validaciones.fails(fallos)
        if fallos==5:
            print('Se ha superado el numero maximo de inetntos, volviendo al menu anterior')
            final = True


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


def modificar(conn):
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe algun profesor
        print('modificar Alumno')
        salida = False
        while not salida:
            fallos=0
            respuesta = None
            candidato = None
            objetivo = None
            pregunta= False
            while not pregunta:
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