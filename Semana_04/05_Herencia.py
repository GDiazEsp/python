'''
Curso : Programacion Basica de Python
Sesion : 04
Tema : Introduccion a Python -  Introduccion a clases
Fecha : 07/2022
Author : Godofredo Diaz

'''


'''
Objeto: Lavadora de ropa
Estado: [encendida,pausa,apagada]
Propiedades: [Color,capacidad]
Comportamiento: [lavar,centrifugar,enjuagar]
'''

class Artefactos:

    def __init__(self, marca = None, estado="Apagada"):
        self.marca = marca
        self.estado = estado
    
    def get_encender(self):
        print(self.estado)


class Lavadoras(Artefactos):
    def __init__(self, marca = None, estado="Apagada"):
        self.marca = marca
        self.estado = estado
        
    def lavar(self):
        if self.estado == "Encender":
            print("Lavando")
        else:
            print("Para lavar tienens que encender.")

class Licuadora(Artefactos):
    pass

lavadora = Lavadoras(marca="LG",estado="Pausa")
lavadora.get_encender()
lavadora.lavar()

Licuadora01 = Licuadora(marca="Oster",estado="Encendida")
print(Licuadora01.marca)
Licuadora01.get_encender()