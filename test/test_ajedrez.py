import unittest
from game.ajedrez import Ajedrez

class Test_inicial_Ajedrez(unittest.TestCase):
    def setUp(self) -> None:
        self.ajedrezdeprueba = Ajedrez()

    def test_init(self):
        self.assertEqual(self.ajedrezdeprueba.__turno__, 'BLANCAS')
        self.assertIsInstance(self.ajedrezdeprueba.__tablero__, object)


if __name__ == '__main__':
    unittest.main()