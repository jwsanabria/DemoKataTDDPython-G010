__author__ = 'Grupo10'

class Secuencia :
    def estadisticas(self, cadena):
        if cadena == "":
            return [0, ]
        elif "," in cadena:
            return [2, ]
        else:
            return [1, ]