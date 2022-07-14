'''
Programa: Fundamentos de Python
Sesión: 02: Introducción
Tema: Lista
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''
lista = [9,2.5,"Tecsup",[5,6,[7,9]],4]
print(lista)
print(lista[3][0])
print(lista[3][2][1])

for element in lista:
    print(element)

list = [1,2,3,4,5,5]
total = 0
for i in list:
    total = total +i

print(total)