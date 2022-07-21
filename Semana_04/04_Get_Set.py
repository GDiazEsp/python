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

class Lavadoras():
    #Definiendo el constructor.
    def __init__(self,estado="Apagada",color="Blanco",capacidad="12kg",voltaje="220v"):        
        self.estado = estado
        self.color = color
        self.capacidad = capacidad
        self.__voltaje = voltaje
        

    #Se define el comportamiento (métodos)
    def set_encender(self,status):
        self.estado = status

    def set_lavar(self):
        pass

    def set_enjuagar(self):
        pass

    def set_centrifugar(self):
        pass

    def get_Estado(self):
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
voltaje = LavadoraEG._Lavadoras__voltaje

print(color)
print(voltaje)
print(LavadoraEG.color)
LavadoraEG.color = "Plomo"
print(LavadoraEG.color)
