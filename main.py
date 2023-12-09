"""
Este fichero Python es desde donde se ejecuta el programa
"""
import menu
import gestion_BBDD

print("Inicio del programa")
conn = gestion_BBDD.mysqlconnect()
menu.main_menu(conn)
conn.close()
print("Fin del programa")