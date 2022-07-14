'''
Programa: Fundamentos de Python
Sesión: 02: 
Tema: 
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''


lista=list()
x=0
j=0

while j<11:
    if (j <= 10):
        lista.append(j) 
        j=j+1


print(lista)
tupla=tuple(lista)
print(tupla)