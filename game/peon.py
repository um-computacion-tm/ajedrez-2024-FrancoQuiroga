from game.piezas import Piezas


class Peon(Piezas):
    def __init__(self, COLOR) -> None:
        super().__init__(COLOR)
        
    def movimiento(self,desde_fila,desde_col,hasta_fila,hasta_col):
        # Movimientos en posicion inicial
        if (desde_fila == 1) and (self.__color__ == 'BLACK'):
            if (hasta_fila == 2) or (hasta_fila == 3):
                return True
            
        if (desde_fila == 6) and (self.__color__ == 'WHITE'):
            if (hasta_fila == 5) or (hasta_fila == 4):
                return True
        else:
            return False

            