from game.piezas import Piezas

class Reina(Piezas):
    def __init__(self, COLOR: str) -> None:
        super().__init__(COLOR)
        self.white_str = '♛'
        self.black_str = '♕'

    def horizontal_movimiento(self,desde_fila:str,desde_col:str,
                   hasta_fila:str,hasta_col:str)->bool:
                if (desde_fila == hasta_fila) and (desde_col != hasta_col):
                    return True # Significa que se movió horizontalmente

                if (desde_fila != hasta_fila) and (desde_col == hasta_col):
                    return True
                else:
                    return False

    def diagonal_movimiento(self,desde_fila:str,desde_col:str,
                   hasta_fila:str,hasta_col:str):
        filaiteradora = desde_fila
        columnaiteradora = desde_col
            #colum_izq = desde_col
            #colum_dere = desde_col
        if desde_fila > hasta_fila:
                multip = -1
        if desde_fila < hasta_fila:
                multip = 1
                
        if desde_col < hasta_col:
                multip_lat = 1
        if desde_col > hasta_col:
                multip_lat = -1

        while 0 <= filaiteradora <= 7:
                filaiteradora += multip * 1
                columnaiteradora += multip_lat * 1
                if filaiteradora == hasta_fila:
                    if columnaiteradora == hasta_col:
                        return True
                    else: return False  


    def movimiento(self,desde_fila:str,desde_col:str,
                   hasta_fila:str,hasta_col:str):
        if self.horizontal_movimiento(desde_fila,desde_col,hasta_fila,hasta_col): 
              return True
        
        if self.diagonal_movimiento(desde_fila,desde_col,hasta_fila,hasta_col):
              return True
        else:
              return False
        
        
        
        
        
        
