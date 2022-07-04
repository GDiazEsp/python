'''
Programa: Fundamentos de Python
Sesión: 01: Introducción
Tema: Números.
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''

#import operator  #Importar libreria operator para manipular números
#Revisar: https://docs.python.org/es/3/library/operator.html

x, y, z, n= 5, 3, 10, 3 #Definimos cuatro variables en una sola línea.
'''
OPERACIONES QUE SE PUEDEN REALIZAR CON NÚMEROS:
x + y           Sumar
x - y           Restar
x * y           Multiplicar
x / y           Dividir
x // y          Devuelve el cociente de la division de x entre y.
x % y           Devuelve el resto de la división de x entre y
x ** y          Potenciación
-x              Cambia el signo de x, siempre y cuando x sea diferente a 0
abs(x)          Devuelve el valor absoluto de x
divmod(x,y)     Devuelve el cociente y el resto como una tupla
pow(x,y)        Eleva x a la potencia de y
pow(x,y,z)      Una alternativa más rápida a (x ** y) % z
round(x,n)      Devuelve x redondeado a n dígitos enteros si n es un int negativo
                o devuelve x redondeado a n lugares decimales si n es un int positivo;
                el valor devuelto tiene el mismo tipo que x.

'''

print(round(x,n))
