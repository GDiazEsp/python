'''
Programa: Fundamentos de Python
Sesión: 01: Introducción
Tema: Definiendo variables.
Fecha:062022
Versión: 1.1
Autor: Godofredo Diaz.
'''

#Definiendo una variable.
from re import X
from tkinter import Y


mi_variable1 = 1

mi_variabletxt = "Texto"

#1_variable = 1 #Una variable no puede iniciar con un número.

#$_variable = 1 #Una variable no puede iniciar con un caracter especial.

#if = 1 #Una variable no puede usar una palabra reservada.

'''
and     assert      break       class       continue
def     del         elif        else        except
exec    finally     for         from        global
if      import      in          is          lambda
not     or          pass        print       raise
return  try         while       
'''

x = 300 #300 es almacenado en x
print(x)
y = x  # ahora y hace referencia a x por lo que su valor será 300

x = 400
print (x)
print(y)