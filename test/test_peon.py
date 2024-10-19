from game.peon import Peon
from game.excepciones import MovimientoErróneo
import unittest
class Test_inicial_Peon(unittest.TestCase):
    def setUp(self) -> None:
        self.peon_prueba_blanco = Peon('WHITE')
        self.peon_prueba_negronegro = Peon('BLACK')

    def test_ataquepeon(self):
        self.assertTrue(self.peon_prueba_blanco.atacar(4,4, 3,5))
        self.assertTrue(self.peon_prueba_blanco.atacar(4,4, 3,3))

        self.assertTrue(self.peon_prueba_negronegro.atacar(4,4, 5,3))
        self.assertTrue(self.peon_prueba_negronegro.atacar(4,4, 5,5))
        self.assertFalse(self.peon_prueba_blanco.atacar(4,4, 4,2))


class Test_movimiento_Peon(unittest.TestCase):
    def setUp(self) -> None:
        self.peon_prueba_blanco = Peon('WHITE')
        self.peon_prueba_negro = Peon('BLACK')

    def test_movim_posicion_inicial_blancoynegro(self):
        #test que permite 
        # que el peon se mueva 1 o 2 posiciones 
        # en su primer turno
        self.assertTrue(self.peon_prueba_negro.movimientoinicial(1,0, 2,0))
        self.assertTrue(self.peon_prueba_negro.movimientoinicial(1,0, 3,0))

        self.assertTrue(self.peon_prueba_blanco.movimientoinicial(6,0, 4,0))
    
    def test_movi_posicion_inicial_novalida_blancoynegro(self):
        #import ipdb
        #ipdb.set_trace()
        self.assertFalse(self.peon_prueba_blanco.movimientoinicial(6,0, 2,0))
        self.assertFalse(self.peon_prueba_negro.movimientoinicial(1,0, 4,0))
        self.assertFalse(self.peon_prueba_blanco.movimientoinicial(5,0, 3,0))
        

    def test_movim_normal_peon_blanco_val(self):

        self.assertTrue(self.peon_prueba_blanco.movimientonormal(4,2,3,2))
        self.assertTrue(self.peon_prueba_negro.movimientonormal(4,4, 5,4))

        self.assertFalse(self.peon_prueba_blanco.movimientonormal(4,4, 6,4))

        
    def test_movimiento(self):
        
        self.assertTrue(self.peon_prueba_negro.movimiento(5,5, 6,5))
        self.assertTrue(self.peon_prueba_blanco.movimiento(6,6, 4,6))
        #self.assertTrue(self.peon_prueba_blanco.movimiento(3,2, 2,1))

        self.assertFalse(self.peon_prueba_negro.movimiento(6,6, 4,5))
        self.assertTrue(self.peon_prueba_negro.movimiento(4,4,5,3))
        self.assertTrue(self.peon_prueba_negro.movimiento(1,0,2,1))
        
if __name__ == '__main__':
    unittest.main()