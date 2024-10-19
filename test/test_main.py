import unittest
from game.main import (main,play,mostrar_fichas_capturadas,
                       mostrar_tablero,turno_actual,verificar_ganador)
from unittest.mock import patch,call
from game.ajedrez import Ajedrez

class Test_funcionesadyacentes(unittest.TestCase):
    def setUp(self):
        self.ajedrez_prueba = Ajedrez()
    @patch('builtins.print')
    
    
    def test_fichas_capturadas_cero(self,print_mockeado):
        mostrar_fichas_capturadas(self.ajedrez_prueba)
        self.assertEqual(print_mockeado.call_count, 2)
    @patch('builtins.print')
    def test_fichas_capturadas1_blanca(self,print_mockeado):
        self.ajedrez_prueba.__listacapturadasporblanco__.append('AA')
        mostrar_fichas_capturadas(self.ajedrez_prueba)
        self.assertEqual(print_mockeado.call_count, 3)
    @patch('builtins.print')
    def test_fichas_capturadas1_negra(self,print_mockeado):
        self.ajedrez_prueba.__listacapturadaspornegro__.append('AA')
        mostrar_fichas_capturadas(self.ajedrez_prueba)
        self.assertEqual(print_mockeado.call_count, 3)
    @patch('builtins.print')
    def test_fichas_capturadas2y2nyb(self,print_mock):
        self.ajedrez_prueba.__listacapturadaspornegro__.append('AA')
        self.ajedrez_prueba.__listacapturadaspornegro__.append('BB')

        self.ajedrez_prueba.__listacapturadasporblanco__.append('AA')
        self.ajedrez_prueba.__listacapturadasporblanco__.append('CC')
        mostrar_fichas_capturadas(self.ajedrez_prueba)
        self.assertEqual(print_mock.call_count, 6)

    @patch('builtins.print')
    def test_turno_actual(self,print):
        self.assertEqual('WHITE',turno_actual(self.ajedrez_prueba))
    
    def test_verificar_ganador_blanco(self):
        for i in range(16):
            self.ajedrez_prueba.__listacapturadasporblanco__.append('AA')
        
        self.assertTrue(verificar_ganador(self.ajedrez_prueba))

    def test_verificar_ganador_negro(self):
        for i in range(16):
            self.ajedrez_prueba.__listacapturadaspornegro__.append('AA')
        self.assertFalse(verificar_ganador(self.ajedrez_prueba))

    
#class Test_funcion_play(unittest.TestCase):
#    def setUp(self) -> None:
#        self.ajedrezprueba = Ajedrez()
#    #def setUp(self) -> None:
#    #    self.juegoprueba = main()
#    #    self.funcionplayp = play()
#    @patch('builtins.input', side_effect=['0','1','t','0'])
#    @patch('builtins.print')
#    @patch('game.main.exit')
#    
#    def test_funcion_play_cierraenhastafila(self,mock_exit,mock_print, mock_input):
#        play(self.ajedrezprueba)
#        ordenllamadas = [call('Tablero Actual: '),call('Elija la Fila y Columna de la ficha que quiere mover'),
#                         call('Ingrese la fila: '),call('Ingrese la columna: '),
#                         call('Elija la posicion a donde mover la ficha'),
#                         call('Ingrese la fila objetivo: '),call('Ingrese la columna objetivo: ')]
#        mock_exit.assert_called_once_with('Cerrando el programa')
#        self.assertEqual(mock_input.call_count, 4)
#        mock_print.assert_has_calls(ordenllamadas,any_order=False)
        



if __name__ == '__main__':
    unittest.main()