"""
Este fichero Python es desde donde se ejecuta el programa
"""
import menu
import gestion_BBDD

print("Inicio del programa")

conn = gestion_BBDD.mysqlconnect()

if conn is not None:
    menu.main_menu(conn)
    cursor = conn.cursor()
    conn.close()

print("Fin del programa")
