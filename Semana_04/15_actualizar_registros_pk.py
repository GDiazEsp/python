'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Conexion a BBDD
Fecha : 
Author : 
'''

# Importando librerias
import mysql.connector
from mysql.connector import errorcode

config =  {"host":"localhost", 
           "user":"prueba", 
           "password":"123456aB$", 
           "db":"hr"}

'''
#  Actualizar registros
conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = ("UPDATE employees "
        "SET first_name=%s, last_name =%s "
        "WHERE emp_no =%s" )

values = ("Maribel","Alegria",1)

cur.execute(sql, values)
conn.commit()

print(cur.rowcount, "Fueron actualizados.")

conn.close()

#'''

#'''
#  Actualizar registros con manejo de errores
conn = mysql.connector.connect(**config)
cur = conn.cursor()

sql = ("UPDATE employees "
        "SET first_name=%s, last_name =%s "
        "WHERE emp_no =%s" )

values = ("Maribel","Alegria",1)

try:
    cur.execute(sql, values)
    conn.commit()
    print(cur.rowcount, "Fueron actualizados.")
except mysql.connector.Error as err:
    print(err.msg)
else:
    print("OK")

conn.close()

#'''