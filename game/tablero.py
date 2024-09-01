from game.torre import Torre
from game.caballo import Caballo
from game.alfil import Alfil
from game.peon import Peon
from game.reina import Reina
from game.rey import Rey
from game.excepciones import (NoPuedeatacar, MovimientoErróneo,
                        HayfichaAliada,MovimSaltaFicha,
                        NoexisteFicha, FueraDelTablero)

class Tablero:
    def __init__(self) -> None:
        self.__posiciones__ = []
        for _ in range(8):
            col = []
            for _ in range (8):
                col.append(None)
            self.__posiciones__.append(col)
# Hardcode de las posciones de las fichas negras
        self.__posiciones__[0][0] = Torre('BLACK')
        self.__posiciones__[0][1] = Caballo('BLACK')
        self.__posiciones__[0][2] = Alfil('BLACK')
        self.__posiciones__[0][3] = Rey('BLACK')
        self.__posiciones__[0][4] = Reina('BLACK')
        self.__posiciones__[0][5] = Alfil('BLACK')
        self.__posiciones__[0][6] = Caballo('BLACK')
        self.__posiciones__[0][7] = Torre('BLACK')


# Hardcode de las posiciones de las fichas blancas
        self.__posiciones__[7][0] = Torre('WHITE')
        self.__posiciones__[7][1] = Caballo('WHITE')
        self.__posiciones__[7][2] = Alfil('WHITE')
        self.__posiciones__[7][3] = Rey('WHITE')
        self.__posiciones__[7][4] = Reina('WHITE')
        self.__posiciones__[7][5] = Alfil('WHITE')
        self.__posiciones__[7][6] = Caballo('WHITE')
        self.__posiciones__[7][7] = Torre('WHITE')

    def obtn_pieza(self,fila,columna): #retorna un objeto o none
        return self.__posiciones__[fila][columna]

    def val_pieza_existe(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        if self.__posiciones__[desde_fila][desde_col] is None:
            raise NoexisteFicha
        else:
            return True
        
    def val_adentro_tablero(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        if 0< desde_fila or desde_col >= 8:
            raise MovimientoErróneo
        if hasta_fila or hasta_col >= 8:
            raise FueraDelTablero
        else: return True
    def val_mov_pieza(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        pass
    def val_nosaltarpiezas(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        pass
    def pieza_alidada(desde_fila,desde_col,hasta_fila,hasta_col):
        pass
    def val_movimiento(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        # Validaciones a realizar:
        esvalido = False
        lista_validaciones = [self.val_adentro_tablero(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.val_pieza_existe(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.val_mov_pieza(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.val_nosaltarpiezas(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.pieza_alidada(desde_fila,desde_col,hasta_fila,hasta_col)]
        for validacion in lista_validaciones:
            esvalido = validacion
            if esvalido == False:
                return False
            else:
                esvalido = True
        # 1ero: Que la posición que se elige tenga una pieza.    
        # 2do: Que el movimiento no se salga del tablero.
        # 3ro: Que la pieza pueda hacer ese movimiento.
        # 4to: Que la pieza no tenga piezas entre la pos_inicial
        # y la posición final.
        # 5to: Que el movimiento final no tenga una pieza del mismo color
        