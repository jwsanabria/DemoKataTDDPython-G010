__author__ = 'Grupo10'

class Secuencia :
    def estadisticas(self, cadena):
        if cadena == "":
            return [0, 0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            if len(numeros) == 2:
                return [len(numeros), int(min(numeros)), int(max(numeros))]
            else:
                return [len(numeros), int(min(numeros)), int(max(numeros))]
        else:
            return [1, int(cadena), int(cadena)]