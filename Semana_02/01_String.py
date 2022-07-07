'''
Programa: Fundamentos de Python
Sesión: 02: Tipo de datos
Tema: String.
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''

msg = "Mi nuevo mensaje"

'''
---------------------------------------
|M|i| |n|u|e|v|o| |m|e |n |s |a |j |e |
---------------------------------------
|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|
---------------------------------------
'''
print(msg[3])    #Imprimiendo el index 3
print(msg[3:8:1])  #Imprimiendo desde el index 3 a index 8 saltando de 1 en 1 [3:8:1]

print(msg.upper())  #Convirtiendo a mayúsculas

print(msg.lower())  #Convirtiendo a minúsculas

print(msg.swapcase())    # Pone la primera letra en minúscula.
print(msg.capitalize())  #Pone la primera letra en mayúscula.
print(msg.find("nuev"))  #Devuelve la posición de n
print(msg.find("z"))     #Devuelve -1 si no encuentra lo buscado
print(msg.rfind("e"))    # Devuelve la última posición de lo buscado.
exp = "z" in msg
print(exp)
print(msg.count("i"))
print(msg.replace(" ","_"))
print(msg)

horizontal = "*"*20
vertial = "| \t|"


print(horizontal)
print(vertial)
print(horizontal)