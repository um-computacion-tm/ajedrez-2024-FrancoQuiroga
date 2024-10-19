from game.piezas import Piezas




class Alfil(Piezas):
    def __init__(self, COLOR: str, ):
        super().__init__(COLOR)
        self.white_str = '♝'
        self.black_str = '♗'


    def movimiento(self,desde_fila:str,desde_col:str,
                   hasta_fila:str,hasta_col:str) ->True:
        
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


