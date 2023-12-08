"""
this is gestion_curso
"""
import gestion_BBDD
import utiles_validaciones


def alta(conn):
    """
    Funcion que da de alta un curso en la bbdd.
    :param conn:
    :return:
    """
    print("Alta curso:")
    done = False
    while not done:  #Para dar de alta varios profesores en una ejecucion de la funcion
        nombre = None
        descripcion = None
        nombre = utiles_validaciones.check_campo("nombre", 25)
        nombre = utiles_validaciones.unique_nombre_curso(conn, nombre)
        if nombre is not None:
            descripcion = utiles_validaciones.check_campo("descripcion", 50)
        if descripcion is not None:

            datos = {"nombre": nombre, "descripcion": descripcion}  #Pasamos los datos a un diccionario

            gestion_BBDD.insert(conn, "cursos", datos)  #Realizamos el insert

            print("Alta realizada con existo")

        if not utiles_validaciones.confirmacion("Quieres tratar de dar de alta otro curso?"):  #Preguntamos si quiere dar otro profesor de alta
            done = True


def busqueda_unica(conn):
    if len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:  # Asegurarnos de que existe alumno alumno
        print("Buscar Curso")
        salida = False
        print('Introduzca el nombre del curso')
        candidato = utiles_validaciones.check_campo("nombre curso", 25)
        if candidato is not None:
            cursos= gestion_BBDD.busqueda(conn, "cursos", "", candidato)
            if len(cursos) == 0:
                print('No se encontro ningun curso con el nombre ' + candidato)
                return None
            elif len(cursos) == 1:
                return cursos[0]
            else:
                print('Varios resultados.\nSeleccione el curso que desea buscar:')
                contador = 0
                for curs in cursos:
                    contador += 1
                    print(str(contador) + '. ' + curs[1] + " " + curs[2])
                opcion = utiles_validaciones.check_index(len(cursos))
                if opcion is not None:
                    objetivo =cursos[opcion]
                    return objetivo
                else:
                    print('Saliendo')
                    return None
        else:
            print("Ha superado el numero maximo de errores permitidos")
            return None
    else:
        print("No hay cursos que mostar\nSaliendo")
        return None


def busqueda(conn):
    if gestion_BBDD.selec_all_from_tabla(conn, "cursos") > 0:
        fallos = 0
        finale = False
        while not finale:
            curso = busqueda_unica(conn)
            if curso is not None:
                print(curso)
                finale = True
            else:
                fallos = utiles_validaciones.fails(fallos)
            if fallos==5:
                print("Curso no encontrado")
                print('Se ha superado el numero maximo de inetntos, volviendo al menu anterior')
                finale = True
    else:
        print("No hay cursos en el sistema.")


def baja(conn):
    if gestion_BBDD.selec_all_from_tabla(conn, "cursos"):
        print('Baja Curso')
        finale = False
        salida = False
        while not salida:
            while not finale:
                curso = busqueda_unica(conn)
                if curso is not None:
                    if utiles_validaciones.confirmacion("Seguro que desea dar de baja el curso: " +  curso[1] + " del sistema?"):
                        gestion_BBDD.delete(conn, "cursos", curso[0])  # Mandamos el delete
                        print("Baja realizada con existo")
                        finale = True
                    else:
                        print("Baja abortada.")
                        finale = True
                if not utiles_validaciones.confirmacion("Desea dar de baja otro curso?"):
                    salida = True
    else:
        print("No hay cursos en el sistema.")


