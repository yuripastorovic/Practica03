"""
this is gestion_profesion
"""
import utiles_validaciones
import gestion_BBDD


def alta(conn):
    """
    Funcion que pide los datos de un profesor y lo inserta en la bbdd
    :param conn: que realiza el insert
    :return: None
    """
    print("Alta profesor:")
    done = False
    while not done:  #Para dar de alta varios profesores en una ejecucion de la funcion
        dni = None
        nombre = None
        direccion = None
        telefono = None  #Las varaibles
        dni = utiles_validaciones.check_dni()  #Comprobamos que los campos son validos
        if dni is not None:
            nombre = utiles_validaciones.check_campo("nombre", 25)
        if nombre is not None:
            direccion = utiles_validaciones.check_campo("direccion", 50)
        if direccion is not None:
            telefono = utiles_validaciones.check_telefono()
        if telefono is not None:
            datos = {"dni": dni, "nombre": nombre, "direccion": direccion, "telefono": telefono}  #Pasamos los datos a un diccionario

            gestion_BBDD.insert(conn, "profesores", datos)  #Realizamos el insert

            print("Alta realizada con existo")

        if not utiles_validaciones.confirmacion("Quieres tratar de dar de alta otro profesor?"):  #Preguntamos si quiere dar otro profesor de alta
            done = True


def baja(conn):
    """
    Funcion que elimina a un profesor de la base de datos
    :param conn: la conexion a la base de datos
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) > 0:  #Comprobamos que la tabla tenga profesores
        print("Baja profesor:")
        done = False
        while not done:  #Para dar de baja mas de uno
            print("Introduzca el DNI del profesor que desea eliminar del sistema.")
            dni = utiles_validaciones.check_dni()  #pedimos dni valido
            if dni is not None:
                profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)  #Cogemos el profesor que corresponde al dni
                if len(profesor) > 0:  #Si lo encuentra
                    if utiles_validaciones.confirmacion("Seguro que desea eliminar a " + profesor[0][2] + " del sistema?"):  #pedimos confirmacion

                        gestion_BBDD.delete(conn, "profesores", dni)  #Mandamos el delete
                        print("Baja realizada con existo")

                    else:
                        print("No se encontro ningun profesor con ese DNI.")

            if len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) > 0 and not utiles_validaciones.confirmacion("Desea dar de baja otro profesor"):  #Si quedan profesores y no quiere borrar mas salimos
                done = True
            if len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) == 0:  #Si no quedan profesores salimos
                done = True
    else:  #Si no hay profesores
        print("No hay profesores en el centro.")


def buscar(conn):
    """
    Funcion que busca y muestra un profesor de la base de datos
    :param conn: la conexion a la bbdd
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) > 0:  #Si hay profesores
        print("buscar profesor:")
        done = False
        while not done:  #Para buscar mas de un profesor
            print("Introduzca el DNI del profesor que desea buscar.")
            dni = utiles_validaciones.check_dni()  #Pedimos dni valido
            if dni is not None:
                profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)  #Encontramos al profesor
                if len(profesor) > 0:  #Si lo encuentra lo muestra
                    print("ID: ", profesor[0][0])
                    print("Nombre: ", profesor[0][2])
                    print("DNI: ", profesor[0][1])
                    print("Descripcion: ", profesor[0][3])
                    print("Telefono: ", profesor[0][4])
                    print()

                else:
                    print("No se encontro ningun profesor con ese DNI.")

            if not utiles_validaciones.confirmacion("Desea buscar otro profesor"):  #Pedimos confirmacion para buscar mas de uno
                done = True
    else:  #Si no hay profesores
        print("No hay profesores en el centro.")


