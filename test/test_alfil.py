from game.alfil import Alfil
import unittest

class Test_Alfil(unittest.TestCase):
    def setUp(self) -> None:
        self.alfilblanco = Alfil('WHITE',(7,2))
        self.alfilnegro = Alfil('BLACK',(0,2))

    def test_init(self):
        self.assertTrue(self.alfilnegro.semueveenblancos)
        self.assertFalse(self.alfilblanco.semueveenblancos)

    def test_movimiento_válido(self):
        pass



if __name__ == '__main__':
    unittest.main()