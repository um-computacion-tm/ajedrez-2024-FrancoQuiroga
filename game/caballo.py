from game.piezas import Piezas

class Caballo(Piezas):
    def __init__(self, COLOR: str) -> None:
        super().__init__(COLOR)
        self.white_str = '♞'
        self.black_str = '♘'

    def movimiento(self,
                   desde_fila: int,desde_col: int
                   ,hasta_fila:int,hasta_col:int):
        """ Verifica si el movimiento que recibe el caballo
        es posible de ser realizado por la pieza.
        """

        MOVIMIENTOLATERAL = (1,2)
        MOVIMIENTOVERTICAL = (2,1)
        
        vectormovimiento= (abs(desde_fila-hasta_fila),
                           abs(desde_col-hasta_col))
        
        if vectormovimiento == MOVIMIENTOLATERAL:
            return True
        if vectormovimiento == MOVIMIENTOVERTICAL:
            return True
        else: 
            return False
        