'''
Programa: Fundamentos de Python
Sesión: 02: Introducción
Tema: Set
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''

#Para crear un conjunto (set), especificamos sus elementos entre llaves {}
conjunto1 = {1,2,3,4,"cinco",5,5}
print(type(conjunto1))
print(conjunto1)

a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a|b)
print(a&b)