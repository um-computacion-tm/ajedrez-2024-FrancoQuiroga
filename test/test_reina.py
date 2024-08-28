import unittest
from game.reina import Reina

class Test_reina(unittest.TestCase):
    def setUp(self) -> None:
        self.reina_prueba_blanca = Reina('WHITE')
        
        self.reina_prueba_negra = Reina('BLACK')

    def test_movimiento_horizontal(self):
        self.assertTrue(self.reina_prueba_blanca.horizontal_movimiento(0,1, 0,4))
        self.assertTrue(self.reina_prueba_blanca.horizontal_movimiento(6,4, 7,4))
        self.assertFalse(self.reina_prueba_negra.horizontal_movimiento(1,1, 0,4))

    def test_movimiento_vertical(self):
        self.assertTrue(self.reina_prueba_negra.diagonal_movimiento(4,4, 0,0))
        self.assertTrue(self.reina_prueba_negra.diagonal_movimiento(4,4, 2,6))
        self.assertTrue(self.reina_prueba_negra.diagonal_movimiento(4,4, 7,1))
        self.assertTrue(self.reina_prueba_negra.diagonal_movimiento(4,4, 7,7))

        

if __name__ == '__main__':
    unittest.main()