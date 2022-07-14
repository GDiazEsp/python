'''
Programa: Fundamentos de Python
Sesión: 02: Tipo de datos
Tema: Tuplas.
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''

mi_tupla = ("M","i"," ","n","u","e","v","o"," ","m","e","n","s","a","j","e")

'''
---------------------------------------
|M|i| |n|u|e|v|o| |m|e |n |s |a |j |e |
---------------------------------------
|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|
---------------------------------------

'''

print(type(mi_tupla))
print(mi_tupla[5])
print(len(mi_tupla))

#Recorrer una Tupla con for.
# for <i> in <variable>:
#    <lógica>

for indice in mi_tupla:
    print (indice)


#Usando un if
# if <condición>:
#   <código si es verdadero>
#<código si es falso>

tupla = (5,4,4.5)
tipo_variable = type(tupla[2])

if tipo_variable == str :
    print("Es una cadena.") 



if tipo_variable == str :
        print("Es una cadena.") 
else:
    print("No es una cadena")


if tipo_variable == str :
    print("Es una cadena.") 
elif tipo_variable == int :
    print("Es un entero")
elif tipo_variable == float :
    print("Es un float")
else:
    print("No es una cadena ni es un entero")

print("línea 61")

