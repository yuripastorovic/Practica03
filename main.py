import utiles_validaciones
import gestion_alumno
import gestion_BBDD
"""
this is the main
"""
conn = gestion_BBDD.mysqlconnect()
gestion_alumno.busqueda(conn)

#utiles_validaciones.check_fecha()
