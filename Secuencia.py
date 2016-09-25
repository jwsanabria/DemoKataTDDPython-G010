__author__ = 'Grupo10'

class Secuencia :
    def estadisticas(self, cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros), int(min(numeros)), int(max(numeros)), self.promedio(numeros)]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]


    def promedio(self,numeros):
        suma = 0.0
        for i in range(0, len(numeros)):
            suma = suma + int(numeros[i])
        return suma / len(numeros)