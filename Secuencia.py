__author__ = 'Grupo10'

class Secuencia :
    def estadisticas(self, cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            if len(numeros) == 2:
                return [len(numeros), int(min(numeros)), int(max(numeros)), (int(numeros[0])+int(numeros[1]))/2]
            else:
                suma = 0.0
                for i in range (0,len(numeros)):
                    suma = suma + int(numeros[i])
                return [len(numeros), int(min(numeros)), int(max(numeros)), suma/len(numeros)]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]