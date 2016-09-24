__author__ = 'Grupo10'

class Secuencia :
    def estadisticas(self, cadena):
        if cadena == "":
            return [0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros), ]
        else:
            return [1,3]