def mostrar_todos(conn):
    """
    Funcion que muestra todos los profesores de la bbdd
    :param conn:
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) > 0:  #Si hay profesores en la BBDD
        print("Mostrar todos los profesores:")

        profesores = gestion_BBDD.selec_all_from_tabla(conn, "profesores")  #Pilla todos los profesores
        for row in profesores:  #Recorremos las row de profesores mostrando los profesores
            print("ID: ", row[0])
            print("Nombre: ", row[2])
            print("DNI: ", row[1])
            print("Descripcion: ", row[3])
            print("Telefono: ", row[4])
            print()

    else:  #Si no hay profesores
        print("No hay profesores en el centro.")


def modificar(conn):
    """
    Funcion que modifica un profesor de la bbdd
    :param conn: la conexion a la bbdd
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) > 0:  #Comprobamos que la tabla tenga profesores
        print("Baja profesor:")
        done = False
        while not done:  #Para dar de baja mas de uno
            print("Introduzca el DNI del profesor que desea eliminar del sistema.")
            dni = utiles_validaciones.check_dni()  #pedimos dni valido
            if dni is not None:
                profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)
                if len(profesor) > 0:  #Si lo encuentra
                    print("Menu de modificacion:")  #Se entra en el menu de profesores
                    datos = {"dni": profesor[0][1], "nombre": profesor[0][2], "direccion": profesor[0][3], "telefono": profesor[0][4]}  #Construimos el diccionario
                    elec = ""
                    while elec != "0":  #Menu de modificacion
                        if elec == "1":  #Cambio de nombre. Se pide nuevo nombre, si se acepta la confirmacion se cambia en el diccionario y se manda a uodatear.
                            print("Nuevo ", end="")
                            nombre = utiles_validaciones.check_campo("Nombre", 25)
                            if utiles_validaciones.confirmacion("Seguro que desea cambiar el nombre: " + datos["nombre"] + " por " + nombre + "?"):
                                datos["nombre"] = nombre
                                gestion_BBDD.update(conn, "profesores", datos, dni)
                                print("Modificacion realizada exitosamente")
                            else:
                                print("Modificacion cancelada")

                        elif elec == "2":  #Cambio de dni. Se pide nuevo nombre, si se acepta la confirmacion se cambia en el diccionario y se manda a uodatear.
                            print("Nuevo ", end="")
                            dni2 = utiles_validaciones.check_dni()
                            if utiles_validaciones.confirmacion("Seguro que desea cambiar el dni:  " + datos["dni"] + " por " + dni2 + "?"):
                                datos["dni"] = dni2
                                gestion_BBDD.update(conn, "profesores", datos, dni)
                                dni = dni2  #Se actualiza el valor de la unique que se usa para buscar
                                print("Modificacion realizada exitosamente")
                            else:
                                print("Modificacion cancelada")

                        elif elec == "3":  #Cambio de descripcion. Se pide nuevo nombre, si se acepta la confirmacion se cambia en el diccionario y se manda a uodatear.
                            print("Nuevo ", end="")
                            descripcion = utiles_validaciones.check_campo("Descripcion", 50)
                            if utiles_validaciones.confirmacion("Seguro que desea cambiar la descripcion:  " + datos["descripcion"] + " por " + descripcion + "?"):
                                datos["descripcion"] = descripcion
                                gestion_BBDD.update(conn, "profesores", datos, dni)
                                print("Modificacion realizada exitosamente")
                            else:
                                print("Modificacion cancelada")

                        elif elec == "4":  #Cambio de telefono. Se pide nuevo nombre, si se acepta la confirmacion se cambia en el diccionario y se manda a uodatear.
                            print("Nuevo ", end="")
                            telefono = utiles_validaciones.check_telefono()
                            if utiles_validaciones.confirmacion("Seguro que desea cambiar el telefono:  " + datos["telefono"] + " por " + telefono + "?"):
                                datos["telefono"] = telefono
                                gestion_BBDD.update(conn, "profesores", datos, dni)
                                print("Modificacion realizada exitosamente")

                            else:  #Se sale
                                print("Modificacion cancelada")
                        elif elec == "0":
                            print("Saliendo del menu de modificacion.")

                        else:  #Opcion no valida
                            print("Opcion no valida.")

                    if not utiles_validaciones.confirmacion("Desea modificar otro profesor?"):  #Para modificar mas de un profesor
                        done = True
                else:
                    print("No se encontro ningun profesor con ese DNI.")
    else:  #Si no hay profesores
       print("No hay profesores en el centro.")
