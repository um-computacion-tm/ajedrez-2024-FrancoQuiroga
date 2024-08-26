from game.piezas import Piezas
from game.excepciones import (MovimientoErróneo, NoPuedeatacar, Puedeatacar)


class Peon(Piezas):
    def __init__(self, COLOR) -> None:
        super().__init__(COLOR)
    def atacar(self,
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int) -> bool :
        """ Método usado para verificar si el peón 
        puede atacar diagonalmente
        Solo lo puede usar el tablero
        Parametros
        --------

        Parámetros descriptos en 
        el método movimiento(), que llama a este método

            desde_fila,desde_col,hasta_fila,hasta_col

        
        """
        if desde_col+1 == hasta_col:
            if desde_fila+1 == hasta_fila:
                return True
        
        if desde_col-1 == hasta_col:
            if desde_fila-1 == hasta_fila:
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
        

        
        """
        if (desde_fila == 1) and (self.__color__ == 'BLACK'):
            if (hasta_fila == 2) or (hasta_fila == 3):
                return True
            
        if (desde_fila == 6) and (self.__color__ == 'WHITE'):
            if (hasta_fila == 5) or (hasta_fila == 4):
                return True
        
        
        
    def movimiento(self,
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int) -> bool :
        """Devuelve True si es valido, Devuelve False 
        si no es válido
        Los parámetros son las posiciones que eligió el usuario
        para mover una pieza, es importante llamar a la función con
        los parámetros que el usuario eligió, para verificar
        correctamente el movimientos"""
        try:
            # Comprueba que el movimiento no sea incorrecto
            puedeatk = self.atacar(desde_fila,desde_col,hasta_fila,hasta_col)
            
            if puedeatk == False:
                if (self.__color__ == 'WHITE') and desde_fila-1 == hasta_fila:
                    if desde_col == hasta_col :
                        return True
                if self.__color__ == 'BLACK' and desde_fila+1 == hasta_fila:
                    if desde_col == hasta_col:
                        return True
                self.movimientoinicial(desde_fila,desde_col,hasta_fila,hasta_col)
                

            else:
                return True
        except NoPuedeatacar:
            return False
        
        except MovimientoErróneo as e:
            return False
        
        else:
            return True
        


            