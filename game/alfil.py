from game.piezas import Piezas




class Alfil(Piezas):
    def __init__(self, COLOR: str, posicion_inicial:tuple):
        super().__init__(COLOR)
        self.posicion_inicial = posicion_inicial
        self.semueveenblancos = False
        if (posicion_inicial[0]-posicion_inicial[1])%2 == 0:
            self.semueveenblancos = True

    def movimiento(self,desde_fila:str,desde_col:str,
                   hasta_fila:str,hasta_col:str) ->True:
        
        pass