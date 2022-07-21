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

class Lavadoras:
    #Se define las propiedades (atributos)
    estado = "Apagada"
    color = "Blanco"
    capacidad = "12kg"

    #Se define el comportamiento (métodos)
    def encender(self,status):
        self.estado = status

    def lavar(self):
        pass

    def enjuagar(self):
        pass

    def centrifugar(self):
        pass

    def Estado(self):
        if self.estado == "Apagada":
            print("La lavadora está apagada")
        elif self.estado == "Pausa":
            print("La lavadora está pausada")
        elif self.estado == "Encender":
            print("La lavadora está encendida")
        else:
            print("La lavadora")
        



#Instanciar un objeto.
LavadoraEG = Lavadoras()
#Llamando a un comportamiento.
color = LavadoraEG.color
print(color)
print(LavadoraEG.color)
#Cambiando el color de la lavadora.
LavadoraEG.color = "Plomo"
print(LavadoraEG.color)
LavadoraEG.Estado()
LavadoraEG.encender("Encender")
LavadoraEG.Estado()
