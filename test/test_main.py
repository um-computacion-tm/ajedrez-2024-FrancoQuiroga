import unittest
from game.main import (main,play)
from unittest.mock import patch
from game.ajedrez import Ajedrez

#class Test_funcion_play(unittest.TestCase):
#    def setUp(self) -> None:
#        self.ajedrezprueba = Ajedrez()
#    #def setUp(self) -> None:
#    #    self.juegoprueba = main()
#    #    self.funcionplayp = play()
#    @patch('builtins.input', return_value=['1','1','0','0'])
#    @patch('builtins.print')
#    def test_funcion_play(self,mock_print, mock_input):
#        play(self.ajedrezprueba )
#        mock_print.assert_called_once_with('Tablero Actual: ')



if __name__ == '__main__':
    unittest.main()