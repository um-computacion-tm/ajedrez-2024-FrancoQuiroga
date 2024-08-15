from game.tablero import Tablero
class Ajedrez:
    def __init__(self,) -> None:
        self.__tablero__ = Tablero()
        self.__turno__ = 'BLANCAS'

    def mover(self, desde_fila,desde_col,hasta_fila,hasta_col):
        pass