from game.piezas import Piezas


class Peon(Piezas):
    def __init__(self, COLOR) -> None:
        super().__init__(COLOR)
    def atacar(self,
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int) -> bool :
        """ Método usado para verificar si el peón 
        puede atacar diagonalmente
        Parametros
        --------

        Parámetros descriptos en 
        el método movimiento(), que llama a este método

            desde_fila,desde_col,hasta_fila,hasta_col

        
        """
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
        """Devuelve True si es valido, Levanta una excepción 
        si no es válido"""


            