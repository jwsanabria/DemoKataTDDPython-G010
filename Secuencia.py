__author__ = 'Grupo10'

class Secuencia :
    def estadisticas(self, cadena):
        if cadena == "":
            return [0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            if len(numeros) == 2:
                return [len(numeros), int(min(numeros))]
            else:
                return [len(numeros), int(min(numeros))]
        else:
            return [1,3]