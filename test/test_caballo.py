import unittest
from game.caballo import Caballo

class TestMovimientoCaballo(unittest.TestCase):

    def setUp(self) -> None:
        self.caballopruebablanco = Caballo('WHITE')
        self.caballopruebanegro = Caballo('BLACK')

    def test_movimientocorrect(self):
# Posicion inicial del caballo: Fila = 0, Columna = 1
        self.assertTrue(self.caballopruebanegro.movimiento(0,1, 2,2))
        self.assertTrue(self.caballopruebanegro.movimiento(0,1, 2,0))

# Posicion inicial del caballo: Fila = 7, Columna = 1
        self.assertTrue(self.caballopruebablanco.movimiento(7,1, 5,0))
        self.assertTrue(self.caballopruebablanco.movimiento(7,1, 5,2))

        self.assertTrue(self.caballopruebablanco.movimiento(4,4, 3,6))

    def test_movimientoincorrect(self):
        self.assertFalse(self.caballopruebablanco.movimiento(4,4, 1,4))
        self.assertFalse(self.caballopruebanegro.movimiento(4,4, 5,3))

if __name__ == '__main__':  
    unittest.main()