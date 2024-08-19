from game.torre import Torre
import unittest

class Test_setup_torre(unittest.TestCase): # Testea el setup de Pieza y la funcion 
    def setUp(self) -> None:
        self.torredeprueba_negra = Torre('BLACK')
        self.torredeprueba_blanca = Torre('WHITE')

    def test_torrenegra_herenciacorrecta(self):
        self.assertEqual(self.torredeprueba_negra.__color__, 'BLACK')
        self.assertEqual(self.torredeprueba_negra.decircolor(), 'BLACK')


    def test_torreblanca_herenciacorrecta(self):
        self.assertEqual(self.torredeprueba_blanca.__color__, 'WHITE')
        self.assertEqual(self.torredeprueba_blanca.decircolor(), 'WHITE')

class Test_movimiento_torre(unittest.TestCase):
    def setUp(self) -> None:
        self.torredeprueba = Torre('WHITE')
    def test_movimiento_validohor_torre(self):
        self.assertTrue(self.torredeprueba.movimiento(5,5, 5,7))
    def test_movimiento_validovert_torre(self):
        self.assertTrue(self.torredeprueba.movimiento(5,5, 7,5))
    def test_movimiento_novalido_torre(self):
        self.assertFalse(self.torredeprueba.movimiento(5,5, 6,7))

if __name__ == '__main__':
    unittest.main()