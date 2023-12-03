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
        nombre = utiles_validaciones.check_campo('alta Alumno', 25)
        if nombre is not None:
            apellido = utiles_validaciones.check_campo('alta Alumno', 25)
        if apellido is not None:
            telefono = utiles_validaciones.check_telefono()
        if telefono is not None:
            direccion = utiles_validaciones.check_campo('alta Alumno', 50)
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
                print('Desea buscar por:\n1. Nombre\2. Apellido\n3. Nombre y Apellido.')
                respuesta = utiles_validaciones.entrada_teclado()
                if respuesta == '1':
                    print('Introduzca el nombre del alumno a dar de baja.')
                    candidato= utiles_validaciones.check_campo('nombre', 25)
                elif respuesta == '2':
                    print('Introduzca el apellido del alumno a dar de baja.')
                    candidato = utiles_validaciones.check_campo('apellido', 25)
                elif respuesta == '3':
                    print('Introduzca el nombre completo del alumno a dar de baja.\nPrimero introduzca el nombre:')
                    name = utiles_validaciones.check_campo('nombre completo', 25)
                    print('Introduzca el nombre completo del alumno a dar de baja.\nAhora introduzca el apellido:')
                    apellido = utiles_validaciones.check_campo('nombre completo', 25)
                    candidato=name+'&&'+apellido
                else:
                    print('Introduzca un valor valido')
                    fallos = utiles_validaciones.fails(fallos)
                if fallos == 6:
                    print("Se han producido 5 fallos, volviendo al menu anterior")
                    pregunta = True
                    salida = True
            if respuesta is not None:
                if respuesta == '1':
                    alumno = gestion_BBDD.buscar(conn, 'alumnos', 'nombre', candidato.capitalize())  # Cogemos el alumno que corresponde con el nombre
                    if len(alumno) == 0:
                        print('No se encontro ningun alumno con el nombre '+candidato)
                    elif len(alumno) == 1:
                        if utiles_validaciones.confirmacion("Seguro que desea eliminar a " + alumno[0][
                            1]+" "+ alumno[0][2]+ " del sistema?"):  # pedimos confirmacion
                            gestion_BBDD.delete(conn, "alumnos", alumno[0][0])  # Mandamos el delete
                            print("Baja realizada con existo")
                            salida = True
                        else:
                            print('Baja cancelada')
                    else:
                        print('Seleccione el alumno que desea eliminar:')
                        contador = 0
                        for alum in alumno:
                            contador+=1
                            print(str(contador)+'. '+alum[1]+alum[2])
                        eliminado=utiles_validaciones.check_index(len(alum))
                        if eliminado is not None:
                            esgresado= alumno[(eliminado-1)][0]
                            if utiles_validaciones.confirmacion("Seguro que desea eliminar a " + alumno[esgresado][
                                1] + " " + alumno[esgresado][2] + " del sistema?"):
                                gestion_BBDD.delete(conn, "alumnos", esgresado)  # Mandamos el delete
                                print("Baja realizada con existo")
                                salida = True
                            else:
                                print('Baja cancelada')
                        else:
                            print('Saliendo')
                elif respuesta =='2':
                    alumno = gestion_BBDD.buscar(conn, 'alumnos', 'apellido', candidato.capitalize())  # Cogemos el alumno que corresponde con el apellido
                else:
                    alumno = gestion_BBDD.buscar(conn, 'alumnos', 'doble', candidato)  # Cogemos el alumno que corresponde con el nombre nombre + apellido


    else:
        print('Nada que mostrar, no existen alumnos aun')
