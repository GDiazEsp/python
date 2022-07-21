'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Clases e Instancias
Fecha : 22/02/2020
Author : Jaime Gomez

'''

'''
Para debug en mac : export LC_ALL=C
'''


#''' Primera version
# Define una clase
class Empleado:

    def __init__(self):
        print("Se instancia una clase..!")      

emp_01 = Empleado() # Se instancia una clase
emp_02 = Empleado()

# Ejercicio: Al instanciar la clase Empleado, 
# Imprimir los numeros 2, 4, 6, 8

# Solucion 1
class Empleado:
    def __init__(self):
        for i in range(2,10,2):
            print(i)
emp_01 = Empleado()

# Solucion 2
class Empleado:

    def __init__(self):
        for i in [2,4,6,8]:
            print(i)

emp_01 = Empleado() # Se instancia una clase

# Solucion 3
class Empleado:
    def __init__(self):
        for i in range(2,9,2):
            print(i)   

emp_01 = Empleado() # Se instancia una clase


class Empleado:

    def __init__(self, dc=1):
        self.dia_cumple = dc # Inicializa un atributo
        print("Se instancia una clase..!")      

emp_01 = Empleado(21) # Se instancia una clase
emp_02 = Empleado(10)
emp_03 = Empleado()    # Falla porque no le paso argumento

'''
Ejercicio : En la clase Empleado
pasar en el constructor, el nombre, 
apellido, edad y dia de nacimiento
(Crear los atributos respectivo).
En caso no se pase la edad y el dia de
nacimiento , deberan ser 30 y 1
'''

# Solucion 01
class Empleado():
    def __init__(self,nomb,apell,edad=30,dn=1):
        self.nombre = nomb #inicializa un atributo
        self.apellido = apell
        self.edad = edad
        self.dia_nacimiento = dn
        print(' finalizado correctamente ')

emp_01 = Empleado('fernando','viton',22,22)

# Solucion 02
class Empleado:
    def __init__(self,nombre1,apellido1,edad1=30,dia1=1):
        self.nombre=nombre1
        self.apellido=apellido1
        self.edad=edad1
        self.dia=dia1
        print("atributos:",self.nombre,self.apellido,self.edad,self.dia)

emp_01 = Empleado("Ricardo","Gomez",15,2) # Se instancia una clase
emp_01 = Empleado("Ricardo","Gomez") # Se instancia una clase


# Clase
class Empleado:

    # Constructor
    def __init__(self,nombre,apellido,edad=30,dia=1):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dia = dia

    # Metodo
    def nombre_completo(self):
        nc = self.nombre + " " + self.apellido
        print(nc)

    def descripcion_info_personal(self):
        nc=self.nombre + " " + self.apellido + " tiene " + str(self.edad) + " años y nacio el " + str(self.dia)
        print(nc)

# Instanciar
emp_01 = Empleado("Ricardo","Gomez",15,2)

# Llama a un metodo
emp_01.nombre_completo() # No necesito pasar 
                         # el nombre y apellido
'''
Crear un metodo que me imprima los siguiente:
Ricardo Gomez tiene 15 años y nacio el 2
'''
emp_01.descripcion_info_personal()

#print(emp_01)
#print(emp_02)

emp_01.nombre = "Jaime"
emp_01.apellido = "Gomez"

print(emp_01.nombre)
print(emp_01.apellido)

emp_01.apellido = "Garcia"

print(emp_01.nombre)
print(emp_01.apellido)


# Crear el atributo dni en la clase Empleado
# y lo incluyas en el constructor
# Instancia llamada emp_10 , que tenga 
# la siguiente informacion:
#     nombre = "Pedrp"
#     apellido = "Galvez"
#     edad = 25
#     dni = "0435678"
#     dia = 13








# Crear el atributo DNI en emp_01 y darle un valor
# Crear los atributos nombre, apellido 
# y DNI en emp_02 , darle valores

emp_01.dni = "12345678"
print(emp_01.dni)

emp_02.nombre = "Juan"
emp_02.apellido = "Acosta"
emp_02.dni = "5652553"
print(emp_02.nombre)
print(emp_02.apellido)
print(emp_02.dni)

#'''


''' Segunda version
class Empleado:

    # Se define el constructor    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

#emp_01 = Empleado()
emp_01 = Empleado("Jaime","Gomez")

print(emp_01.nombre)
print(emp_01.apellido)
print(emp_01.nombre_completo())

emp_01.apellido = "Garcia"

print(emp_01.nombre)
print(emp_01.apellido)
print(emp_01.nombre_completo())

# Agregar el atributo dni a la clase Empleado y
# le pasas un valor al instanciar la clase

#'''

''' Tercera version
class Empleado:
    
    def __init__(self, nombre, apellido):
        #super().__init__()
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

emp_01 = Empleado("Jaime","Gomez")

print(emp_01.nombre_completo())
print(Empleado.nombre_completo(emp_01))
print(type(emp_01))
#'''
