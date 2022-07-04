'''
Programa: Fundamentos de Python
Sesión: 01: Introducción
Tema: Definiendo variables.
Fecha:072022
Versión: 1.2
Autor: Godofredo Diaz.
'''

import sys  #Importar libreria sys para usar la función getrefcount()
import keyword   #Importar libreria keyword para identificar las palabras reservadas.



Variable1 = [0,1,2,3,4]                     # Definiendo una nueva variable.
print(type(Variable1))                      #Identificando el tipo de variable.
referencias= sys.getrefcount(Variable1)     #Identificanto el número de referencias.
print(referencias)
print("ID:",id(Variable1),"TIPO:",type(Variable1),"VALOR:",Variable1)

Variable2 = Variable1                       #Agregando una nueva referencia a la Variable1
referencias= sys.getrefcount(Variable1)
print(referencias)                         #Imprimiendo el nuevo número de referencias.
print("ID:",id(Variable2),"TIPO:",type(Variable2),"VALOR:",Variable2)

print(keyword.kwlist)                       #Identificando las palabras reservadas.

#Nombre de variables - Revisar: https://peps.python.org/pep-0008/
