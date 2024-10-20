import unittest
from game.excepciones import(TerminaJuego)
from game.main import (main,play,mostrar_fichas_capturadas,
                       mostrar_tablero,turno_actual,verificar_ganador,
                         moverpieza,tomar_input, play)
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
    @patch('builtins.print')
    def test_mostrar_tablero(self,patch_print):
        mostrar_tablero(self.ajedrez_prueba)
        self.assertEqual(patch_print.call_count, 82)

    @patch('builtins.print')
    def test_mover_pieza(self,patch_print):
        self.ajedrez_prueba.__turno__ = 'BLACK'
        moverpieza(self.ajedrez_prueba,1,1,2,1)
        self.assertEqual(patch_print.call_count, 1)
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1','A','q'])
    def test_tomar_input_salida1(self,patch_input,patch_print):
        with self.assertRaises(TerminaJuego):
            tomar_input()
        self.assertEqual(patch_print.call_count,1)
        self.assertEqual(patch_input.call_count,3)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1','A','2','B'])
    def test_tomar_input_completo(self,patch_input,patch_print):
        lista_salida = tomar_input()
        self.assertEqual(len(lista_salida),4)
        self.assertEqual(lista_salida,('1','A','2','B'))
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['q'])
    def test_tomar_input_salida2(self,patch_input,print):    
        with self.assertRaises(TerminaJuego):
            tomar_input()
        self.assertEqual(patch_input.call_count,1)
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1','Q'])
    def test_tomar_input_salida3(self,patch_input,pri):      
        with self.assertRaises(TerminaJuego):
            tomar_input()
        self.assertEqual(patch_input.call_count,2)
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1','1','1','q'])
    def test_tomar_input_salida4(self,patch_input,print):    
        with self.assertRaises(TerminaJuego):
            tomar_input()
        self.assertEqual(patch_input.call_count,4)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1','A','2','B','q'])
    def test_play(self,inputs,outpust):
        play(self.ajedrez_prueba)
        self.assertEqual(inputs.call_count, 5)
        

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