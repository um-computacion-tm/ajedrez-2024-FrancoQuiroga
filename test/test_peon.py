from game.peon import Peon
import unittest
class Test_inicial_Peon(unittest.TestCase):
    def setUp(self) -> None:
        self.peon_pruebablanco = Peon('WHITE')
        self.peon_pruebanegro = Peon('BLACK')

    def test_initpeon(self):
        pass

if __name__ == '__main__':
    unittest.main()