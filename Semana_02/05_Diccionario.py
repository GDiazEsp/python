'''
Programa: Fundamentos de Python
Sesión: 02: Introducción.
Tema: Diccionario.
Fecha:072022
Versión: 1.1
Autor: Godofredo Diaz.
'''
#Sintaxis
diccionario = {"clave":"valor","llave":"dato"}


diccionario = {
    "clave":"valor",
    "llave":"dato"
    }

arqueros = {1:"Pedro Gallese",2:"Carlos Càceda"}

for var in arqueros.items():
    print(var)

print(len(arqueros))
print(arqueros.keys())

for var in arqueros.values():
    print(var)
salir = 0





while salir ==0:
    print("Desa salir")
    diccionario = {}
    usuario = input("Ingrese su nombre de usuario:")
    email = input("Igrese su dirección de correo:")
    password = input("Ingreser su contraseña:")
    lista = [email,password]
    diccionario[usuario]= lista
    print(diccionario)




    salir=1

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))