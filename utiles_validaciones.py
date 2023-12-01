"""
this is ustiles_validaciones
"""


# UTILES
def fails(fallos):
    """
    Funcion de apoyo que cuenta el numero de fallos para los menus
    :param fallos: numero de fallos hasta ahora
    :return:  fallos: numero de fallos actualizado
    """
    fallos += 1;
    print(fallos + "/5 fallos antes de salir.")
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
    print(contexto + ": ")
    respuesta = input()
    if respuesta is not None and not respuesta.isspace():
        return respuesta
    else:
        print("El campo, " + contexto + " no puede estar vacio.")
        return None


# VALIDADORES
def check_campo(contexto, long):
    fallos = 0
    while fallos < 5:
        campo = entrada_teclado(contexto)
        if campo is not None:
            if campo.isalnum():
                if 0 < len(campo) <= long:
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


"arreglar fails"


def validar_dni():
    """
    funcion que pide un input, valida la longitud, y si es un dni
    """
    cont = 0
    while cont < 3:
        dni = input(
            "Introduzca un dni valido, este debe de tener 9 caracteres, los 8 primeros numeros y el ultimo una letra. ")
        if not dni.isspace():
            dni = dni.strip()  # El trim de python
            if len(dni) == 9:
                if dni[0:8].isnumeric():  # Es cerrado por la izquierda abierto por la derecha
                    if dni[8].isalpha():  # Solo coge el noveno caracter
                        print("DNI Valido.")
                        return dni
                    else:
                        cont += 1
                        print("El ultimo caracter debe tratarse de una letra. Fallos = ", cont)
                else:
                    cont += 1
                    print("Los primeros 8 caracteres deben tratarse de numeros. Fallos = ", cont)
            else:
                cont += 1
                print("El DNI debe de tener 9 caracteres. Fallos = ", cont)
        else:
            cont += 1
            print("La cadena no puede tratarse de una cadena vacia o solo de espacios, Fallos = ", cont)
    return None


def check_telefono():
    fallos = 0
    while fallos < 5:
        campo = entrada_teclado("telefono")
        if campo is not None:
            if campo.numeric():
                if len(campo) == 9:
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
    fallos = 0
    while fallos < 5:
        print("Recuerde el formato de la fecha es DD-MM-YYYY")
        fecha = entrada_teclado("telefono")
        if fecha is not None:
            datos = fecha.split("-")
            if datos[0].isnumeric() and datos[1].isnumeric() and datos[0].isnumeric():
                dia = int(datos[0])
                mes = int(datos[1])
                year = int(datos[2])
                if ((
                            mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and 0 < dia >= 31 and (
                            1990 <= year >= 2023)) or (
                        (mes == 4 or mes == 6 or mes == 9 or mes == 11) and 0 < dia >=30 and (1990 <= year >= 2023)) or (
                        mes == 2 and 0 < dia >=28 and (1990 <= year >= 2023)):
                    print()
                else:
                    print("No se corresponde con una fecha valida: para mas info--> https://es.wikipedia.org/wiki/Mes")
                    fallo = fails(fallos)
            else:
                print("Formato de fecha no valido")
                fallo = fails(fallos)
        else:
            fallo = fails(fallos)

    print("Se han producido 5 fallos.\nAbotortando proceso")
    return None
