from game.piezas import Piezas
class Torre(Piezas):
    def __init__(self, COLOR) -> None:
        super().__init__(COLOR)

    def movimiento(self,desde_fila:str,desde_col:str,
                   hasta_fila:str,hasta_col:str)->bool:
        if (desde_fila == hasta_fila) and (desde_col != hasta_col):
            return True # Significa que se movió horizontalmente
        
        if (desde_fila != hasta_fila) and (desde_col == hasta_col):
            return True
        else:
            return False
        