'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Introduccion a clases
Fecha : 07/2022
Author : Godofredo Diaz

'''


'''
Objeto: Celular
Estado: [encendido,apagado]
Propiedades: [marca,modelo,color,estado]
Comportamiento: [llamar,navegar,tomar_fotos,chatear,jugar,encender,apagar]
'''

class Celular:
    def __init_(self,marca=None,modelo=None,color=None,estado=False):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estado = estado
    

    def encender(self,enciende):
        self.estado = enciende
        if self.estado == True:
            print("Celular encendido.")
        else:
            print("Celular apagado.")

    def apagar(self,apaga):
        if self.estado == False:
            print("Apagando celular.")
        else:
            print("Celular encendido.")

    
    def llamar(self,numero):
        print("LLamando al número: ", numero)
        
    def navegar(self,web):
        print("Ingregando al página web:", web)

    def tomar_fotos(self):
        pass
    def chatear(self):
        pass
    def jugar(self):
        pass

    def estado(self):
        pass


Celular01 = Celular()
Celular01.encender(enciende=False)
Celular01.llamar(numero=989826008)
Celular01.navegar(web="https://www.tecsup.edu.pe")