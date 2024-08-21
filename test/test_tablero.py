from game.tablero import (Tablero)
from game.torre import Torre
import unittest

class Test_Tablero_setup(unittest.TestCase):
    def setUp(self) -> None:
        self.tablerodeprueba = Tablero()
    
    def test_inicial(self):
        self.assertIsInstance(self.tablerodeprueba.__posiciones__, list) #Verifica que el elemento posiciones sea una lista
        self.assertEqual(self.tablerodeprueba.__posiciones__[5][5], None)

    def test_posicion_torres_negras(self):
        self.assertEqual(self.tablerodeprueba.__posiciones__[0][0].decircolor,'BLACK')
        self.assertEqual(self.tablerodeprueba.__posiciones__[0][7].decircolor,'BLACK')
    def test_posicion_torres_blancas(self):
        self.assertEqual(self.tablerodeprueba.__posiciones__[7][0].decircolor,'WHITE')
        self.assertEqual(self.tablerodeprueba.__posiciones__[7][7].decircolor,'WHITE')

    def test_obtn_pieza(self):
        self.assertIsInstance(self.tablerodeprueba.obtn_pieza(0,7),Torre)
        self.assertEqual(self.tablerodeprueba.obtn_pieza(0,5),None)



if __name__ == '__main__':
    unittest.main()