def modificar(conn):
    if gestion_BBDD.selec_all_from_tabla(conn, "cursos") > 0:
        print('Modificar Curso')
        finale = False
        salida = False
        while not salida:
            while not finale:
                curso = busqueda_unica(conn)
                if curso is not None:
                    print("Estos son los datos del curso")
                    print(curso)
                    print("Que desea modificar:\n1. Nombre\n2. Descripcion\n3. Modificar todos los datos\n0. Para salir")
                    modif = utiles_validaciones.check_index(4)
                    modif += 1 # Ajuste del metodo check_index
                    if modif is None or modif == 0:
                        print("Modificacion abortada")
                        finale = True
                    elif modif == 1:
                        fallitos = 0
                        confirmado = False
                        while not confirmado:
                            print("Modificacion Nombre\nIntroduzca el nuevo Nombre:")
                            name = utiles_validaciones.check_campo("nombre", 25)
                            if name is not None:
                                if utiles_validaciones.unique_nombre_curso(conn, name):
                                    if utiles_validaciones.confirmacion("Seguro que desea modificar el curso " + curso[1] +"?"):
                                        nuevo = {"nombre": name, "descripcion": curso[2]}
                                        gestion_BBDD.update(conn, "cursos", nuevo, curso[0])
                                        confirmado = True
                                    else:
                                        print("Modificacion abortada")
                                        confirmado = True
                            else:
                                print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                                confirmado = True

                    elif modif == 2:
                        fallitos = 0
                        confirmado = False
                        while not confirmado:
                            print("Modificacion Descripcion\nIntroduzca la nueva Descripcion:")
                            des = utiles_validaciones.check_campo("descripcion", 25)
                            if des is not None:
                                if utiles_validaciones.confirmacion("Seguro que desea modificar el curso " + curso[1] +"?"):
                                    nuevo = {"nombre": curso[1], "descripcion": des}
                                    gestion_BBDD.update(conn, "cursos", nuevo, curso[0])
                                    confirmado = True
                                else:
                                    print("Modificacion abortada")
                                    confirmado = True
                            else:
                                print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                                confirmado = True
                    elif modif == 3:
                        fallitos = 0
                        confirmado = False
                        while not confirmado:
                            print("Modificacion Nombre\nIntroduzca el nuevo Nombre:")
                            name = utiles_validaciones.check_campo("nombre", 25)
                            if name is not None:
                                if utiles_validaciones.unique_nombre_curso(conn, name):
                                    print("Modificacion Descripcion\nIntroduzca la nueva Descripcion:")
                                    des = utiles_validaciones.check_campo("descripcion", 25)
                                    if des is not None:
                                        if utiles_validaciones.confirmacion(
                                                "Seguro que desea modificar el curso " + curso[1] + "?"):
                                            nuevo = {"nombre": name, "descripcion": des}
                                            gestion_BBDD.update(conn, "cursos", nuevo, curso[0])
                                            confirmado = True
                                        else:
                                            print("Modificacion abortada")
                                            confirmado = True
                                    else:
                                        print(
                                            "Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                                        confirmado = True
                else:
                    print("Modificacion abortada, se han superado el maximo de fallos\nVolviendo al menu anterior")
                    confirmado = True
            if not utiles_validaciones.confirmacion("Desea modificar otro curso?"):
                    salida = True
        else:
            print("No hay cursos en el sistema.")


def buscar(conn):
    """
    Funcion que busca un curso en la bbdd
    :param conn: conexion a la bbdd
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) > 0:
        print("buscar cursos:")
        cursos = gestion_BBDD.selec_all_from_tabla(conn, "cursos")
        print("Nombre de los cursos: ", end="")
        for curso in cursos:
            print(curso[1], ", ", end="")
        print()
        done = False
        while not done:  #Para buscar mas de un profesor
            print("Introduzca el nombre del curso que desea buscar.")
            nombre = utiles_validaciones.check_campo("Nombre", 25)  #Pedimos dni valido
            if nombre is not None:
                curso = gestion_BBDD.selec_join(conn, "cursos", nombre)  #Encontramos al profesor
                print(len(curso))
                if len(curso) > 0:  #Si lo encuentra lo muestra
                    curNombre = ""
                    if len(curso[0]) == 6: #Todos los campos
                        for i in range(0, len(curso)):
                            if curNombre != curso[0][1]:
                                curNombre = curso[0][1]
                                print("Codigo del curso: ", curso[i][0])
                                print("Nombre: ", curso[i][1])
                                print("Descripcion:", curso[i][2])
                                if curso[i][3] is not None:
                                    print("Profesor:", curso[i][3])
                                if curso[i][4] is not None and curso[i][5] is not None:
                                    print("Alumno/os:" + curso[i][4] + "_" + curso[i][5], end="")
                            else:
                                if curso[i][4] is not None and curso[i][5] is not None:
                                    print(" | " + curso[i][4] + "_" + curso[i][5], end="")
                        print()

                    elif len(curso[0]) == 4: #Silo profesores
                        print("Codigo del curso: ", curso[0][0])
                        print("Nombre: ", curso[0][1])
                        print("Descripcion:", curso[0][2])
                        if curso[0][3] is not None:
                            print("Profesor:", curso[0][3])
                        print()

                    elif len(curso[0]) == 5: #solo alumnos
                        for i in range(0, len(curso)):
                            if curNombre != curso[0][1]:
                                curNombre = curso[0][1]
                                print("Codigo del curso: ", curso[i][0])
                                print("Nombre: ", curso[i][1])
                                print("Descripcion:", curso[i][2])
                                if curso[i][3] is not None and curso[i][4] is not None:
                                    print("Alumno/os:" + curso[i][3] + "_" + curso[i][3], end="")
                            else:
                                if curso[i][3] is not None and curso[i][4] is not None:
                                    print(" | " + curso[i][3] + "_" + curso[i][4], end="")
                        print()

                    elif len(curso[0]) == 3: #ni profesores ni alumnos
                        print("Codigo del curso: ", curso[0][0])
                        print("Nombre: ", curso[0][1])
                        print("Descripcion:", curso[0][2])
                        print()

                else:
                    print("No se encontro ningun curso con ese nombre.")

            if not utiles_validaciones.confirmacion("Desea buscar otro curso"):  #Pedimos confirmacion para buscar mas de uno
                done = True

    else:
        print("No hay cursos en la base de datos.")


def mostrar_todos(conn):
    """
    Funcion que muestra por pantalla todos los cursos de la base de datos
    :param conn: la conexion a la bbdd
    :return: None
    """
    cursos = gestion_BBDD.selec_all_from_tabla(conn, "cursos")
    if len(cursos) > 0:
        print("Mostrar todos los cursos:")
        for curso in cursos:
            print("Codigo del curso: ", curso[0])
            print("Nombre: ", curso[1])
            print("Descripcion:", curso[2])
            print()

    else:
        print("No hay cursos en la base de datos.")
