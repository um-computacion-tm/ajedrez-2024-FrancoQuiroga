import unittest
from game.ajedrez import Ajedrez
from unittest.mock import patch
from game.excepciones import (MovimientoErróneo,MovimSaltaFicha,
                             NoexisteFicha,NoPuedeatacar,FueraDelTablero,
                             HayfichaAliada)
class Test_inicial_Ajedrez(unittest.TestCase):
    def setUp(self) -> None:
        self.ajedrezdeprueba = Ajedrez()

    def test_init(self):
        self.assertEqual(self.ajedrezdeprueba.__turno__, 'WHITE')
        self.assertIsInstance(self.ajedrezdeprueba.__tablero__, object)

    def test_mover(self):
        
        self.ajedrezdeprueba.__turno__ = 'BLACK'
        self.assertTrue(self.ajedrezdeprueba.mover(1,1,2,1))
        
        
        self.assertTrue(self.ajedrezdeprueba.mover(6,1,4,1))
        
        with self.assertRaises(MovimSaltaFicha):
            self.ajedrezdeprueba.mover(0,0,5,0)
            self.assertEqual(len(self.ajedrezdeprueba.__listadenegrascapturadas__),0)
        self.assertEqual(len(self.ajedrezdeprueba.__listacapturadasporblanco__),0)

        self.assertEqual(len(self.ajedrezdeprueba.__listacapturadaspornegro__),0)

    def test_mover_capturapiezablanca(self):
        self.ajedrezdeprueba.__tablero__.__posiciones__[1][0] = None
        self.ajedrezdeprueba.__tablero__.__posiciones__[6][0] = None
        
        self.assertTrue(self.ajedrezdeprueba.mover(7,0, 0,0))
        
        self.ajedrezdeprueba.__tablero__.__posiciones__[7][0] = self.ajedrezdeprueba.__tablero__.__posiciones__[1][1]
        self.ajedrezdeprueba.__turno__ = 'WHITE'
        self.assertTrue(self.ajedrezdeprueba.mover(0,0, 7,0))
        # Checkea la lista de capturadas para validar el movimiento
        self.assertEqual(2,len(self.ajedrezdeprueba.__listacapturadasporblanco__))

    def test_capturarpiezanegra(self):
        self.ajedrezdeprueba.__tablero__.__posiciones__[1][0] = None
        self.ajedrezdeprueba.__tablero__.__posiciones__[6][0] = None

        self.ajedrezdeprueba.__turno__ = 'BLACK'
        self.assertTrue(self.ajedrezdeprueba.mover(0,0, 7,0))
        self.ajedrezdeprueba.__tablero__.__posiciones__[7][0] = self.ajedrezdeprueba.__tablero__.__posiciones__[1][1]
        # Checkea la lista de capturadas para validar el movimiento
        self.assertEqual(1,len(self.ajedrezdeprueba.__listacapturadaspornegro__))
    
    def test_traducir_posiciones(self):
        self.assertEqual(4,len(self.ajedrezdeprueba.traducir_posiciones(8,'A',2,'F')))
        self.assertEqual((0,0,6,5),self.ajedrezdeprueba.traducir_posiciones(8,'A',2,'F'))
        with self.assertRaises(KeyError):
            self.ajedrezdeprueba.traducir_posiciones(8,'A',2,'Z')
    @patch('builtins.print')
    def test_listablancas(self,mock_print):
        self.ajedrezdeprueba.__listacapturadasporblanco__ = ['a','b','c']
        self.ajedrezdeprueba.listar_blancas
        mock_print.assert_called()
    
    @patch('builtins.print')
    def test_listanegras(self,mock_print):
        self.ajedrezdeprueba.__listacapturadaspornegro__ = ['a','b','c']
        self.ajedrezdeprueba.listar_negras
        mock_print.assert_called()

    def test_decir_turno(self):
        self.assertEqual(self.ajedrezdeprueba.decir_turno,'WHITE')
        self.ajedrezdeprueba.__turno__ = 'BLACK'
        self.assertEqual(self.ajedrezdeprueba.decir_turno,'BLACK')

    def test_longitudlist_blanca(self):
        self.ajedrezdeprueba.__listacapturadasporblanco__ = ['a','b','c']
        self.assertEqual(3,self.ajedrezdeprueba.longitud_lista_blancas)


    def test_longitudlist_negra(self):
        self.ajedrezdeprueba.__listacapturadaspornegro__ = ['a','b','c']
        self.assertEqual(3,self.ajedrezdeprueba.longitud_lista_negras)

if __name__ == '__main__':
    unittest.main()