def menu_alumno():
    """
    Funcion que gestiona el menu alumno
    :param conn: Conexion con BBDD
    :return: None
    """
    espai = "\n\t\t\t[--]\t"+'\033[92m'
    espai1 = '\033[0m'+"\t\t[--]\n\t\t\t[--]\t"+'\033[92m'
    salida = False
    while not salida:
        respuesta = input(
            espai+" "*(15)+"--MENU ALUMNO--" + " " * (15) + espai1 + "Seleccione una opcion:" + " " * (23) + espai1 + "1. Alta" + " " * (37) + espai1 + "2. Baja" + " " * (37) + espai1 + "3. Buscar" + " " * (37) + espai1 + "4. Modificar" + " " * (35) + espai1 + "5. Mostrar Todos" + " " * (31) + espai1 +" "*(19)+ "------" + " " * (19) + espai1 + "0. Volver a Main Menu" + " " * (23) + espai1 + "")
        if respuesta is not None:
            if respuesta == "0":
                salida = True
            if respuesta == "1":
                salida = True
            if respuesta == "2":
                salida = True
            if respuesta == "3":
                salida = True
            if respuesta == "4":
                salida = True
            if respuesta == "5":
                salida = True
            else:
                print("Opcion no valida")
        else:
            print("\nIntroduzca una opcion valida\n")


menu_alumno()