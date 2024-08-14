from torre import Torre
import unittest

class Test_setup_torre(unittest.TestCase): # Testea el setup de Pieza y la funcion 
    def setUp(self) -> None:
        self.torredeprueba_negra = Torre('BLACK')
        self.torredeprueba_blanca = Torre('WHITE')
    def test_torrenegra(self):
        

if __name__ == '__main__':
    unittest.main()