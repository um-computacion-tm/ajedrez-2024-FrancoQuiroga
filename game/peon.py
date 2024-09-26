from game.piezas import Piezas
from game.excepciones import (MovimientoErróneo, NoPuedeatacar)


class Peon(Piezas):
    def __init__(self, COLOR) -> None:
        super().__init__(COLOR)
        self.white_str = '♟'
        self.black_str = '♙'
    def atacar(self,
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int) -> bool :
        """ Método usado para verificar si el peón 
        puede atacar diagonalmente
        Solo lo puede usar el tablero, ya que esta clase
        no conoce el estado del tablero, por lo que no
        puede verificar si hay una ficha en la diagonal 
        que ataca.
        
        Parametros
        --------

        Parámetros descriptos en 
        el método movimiento(), que llama a este método

            desde_fila,desde_col,hasta_fila,hasta_col

        
        NO USAR ESTA FUNCIÓN FUERA DE LA CLASE PEÓN
        PARA VERIFICAR EL MOVIMIENTO, SOLO USAR LA FUNCION:
        peon.movimiento()
        
        """
        
        if (desde_fila+1 == hasta_fila)\
            and (self.__color__ == 'BLACK'):

            if (desde_col+1 == hasta_col) or\
            (desde_col-1 == hasta_col):
                return True
        
        if (desde_fila-1 == hasta_fila) and \
            (self.__color__ == 'WHITE'):

            if (desde_col-1 == hasta_col) or \
                (desde_col+1 == hasta_col):

                return True
        
        else: return False

    def movimientoinicial(self,
        
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int) -> bool :
        """Método usado para verificar si el peón está en su posición
        inicial, lo que le permite moverse 2 espacios
        Parametros
        --------
        desde_fila,desde_col,hasta_fila,hasta_col

        Parámetros descriptos en 
        el método movimiento() que llama a este método
                
        NO USAR ESTA FUNCIÓN FUERA DE LA CLASE PEÓN
        PARA VERIFICAR EL MOVIMIENTO, SOLO USAR LA FUNCION:
        peon.movimiento()
        
        """
        if (desde_fila == 1) and (self.__color__ == 'BLACK'):
            if (hasta_fila == 2) or (hasta_fila == 3):
                return True
            
        if (desde_fila == 6) and (self.__color__ == 'WHITE'):
            if (hasta_fila == 4):
                return True
        #(hasta_fila == 5) or 
        else: return False
    def movimientonormal(self,
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int) -> bool :   
        """Movimiento de un peon, en línea recta y uno hacia delante
        
        NO USAR ESTA FUNCIÓN FUERA DE LA CLASE PEÓN
        PARA VERIFICAR EL MOVIMIENTO, SOLO USAR LA FUNCION:
        peon.movimiento()
        """
         
        if (self.__color__ == 'WHITE') and desde_fila-1 == hasta_fila:
                    if desde_col == hasta_col :
                        return True
        if self.__color__ == 'BLACK' and desde_fila+1 == hasta_fila:
                    if desde_col == hasta_col:
                        return True
        else:
             return False
        
    def movimiento(self,
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int) -> bool :
        """Devuelve True si es valido, Devuelve False 
        si no es válido
        Los parámetros son las posiciones que eligió el usuario
        para mover una pieza, es importante llamar a la función con
        los parámetros que el usuario eligió, para verificar
        correctamente el movimientos"""
        if self.movimientonormal(desde_fila,desde_col,
                                 hasta_fila,hasta_col):
             return True
        if self.movimientoinicial(desde_fila,desde_col,
                                 hasta_fila,hasta_col):
             return True
        #if self.atacar(desde_fila,desde_col,
        #                         hasta_fila,hasta_col):
        #     return True
        else: return False
             

            