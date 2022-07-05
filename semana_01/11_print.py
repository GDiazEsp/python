'''
Programa: Fundamentos de Python
Sesión: 01: Introducción
Tema: Print.
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''

#print("Primera línea","\n","Segunda línea")
#print("Primera línea\n","Segunda línea")
#print("Primera línea","\nSegunda línea")

print('{2}{0}{2}'.format("A","B","c"))

horizontal= "*"*60
vertical1="*\n"*2
descrip = "Descripción"
print(horizontal)
print(vertical1,)
print(vertical1,descrip)

print(vertical1)
