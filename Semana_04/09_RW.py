import csv



class Lectura:
    def __init__(self):
        pass
    def leerarchivo(self):
       with open('medallero.csv', newline='') as csvfile:
           spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
           for row in spamreader:
               print(', '.join(row))


leer = Lectura()
leer.leerarchivo()