"""
this is ustiles_validaciones
"""
from datetime import datetime


# UTILES
def fails(fallos):
    """
    Funcion de apoyo que cuenta el numero de fallos para los menus
    :param fallos: numero de fallos hasta ahora
    :return:  fallos: numero de fallos actualizado
    """
    fallos += 1;
    print(fallos, "/5 fallos antes de salir.")
    return fallos


def confirmacion(contexto):
    """
    Funcion de apoyo que responde y filtra entre dos opciones
    :param contexto: cadena que explica el contexto de la situaccion
    :return: True: acepta
    :return: False: no acepta
    """
    elect = ""
    while elect != "1" or elect != "2":
        print(contexto)
        elect = input("1. Si\n2.No\n")
        if elect == "1":
            return True
        elif elect == "2":
            return False
        else:
            print("Opcion no valida.")


def entrada_teclado(contexto):
    """
    Funcion de apoyo que cerciora que la cadena que se introduce no este vacia
    :param contexto: informcacion sobre el campo
    :return: respuesta: si el campo es correcto
    :return: None: si el campo esta vacio
    """
    print(contexto.capitalize() + ": ")
    respuesta = input()
    if respuesta is not None and not respuesta.isspace():
        return respuesta.strip()
    else:
        print("El campo, " + contexto + " no puede estar vacio.")
        return None


# CHECKERS
def check_campo(contexto, long):
    """
    Funcion de apoyo que cerciora que la cadena que se introduce tiene como maximo una longitud y ademas es alfanumerica
    :param contexto: Explicacion del campo al que se refiere
    :param long: longitud maxima de la cadena
    :return: campo si este cumple las validaciones
    :return: None si se falla 5 veces en la introduccion del campo
    """
    fallos = 0
    while fallos < 5:
        campo = entrada_teclado(contexto)
        if campo is not None:
            if campo.isalnum():
                long = int(long)
                if 0 < len(campo) <= long:
                    print(contexto + " introducido con exito.")
                    return campo
                else:
                    print(contexto + " tiene una longituz no valida, longitud maxima: " + long)
                    fallo = fails(fallos)
            else:
                print(contexto + "contiene caracteres no validos")
                fallo = fails(fallos)
        else:
            fallo = fails(fallos)
    print("Se han producido 5 fallos.\nAbotortando proceso")
    return None


def check_dni():
    """
    Funcion de apoyo que cerciora que se introduce un DNI valido
    :return: dni, si es valido
    :return: None, si se falla 5 veces en la introduccion de DNI
    """
    fallo = 0
    while fallo < 5:
        print("Recuerde el formato de un DNI valido es 00000000A")
        dni = entrada_teclado("DNI")
        if dni is not None:
            if len(dni) == 9:
                if dni[0:8].isnumeric():  # Es cerrado por la izquierda abierto por la derecha
                    if dni[8].isalpha():  # Solo coge el noveno caracter
                        print("DNI introducido con exito.")
                        return dni
                    else:
                        print("El ultimo caracter debe tratarse de una letra.")
                        fallo = fails(fallo)
                else:
                    print("Los primeros 8 caracteres deben tratarse de numeros.")
                    fallo = fails(fallo)
            else:
                print("El DNI debe de tener 9 caracteres.")
                fallo = fails(fallo)
        else:
            fallo = fails(fallo)

    print("Se han producido 5 fallos.\nAbotortando proceso")
    return None


def check_telefono():
    """
    Funcion de apoyo que cerciora que se introduce un telefono valido
    :return: telefono, si esta es valida
    :return: None, si se falla 5 veces en la introduccion de un telefono
    """
    fallos = 0
    while fallos < 5:
        campo = entrada_teclado("telefono")
        if campo is not None:
            if campo.numeric():
                if len(campo) == 9:
                    print("Telefono introducido con exito.")
                    return campo
                else:
                    print("Telefono tiene una longituz no valida, longitud debe ser: 9")
                    fallo = fails(fallos)
            else:
                print("Telefono contiene caracteres no validos")
                fallo = fails(fallos)
        else:
            fallo = fails(fallos)
    print("Se han producido 5 fallos.\nAbotortando proceso")
    return None


def check_fecha():
    """
    Funcion de apoyo que cerciora que se introduce una fecha valida
    :return: fecha, si esta es valida
    :return: None, si se falla 5 veces en la introduccion de una fecha
    """
    fallos = 0
    while fallos < 5:
        print("Recuerde el formato de la fecha es DD-MM-YYYY")
        fecha = entrada_teclado("fecha")
        if fecha is not None:
            datos = fecha.split("-")
            if datos[0].isnumeric() and datos[1].isnumeric() and datos[0].isnumeric():
                dia = int(datos[0])
                mes = int(datos[1])
                year = int(datos[2])
                if (((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and 0 < dia >= 31 and (1990 <= year >= 2023)) or
                        ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and 0 < dia >=30 and (1990 <= year >= 2023)) or
                        (mes == 2 and 0 < dia >= 28 and (1990 <= year >= 2023))):
                    print("Fecha introducido con exito.")
                    return datetime.date(dia, mes, year)
                else:
                    print("No se corresponde con una fecha valida: para mas info--> https://es.wikipedia.org/wiki/Mes\n")
                    fallo = fails(fallos)
            else:
                print("Formato de fecha no valido")
                fallo = fails(fallos)
        else:
            fallo = fails(fallos)

    print("Se han producido 5 fallos.\nAbotortando proceso")
    return None


#UNIQUES

def unique_nombre_curso(comparacion): # comprueba que el nombre del curso no esta ocupado ya si lo esta al nuevo le asigna +1
    return None


def unique_dni(comparacion):# comprueba que el dni del profesor es unico, que no esta en uso
    return None


def unique_nombre_completo(comparacion):# comprueba que el nombre completo del alumno es unico, que no esta en uso
    return None
