import unittest
from game.rey import Rey

class Test_rey(unittest.TestCase):
    def setUp(self) -> None:
        self.rey_pruebanegro = Rey('BLACK')
        self.rey_pruebablanco = Rey('WHITE')

    def test_movimiento_diagonal(self):
        self.assertTrue(self.rey_pruebablanco.movimiento(4,4, 5,5))
        self.assertTrue(self.rey_pruebablanco.movimiento(4,4, 3,3))
        self.assertTrue(self.rey_pruebablanco.movimiento(4,4, 3,5))
        self.assertTrue(self.rey_pruebablanco.movimiento(4,4, 5,3))

        
    def test_movimiento_horizontal(self):
        self.assertTrue(self.rey_pruebanegro.movimiento(3,3, 4,3))
        self.assertTrue(self.rey_pruebanegro.movimiento(3,3, 3,2))
        self.assertTrue(self.rey_pruebanegro.movimiento(3,3, 2,3))
        self.assertTrue(self.rey_pruebanegro.movimiento(3,3, 3,4))


    def test_movim_erróneos(self):
        self.assertFalse(self.rey_pruebablanco.movimiento(4,4, 2,6))
        self.assertFalse(self.rey_pruebablanco.movimiento(4,4, 0,0))
        self.assertFalse(self.rey_pruebablanco.movimiento(4,4, 7,1))

        self.assertFalse(self.rey_pruebablanco.movimiento(4,4, 1,4))
        self.assertFalse(self.rey_pruebablanco.movimiento(4,4, 7,7))
        self.assertFalse(self.rey_pruebablanco.movimiento(4,4, 4,2))
        self.assertFalse(self.rey_pruebablanco.movimiento(4,4, 4,6))
if __name__ == '__main__':
    unittest.main()