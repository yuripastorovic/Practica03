import gestion_BBDD
import gestion_alumno
import gestion_curso
import gestion_profesor
import utiles_validaciones


def matricular_profesor_curso(conn):
    """
    Funcion que crea la relacion entre cursos y profesores.
    :param conn: la conexion a la bbdd
    :return: None
    """
    done = False
    while not done:
        print("Relacionar profesores y cursos.")
        print("Introduzca el dni del profesor que desea relacionar.")
        curso = None
        dni = utiles_validaciones.check_dni()
        if dni is not None and not utiles_validaciones.unique_dni(conn, dni):
            curso = gestion_curso.busqueda_unica(conn)
        if curso is not None:

            profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)
            datos = {"id_profesor": profesor[0][0], "cod_curso": curso[0]}
            if gestion_BBDD.existe_relacion(conn, "cursos_profesores", datos):
                print(profesor[0][2] + " ya imparte " + curso[1])
            else:
                prof_ant = gestion_BBDD.tiene_profesor(conn, curso[0])
                if len(prof_ant) > 0:
                    if utiles_validaciones.confirmacion(curso[1] + " ya tiene profesor, desea sustituirlo por " + profesor[0][2] + "?"):
                        para_borrar = {"id_profesor": prof_ant[0][4], "cod_curso": curso[0]}
                        gestion_BBDD.delete(conn, "cursos_profesores", para_borrar)
                        gestion_BBDD.insert(conn, "cursos_profesores", datos)
                    else:
                        print("Relacion abortada")
                else:
                    if utiles_validaciones.confirmacion("Seguro que desea que " + profesor[0][2] + " imparta " + curso[1] + "?"):
                        gestion_BBDD.insert(conn, "cursos_profesores", datos)
                    else:
                        print("Relacion abortada")

        if not utiles_validaciones.confirmacion("Desea relacionar otro profesor con otro curso?"):
            done = True


def desmatricular_profesor_curso():
    print("Desrelacionar profesores y cursos.")
    return None
