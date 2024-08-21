from game.peon import Peon
from game.excepciones import MovimientoErróneo
import unittest
class Test_inicial_Peon(unittest.TestCase):
    def setUp(self) -> None:
        self.peon_prueba_negroblanco = Peon('WHITE')
        self.peon_prueba_negronegro = Peon('BLACK')

    def test_initpeon(self):
        pass


class Test_movimiento_Peon(unittest.TestCase):
    def setUp(self) -> None:
        self.peon_prueba_blanco = Peon('WHITE')
        self.peon_prueba_negro = Peon('BLACK')

    def test_movim_posicion_inicial_blancoynegro(self):
        #test que permite 
        # que el peon se mueva 1 o 2 posiciones 
        # en su primer turno
        self.assertTrue(self.peon_prueba_negro.movimiento(1,0, 2,0))
        self.assertTrue(self.peon_prueba_negro.movimiento(1,0, 3,0))

        self.assertTrue(self.peon_prueba_blanco.movimiento(6,0, 5,0))
        self.assertTrue(self.peon_prueba_blanco.movimiento(6,0, 4,0))
    
    def test_movi_posicion_inicial_novalida_blancoynegro(self):
        self.assertFalse(self.peon_prueba_blanco.movimiento(5,0, 3,0))
        self.assertFalse(self.peon_prueba_negro.movimiento(1,0, 4,0))
        self.assertFalse(self.peon_prueba_blanco.movimiento(6,0, 3,0))
        

    def test_movim_peon_blanco_val(self):

        self.assertTrue(self.peon_prueba_blanco.movimiento(4,2,5,2))
        
        
    def test_movimiento(self):
        
        pass
if __name__ == '__main__':
    unittest.main()