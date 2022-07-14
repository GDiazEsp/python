'''
Programa: Fundamentos de Python
Sesión: 02: Introducción
Tema: 
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''
datos_personales={4:["Hiroito","Sanchez Hurtado","programador",1,"Activo"]}
print(datos_personales)
print(datos_personales.get(4))
value = datos_personales.get(4)
print(value[2])
print(value[3])
print(value[4])
value[4]="Inactivo"
print(value)
datos_personales[4]=value
print(datos_personales)