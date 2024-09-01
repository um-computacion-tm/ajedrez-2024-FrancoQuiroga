from game.tablero import (Tablero)
from game.torre import Torre
from game.excepciones import (NoPuedeatacar, MovimientoErróneo,
                               HayfichaAliada,MovimSaltaFicha, 
                               NoexisteFicha, FueraDelTablero)
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
    
    def test_posicion_caballos_blancos(self):
        self.assertEqual(self.tablerodeprueba.__posiciones__[7][1].decircolor, 'WHITE')
        self.assertEqual(self.tablerodeprueba.__posiciones__[7][6].decircolor, 'WHITE')

    def test_obtn_pieza(self):
        self.assertIsInstance(self.tablerodeprueba.obtn_pieza(0,7),Torre)
        self.assertEqual(self.tablerodeprueba.obtn_pieza(4,4),None)

    def test_validar_movimiento(self):
        self.assertTrue(self.tablerodeprueba.val_pieza_existe(0,1, 0,2))
        with self.assertRaises(NoexisteFicha):
            self.tablerodeprueba.val_pieza_existe(4,4, 0,2)

    def test_validar_adentro_tablero(self):
        self.assertTrue(self.tablerodeprueba.val_adentro_tablero(0,4, 0,5))
        with self.assertRaises(FueraDelTablero):
            self.tablerodeprueba.val_adentro_tablero(0,4, 0,15)
        with self.assertRaises(MovimientoErróneo):
            self.tablerodeprueba.val_adentro_tablero(15,0, 0,5)
    
    def val_movimiento_piezas(self):
        pass
if __name__ == '__main__':
    unittest.main()