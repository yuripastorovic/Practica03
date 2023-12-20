"""
Este fichero Python se encarga de la gestion de las relaciones Alumno-Curso, Curso-Profesor
"""
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
    if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) > 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) > 0:
        done = False
        while not done:
            print("Relacionar profesores y cursos.")
            print("Introduzca el dni del profesor que desea relacionar.")
            curso = None
            dni = utiles_validaciones.check_dni()  #Pedimos dni para mas adelante coger el profesor
            if dni is not None:
                if not utiles_validaciones.unique_dni(conn, dni):  #Si el dni existe
                    curso = gestion_curso.busqueda_unica(conn)  #Pillamos el curso por el nombre
                else:
                    print("El dni no pertenece a ningun profesor"+"\n")
                    dni = None
            if curso is not None:

                profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)  #Pillamos el profesor
                datos = {"id_profesor": profesor[0][0], "cod_curso": curso[0]}  #Montamos el diccionario de datos
                if gestion_BBDD.existe_relacion(conn, "cursos_profesores", datos):  #Si ya estan relacionados se notifica, pues no tiene sentidos volver a hacer el mismo insert
                    print(profesor[0][2] + " ya imparte " + curso[1]+"\n")
                else:  #Si no estan relacionados
                    prof_ant = gestion_BBDD.tiene_profesor(conn, curso[0])  #Pillamos la posible relacion del curso
                    if len(prof_ant) > 0:  #Si el curso ya tenia profesor
                        if utiles_validaciones.confirmacion(curso[1] + " ya tiene profesor, desea sustituirlo por " + profesor[0][2] + "?"):  #Se pregunta si quiere sustituirlo
                            para_borrar = {"id_profesor": prof_ant[0][4], "cod_curso": curso[0]}
                            gestion_BBDD.delete(conn, "cursos_profesores", para_borrar)  #Deleteamos la antigua row
                            gestion_BBDD.insert(conn, "cursos_profesores", datos)  #Creamos la nueva
                            print("Relacion realizada con exito"+"\n")
                        else:
                            print("Relacion abortada"+"\n")
                    else:  #Si el curso no tiene relacion
                        if utiles_validaciones.confirmacion("Seguro que desea que " + profesor[0][2] + " imparta " + curso[1] + "?"):  #Preguntamos confirmacion
                            gestion_BBDD.insert(conn, "cursos_profesores", datos)  #Hacemos insert
                            print("Relacion realizada con exito"+"\n")
                        else:
                            print("Relacion abortada"+"\n")

            if not utiles_validaciones.confirmacion("Desea relacionar otro profesor con otro curso?"):  #Esto para relacionar mas de uno
                done = True
                print("-"*20+"\n")
            else:
                print("\n")
    else:
        if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) == 0:
            print("No existen ni cursos ni profesores")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0:
            print("No existen cursos")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) == 0:
            print("No existen profesores")
        print("-"*20+"\n")

def desmatricular_profesor_curso(conn):
    """
    Funcion que desbindea un profesor y un curso
    :param conn: la conexion a la bbdd
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) > 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) > 0:
        done = False
        while not done:

            print("Desrelacionar profesores y cursos.")
            curso = None
            dni = utiles_validaciones.check_dni()  #Pedimos del dni del profeosr
            if dni is not None:
                if not utiles_validaciones.unique_dni(conn, dni):
                    curso = gestion_curso.busqueda_unica(conn)  #conseguimos el curso por nombre
                else:
                    print("El dni no pertenece a ningun profesor"+"\n")
                    dni = None
            if curso is not None:

                profesor = gestion_BBDD.selec_one_from_tabla(conn, "profesores", dni)  #Cogemso el profesor por el dni
                datos = {"id_profesor": profesor[0][0], "cod_curso": curso[0]}  #Montamos el diccionario
                if gestion_BBDD.existe_relacion(conn, "cursos_profesores", datos):  #Si hay relacion
                    if utiles_validaciones.confirmacion("Seguro que desea que " + profesor[0][2] + " deje de ser el profesor de " + curso[1]):  #Pedimos confirmacion
                        gestion_BBDD.delete(conn, "cursos_profesores", datos)  #Deleteamos
                        print("Desrelacion realizada con exito"+"\n")
                    else:
                        print("Desrelacion abortada"+"\n")
                else:
                    print(profesor[0][2] + " no es el profesor de " + curso[1])  #si no hay relacion se notifica

            if not utiles_validaciones.confirmacion("Desea desrelacionar otro profesor con otro curso?"):  #Esto para desrealacionar mas de uno
                done = True
                print("-"*20+"\n")
            else:
                print("\n")
    else:
        if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) == 0:
            print("No existen ni cursos ni profesores")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0:
            print("No existen cursos")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "profesores")) == 0:
            print("No existen profesores")
        print("-"*20+"\n")


def matricular_curso_alumno(conn):
    """
    Funcion que permite matricular un alumno en un curso
    :param conn: Conexion con BBDD
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) > 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:
        salida = False
        while not salida:
            print("Relacionar alumnos y cursos.")
            alumno = gestion_alumno.busqueda_unica(conn)
            if alumno is not None:
                curso= gestion_curso.busqueda_unica(conn)
                if curso is not None:
                    if utiles_validaciones.confirmacion("Desea matricuar al alumno "+alumno[1]+", al curso "+curso[1]+"?"):
                        datos ={"num_exp": alumno[0], "cod_curso": curso[0]}
                        gestion_BBDD.insert(conn, "cursos_alumnos",datos)
                        print("Matriculacion realizada con exito"+"\n")
                    else:
                        print("Matriculacion abortada"+"\n")
            if not utiles_validaciones.confirmacion("Desea matricular otro alumno?"):
                print("Voviendo al menu anterior")
                salida = True
                print("-"*20+"\n")
            else:
                print("\n")
    else:
        if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) == 0:
            print("No existen ni cursos ni alumnos")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0:
            print("No existen cursos")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) == 0:
            print("No existen alumnos")
        print("-"*20+"\n")


def desmatricular_curso_alumno(conn):
    """
    Funcion que permite desmatricular un alumno de un curso
    :param conn: Conexion con BBDD
    :return: None
    """
    if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) > 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) > 0:
        salida = False
        while not salida:
            print("Relacionar alumnos y cursos.")
            alumno = gestion_alumno.busqueda_unica(conn)
            if alumno is not None:
                curso = gestion_curso.busqueda_unica(conn)
                if curso is not None:
                    aux = {"num_exp": alumno[0], "cod_curso":curso[0]}
                    if gestion_BBDD.existe_relacion(conn, "cursos_alumnos", aux):
                        if utiles_validaciones.confirmacion("Desea desmatricuar al alumno " + alumno[1] + ", al curso " + curso[1] + "?"):
                            datos = {"num_exp": alumno[0], "cod_curso": curso[0]}
                            gestion_BBDD.delete(conn, "cursos_alumnos", datos)
                            print("Desmatriculacion realizada con exito"+"\n")
                        else:
                            print("Desmatriculacion abortada"+"\n")
                    else:
                        print("El alumno " + alumno[1] + " no pertenece al curso "+curso[1])
            if not utiles_validaciones.confirmacion("Desea dematricular otro alumno?"):
                print("Voviendo al menu anterior")
                salida = True
                print("-"*20+"\n")
            else:
                print("\n")
    else:
        if len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0 and len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) == 0:
            print("No existen ni cursos ni alumnos")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "cursos")) == 0:
            print("No existen cursos")
        elif len(gestion_BBDD.selec_all_from_tabla(conn, "alumnos")) == 0:
            print("No existen alumnos")
        print("-"*20+"\n")
