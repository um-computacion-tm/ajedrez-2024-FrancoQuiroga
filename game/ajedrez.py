from game.tablero import Tablero
from game.excepciones import(MovimientoErróneo,MovimSaltaFicha,
                             NoexisteFicha,NoPuedeatacar,FueraDelTablero,HayfichaAliada)
class Ajedrez:
    def __init__(self,) -> None:
        """Inicializa una instancia de la clase Tablero,
        El turno inicial son la blancas"""
        self.__tablero__ = Tablero()
        self.__turno__ = 'WHITE'

    def mover(self, desde_fila,desde_col,hasta_fila,hasta_col):
        #Utiliza los inputs de los usuarios y los usa en tablero
        #Maneja los outputs del tablero y le da una imagen al tablero
        try:
            self.__tablero__.val_movimiento(desde_fila,desde_col,
                                            hasta_fila,hasta_col)
        except NoPuedeatacar:
            return NoPuedeatacar
        
        except FueraDelTablero:
            return FueraDelTablero
        
        except NoexisteFicha:
            return NoexisteFicha
        
        except HayfichaAliada:
            return HayfichaAliada
        
        except MovimientoErróneo:
            return MovimientoErróneo

        except MovimSaltaFicha:
            return MovimSaltaFicha


