import gestion_BBDD
import gestion_alumno
import gestion_curso
import gestion_profesor
import utiles_validaciones


def matricular_profesor_curso(conn):
    done = False
    while not done:
        print("Relacionar profesores y cursos.")
        print("Introduzca el dni del profesor que desea relacionar.")
        nomb_curso = None
        dni = utiles_validaciones.check_dni()
        if dni is not None and not utiles_validaciones.unique_dni(conn, dni):
            nomb_curso = utiles_validaciones.check_campo("Nombre", 25)
        if nomb_curso is not None and not utiles_validaciones.comprobar_nombre_curso(conn, nomb_curso):



        if not utiles_validaciones.confirmacion("Desea relacionar otro profesor con otro curso?")
            done = True


def desmatricular_profesor_curso():
    print("Desrelacionar profesores y cursos.")
    return None
