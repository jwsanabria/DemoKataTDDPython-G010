from unittest import TestCase

from Secuencia import Secuencia

class SecuenciaTest(TestCase):
    def test_estadisticas(self):
        self.assertEqual(Secuencia().estadisticas(""), [0, 0,], "Cadena vacia")

    def test_estadisticas_cadenaConUnNumero(self):
        self.assertEqual(Secuencia().estadisticas("1"), [1, ], "Cadena con un numero")

    def test_estadisticas_cadenaConDosNumeros(self):
        self.assertEqual(Secuencia().estadisticas("1,3"), [2, ], "Cadena con dos numeros")

    def test_estadisticas_cadenaConVariosNumeros(self):
        self.assertEqual(Secuencia().estadisticas("1,3,5,6,7"), [5, ], "Cadena con dos numeros")