from game.alfil import Alfil
import unittest

class Test_Alfil(unittest.TestCase):
    def setUp(self) -> None:
        self.alfilblanco = Alfil('WHITE',(7,2))
        self.alfilnegro = Alfil('BLACK',(0,2))

    def test_init(self):
        self.assertTrue(self.alfilnegro.semueveenblancos)
        self.assertFalse(self.alfilblanco.semueveenblancos)

    def test_movimiento_válido_negro(self):
        self.assertTrue(self.alfilnegro.movimiento(4,4, 0,0))
        self.assertTrue(self.alfilnegro.movimiento(4,4, 2,6))
        self.assertTrue(self.alfilnegro.movimiento(4,4, 7,1))
        self.assertTrue(self.alfilnegro.movimiento(4,4, 7,7))

    def test_movimiento_válido_blanco(self):
        self.assertTrue(self.alfilblanco.movimiento(4,1, 7,4))
        self.assertTrue(self.alfilblanco.movimiento(4,1, 5,0))
        self.assertTrue(self.alfilblanco.movimiento(4,1, 3,0))
        self.assertTrue(self.alfilblanco.movimiento(4,1, 1,4))
    def test_movimiento_inválido_blanco(self):
            self.assertFalse(self.alfilblanco.movimiento(4,1, 6,4))
            self.assertFalse(self.alfilblanco.movimiento(4,1, 6,2))
    
if __name__ == '__main__':
    unittest.main()