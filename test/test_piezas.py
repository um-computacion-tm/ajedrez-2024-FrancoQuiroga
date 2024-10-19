from game.piezas import Piezas
import unittest

class Test_setup_pieza(unittest.TestCase): # Testea el setup de Pieza y la funcion 
    def setUp(self) -> None:
        self.piezadepruebablanco = Piezas('WHITE')
        self.piezadepruebanegro = Piezas('BLACK')
    
    def test_COLOR_blanco_setup(self):
        self.assertEqual('WHITE', self.piezadepruebablanco.__color__)
    def test_COLOR_negro_setup(self):
        self.assertEqual('BLACK', self.piezadepruebanegro.__color__)
    

    def test_decircolor_blanco(self):
        self.assertEqual('WHITE', self.piezadepruebablanco.decircolor)
    def test_decircolor_negro(self):
        self.assertEqual('BLACK', self.piezadepruebanegro.decircolor)

    def test_swap_color_intrfz(self):
        self.piezadepruebablanco.white_str = 'negro'
        self.piezadepruebablanco.black_str = 'blanco'
        self.piezadepruebablanco.swap_color_intrfz()

        self.assertEqual(self.piezadepruebablanco.white_str,'blanco')
        self.assertEqual(self.piezadepruebablanco.black_str,'negro')

if __name__ == '__main__':
    unittest.main()