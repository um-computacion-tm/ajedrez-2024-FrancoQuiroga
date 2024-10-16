from game.torre import Torre
from game.caballo import Caballo
from game.alfil import Alfil
from game.peon import Peon
from game.reina import Reina
from game.rey import Rey
from game.excepciones import (NoPuedeatacar, MovimientoErróneo,
                        HayfichaAliada,MovimSaltaFicha,
                        NoexisteFicha, FueraDelTablero,FichaAjena)


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
        for i in range(0,8):
            self.__posiciones__[1][i] = Peon('BLACK')


# Hardcode de las posiciones de las fichas blancas
        self.__posiciones__[7][0] = Torre('WHITE')
        self.__posiciones__[7][1] = Caballo('WHITE')
        self.__posiciones__[7][2] = Alfil('WHITE')
        self.__posiciones__[7][3] = Rey('WHITE')
        self.__posiciones__[7][4] = Reina('WHITE')
        self.__posiciones__[7][5] = Alfil('WHITE')
        self.__posiciones__[7][6] = Caballo('WHITE')
        self.__posiciones__[7][7] = Torre('WHITE')
        for i in range(0,8):
                    self.__posiciones__[6][i] = Peon('WHITE')
    
    def obtn_pieza(self,fila,columna): #retorna un objeto o none
        return self.__posiciones__[fila][columna]

    def val_pieza_existe(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        if self.__posiciones__[desde_fila][desde_col] is None:
            raise NoexisteFicha('ERROR: No hay ninguna ficha en la posicion inicial')
        else:
            return True
        
    def val_adentro_tablero(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        if  (desde_fila or desde_col) > 7:
            raise FueraDelTablero('ERROR: La posicion Inicial está fuera del tablero')
        if  (hasta_fila or hasta_col) > 7:
            raise FueraDelTablero('ERROR: La posicion Final está fuera del tablero')
        
        if 0 > (hasta_fila or hasta_col):
            raise FueraDelTablero('ERROR: La posicion Final está fuera del tablero')
        if 0 > (desde_fila or desde_col):
            raise FueraDelTablero('ERROR: La posicion Inicial está fuera del tablero')
        else: return True

    def val_mov_pieza(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        if self.__posiciones__[desde_fila][desde_col].movimiento(desde_fila,desde_col,
            hasta_fila, hasta_col):
            return True
        else: 
            raise MovimientoErróneo(f'ERROR: La ficha{self.__posiciones__[desde_fila][desde_col].__str__} no puede hacer ese movimiento')

    def val_nosaltarpiezas(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        
        
        ### Sección que verifica si es un caballo la ficha inicial o no
        
        if  isinstance(self.__posiciones__[desde_fila][desde_col],Caballo):
            return True
        
        ###
        
        filaiteradora = desde_fila
        columnaiteradora = desde_col
        multip = 1
        multip_lat = 1
        if desde_fila > hasta_fila:
                multip = -1
        if desde_col > hasta_col:
                multip_lat = -1

        if desde_fila == hasta_fila:
            multip = 0
        if desde_col == hasta_col:
            multip_lat = 0

        # Todo esto navega exclusivamente en diagonal
        # Necesitaría un if (o una función distinta, si la complejidad lo permite),
        #para verificar si el movimiento es horizontal/Vertical(y se ejecuta un código más sencillo)
        #o para verificar si el movimiento es diagonal
        while (filaiteradora != (hasta_fila)) or (columnaiteradora != (hasta_col)):
            filaiteradora += multip * 1
            columnaiteradora += multip_lat * 1
            if (filaiteradora == hasta_fila) and (columnaiteradora == hasta_col):
                return True
            
            try:
                if self.__posiciones__[filaiteradora][columnaiteradora] is not None:
                    raise MovimSaltaFicha('ERROR: Este movimiento hace que la ficha salte a otra ficha')
                
            except AttributeError:
                continue
        
        else: return True 
                
        



    def pieza_aliada(self,desde_fila,desde_col,hasta_fila,hasta_col):
        try:
            colorpiezainicial = self.__posiciones__[desde_fila][desde_col].decircolor
            colorpiezafinal = self.__posiciones__[hasta_fila][hasta_col].decircolor
        except AttributeError:
            colorpiezafinal = None
        
        if colorpiezafinal == None:
            return True
        if colorpiezainicial == colorpiezafinal:
            raise HayfichaAliada('ERROR: En la posicion final, hay una ficha del mismo color que el tuyo')
        if colorpiezainicial != colorpiezafinal:
            return True
        
    def val_mov_inicial(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        if desde_fila == hasta_fila:
            if desde_col == hasta_col:
                raise MovimientoErróneo('ERROR: La posicion inicial elegida es la misma que la posicion final')
            else:
                return True
        else: return True

    def validar_atq_peon(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int)-> bool:
        if isinstance(self.__posiciones__[desde_fila][desde_col], Peon):

            if self.__posiciones__[desde_fila][desde_col].atacar(desde_fila,
            desde_col,hasta_fila,hasta_col):
                try:
                    if self.__posiciones__[desde_fila][desde_col].decircolor != \
                        self.__posiciones__[hasta_fila][hasta_col].decircolor:
                        return True
                    else: raise NoPuedeatacar('ERROR: El peon elegido no puede atacar en esa direccion')
                except AttributeError:
                    raise NoPuedeatacar('ERROR: El peon no puede atacar en esa direccion, porque no hay ninguna ficha para capturar')
            else: return True
    def capturar_pieza(self,desde_fila,desde_col, hasta_fila, hasta_col):
        
        ficha_capturada = self.__posiciones__[hasta_fila][hasta_col]
        self.__posiciones__[hasta_fila][hasta_col] = self.__posiciones__[desde_fila][desde_col]
        self.__posiciones__[desde_fila][desde_col] = None
        return ficha_capturada

    def verificar_jugador(self,desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int,color_jugador):
        if self.__posiciones__[desde_fila][desde_col].decircolor == color_jugador:
            return True
        else:
            raise FichaAjena('ERROR: Estás intentando mover una ficha del otro color >:C')

    def val_movimiento(self, desde_fila: int,desde_col:int, 
                       hasta_fila:int,hasta_col:int,color_player:str)-> bool:
        """Método usado por clase Ajedrez
        
        Combina todas las posibles verificaciones que hay que 
        realizar para un funcionamiento normal de ajedrez
        (Este método no hace chequeos de checkmate[WIP?])
        
        Parámetros:
        desde_(fila/col): entero, entre 0 y 7, posición de origen delm movimiento

        hasta_(fila/col): entero, entre 0 y 7, posición final del movimiento

        color_player: string, tiene que ser exclusivamente o 'WHITE' o 'BLACK' 
        """
        # Validaciones a realizar:
        
        lista_validaciones = [self.val_mov_inicial(desde_fila,desde_col,hasta_fila,hasta_col),
             self.val_adentro_tablero(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.val_pieza_existe(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.verificar_jugador(desde_fila,desde_col,hasta_fila,hasta_col,color_player),
                            self.pieza_aliada(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.val_mov_pieza(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.val_nosaltarpiezas(desde_fila,desde_col,hasta_fila,hasta_col),
                            self.validar_atq_peon(desde_fila,desde_col,hasta_fila,hasta_col),]
        return True
        
        
        
        
        
        # Verificar si el jugador correcto 
        # puede mover la ficha correcta
        # -----Si es un caballo ignorar la validacion de saltar las fichas
        # -----Validar si un peon se mueve diagonalmente,
        # -----que exite una ficha que ese peon pueda capturar
        
        # -----0ero: Que el movimiento inicial no sea el mismo que el final
        # -----1ero: Que la posición que se elige tenga una pieza.    
        # -----2do: Que el movimiento no se salga del tablero.
        # -----3ro: Que la pieza pueda hacer ese movimiento.
        # -----4to: Que la pieza no tenga piezas entre la pos_inicial
        #------ y la posición final.
        #------ 5to: Que el movimiento final no tenga una pieza del mismo color
        