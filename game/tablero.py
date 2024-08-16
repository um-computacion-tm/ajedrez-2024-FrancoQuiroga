from game.torre import Torre
class Tablero:
    def __init__(self) -> None:
        self.__posiciones__ = []
        for _ in range(8):
            col = []
            for _ in range (8):
                col.append(None)
            self.__posiciones__.append(col)

        self.__posiciones__[0][0] = Torre('BLACK')
        self.__posiciones__[0][7] = Torre('BLACK')
        self.__posiciones__[7][0] = Torre('WHITE')
        self.__posiciones__[7][7] = Torre('WHITE')

    def obtn_pieza(self,fila,columna): #retorna un objeto o none
        return self.__posiciones__[fila][columna]
