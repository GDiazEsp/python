'''
Programa: Fundamentos de Python
Sesión: 01: Introducción
Tema: Identidad, tipo y valor.
Fecha:062022
Versión: 1.1
Autor: Godofredo Diaz.
'''


'''
Python trata los datos como objetos
por lo que cada objeto tiene:
Identidad: Identifica al objeto
Tipo: Tipo dato al que pertenece
Valor: Caracteristica particular que puede ser mutable o inmutable.
'''

#La función id(), identifica la identidad de la variable.
variable = 25
print("Identidad: ", id(variable))
#La función type(), identifica el tipo de dato.
x =1
print("Tipo: ",type(x))
#<class 'int'>


print("Valor: ",x)
#1
