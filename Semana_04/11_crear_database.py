'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Conexion a BBDD
Fecha : 
Author : 
'''

# Importando librerias
import mysql.connector

'''
# Mostrar esquemas de base de datos
config =  {"host":"localhost", 
           "user":"prueba", 
           "password":"123456aB$"}

conn = mysql.connector.connect(**config)
cur = conn.cursor()
sql = "SHOW DATABASES"  # input
cur.execute(sql)

# output cur
print(type(cur))

for line in cur:
    print(type(line)) 
    print(line)

# Cerrar conexion
conn.close()

#'''


# Crear esquema de base de datos

config =  {"host":"69.73.180.151", 
           "user":"asesores_python", 
           "password":"T3c5up00--",  
           "db":"asesores_python"}

conn = mysql.connector.connect(**config)
cur = conn.cursor()
sql = "CREATE DATABASE hr"
cur.execute(sql)
conn.close()



'''
# Verifica que esquema de base de datos exista

config =  {"host":"localhost", 
           "user":"prueba", 
           "password":"123456aB$", 
           "db":"hr"}

conn = mysql.connector.connect(**config)
print(conn)
conn.close()

#'''

