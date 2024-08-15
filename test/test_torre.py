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


if __name__ == '__main__':
    unittest.main()