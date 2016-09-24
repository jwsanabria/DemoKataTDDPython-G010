from unittest import TestCase

from Secuencia import Secuencia

class SecuenciaTest(TestCase):
    def test_estadisticas(self):
        self.assertEqual(Secuencia().estadisticas(""), [0,], "Cadena vacia")
