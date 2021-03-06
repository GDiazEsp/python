'''
Curso : Programacion Basica de Python
Sesion : 03
Tema : Introduccion a Python -  Variables de clases
Fecha : 22/02/2020
Author : Jaime Gomez

'''

'''
Para debug en mac : export LC_ALL=C
'''

#''' Primera version
class Empleado:
    
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def incremento_sueldo(self):
        self.sueldo = int(self.sueldo * 1.10)

emp_01 = Empleado("Jaime","Gomez",1000)

print("{:-^80s}".format("-"))
print("emp_01 : ",emp_01.__dict__)
print("{:-^80s}".format("-"))
print("Empleado : ",Empleado.__dict__)

#'''

''' Segunda version
class Empleado:
    
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def incremento_sueldo(self):
        self.sueldo = int(self.sueldo * 1.10)

emp_01 = Empleado("Jaime","Gomez",1000)
print(emp_01.sueldo)
emp_01.incremento_sueldo()
#emp_01.sueldo = int(emp_01.sueldo * 1.10)
print(emp_01.sueldo)

emp_02 = Empleado("Oscar","Garcia",2000)
print(emp_02.sueldo)
emp_02.incremento_sueldo()
print(emp_02.sueldo)

#'''

#''' Tercera version
class Empleado:
    aumento = 1.10
    descuento = 0.95    
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def incremento_sueldo(self):
        self.sueldo = \
            int(self.sueldo * self.aumento)

    def descuento_sueldo(self):
        self.sueldo = \
            int(self.sueldo * self.descuento)

# Se instancia el objeto emp_01
emp_01 = Empleado("Jaime","Gomez",1000)

# Se cambia el incremento a la instancia
emp_01.aumento = 1.5   
print(emp_01.sueldo)
emp_01.incremento_sueldo()
print(emp_01.sueldo)

# Se cambia el incremento a la clase
Empleado.aumento = 1.5 

# Se instancia otro objeto emp_02 ,el incremento 
# ya se realizo a traves de la clase Empleado
emp_02 = Empleado("Oscar","Garcia",2000)
print(emp_02.sueldo)
emp_02.incremento_sueldo()
print(emp_02.sueldo)

#print(emp_01.__dict__)
#print(Empleado.__dict__)
#'''

''' Cuarta version
class Empleado:

    aumento  = 1.10
    nro_empleados = 0
    
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        Empleado.nro_empleados += 1
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def incremento_sueldo(self):
        self.sueldo = \
            int(self.sueldo * self.aumento)

emp_01 = Empleado("Jaime","Gomez",1000)
print(emp_01.nro_empleados)
print(Empleado.nro_empleados)
emp_02 = Empleado("Oscar","Garcia",2000)
#print(emp_02.nro_empleados)
print(Empleado.nro_empleados)
emp_03 = Empleado("Maribel","Alegria",3000)
#print(emp_03.nro_empleados)
print(Empleado.nro_empleados)

#''' 