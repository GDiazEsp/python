'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Introduccion a clases
Fecha : 07/2022
Author : Godofredo Diaz

'''
class Lectura0:
    def __init__(self):
        pass
    def leerarchivo(self):
        miarchivo =open("archivo1.txt","r")
        lineast = miarchivo.readline()
        print(lineast[0],lineast[1],lineast[2])
        miarchivo.close()
        print(type(lineast))

class Lectura1:
    def __init__(self):
        pass
    def leerarchivo(self):
        miarchivo =open("archivo1.txt","r")
        lineast = miarchivo.readline()
        miarchivo.close()
        suma =0
        for i in lineast:
            suma = suma+int(i)
        
        print("La suma total es: ",suma)


class Lectura:
    def __init__(self):
        pass
    def leerarchivo(self):
        miarchivo =open("archivo1.txt","r")
        
        print(miarchivo.readline())
        miarchivo.seek(2)
        print(miarchivo.readline())
        miarchivo.close()
        

leer = Lectura()
leer.leerarchivo()