from game.tablero import Tablero
from game.excepciones import(MovimientoErróneo,MovimSaltaFicha,
                             NoexisteFicha,NoPuedeatacar,FueraDelTablero,HayfichaAliada)
class Ajedrez:
    def __init__(self,) -> None:
        """Inicializa una instancia de la clase Tablero,
        El turno inicial son la blancas"""
        self.__tablero__ = Tablero()
        self.__turno__ = 'WHITE'
        self.__listacapturadasporblanco__ = []          
        self.__listacapturadaspornegro__ = []

    def mover(self, desde_fila,desde_col,hasta_fila,hasta_col):
        #Utiliza los inputs de los usuarios y los usa en tablero
        #Maneja los outputs del tablero y le da una imagen al tablero
        try:
            self.__tablero__.val_movimiento(desde_fila,desde_col,
                                            hasta_fila,hasta_col,color_player=self.__turno__)
            #Luego de verificar el movimiento, ejecutar el movimiento
            #Añadir la pieza eliminada a una lista correspondiente
            
            if self.__turno__ == 'WHITE':
                piezacapturadablanca = self.__tablero__.capturar_pieza(desde_fila,desde_col,hasta_fila,hasta_col)
                if piezacapturadablanca != None :
                    self.__listacapturadasporblanco__.append(piezacapturadablanca)
                self.__turno__ = 'BLACK'
                return True

            if self.__turno__ == 'BLACK':
                piezacapturadanegra = self.__tablero__.capturar_pieza(desde_fila,desde_col,hasta_fila,hasta_col)
                if piezacapturadanegra != None:
                    self.__listacapturadaspornegro__.append(piezacapturadanegra)
                self.__turno__ = 'WHITE'
                return True
                 
            #VERIFICAR QUE EL JUGADOR BLANCO NO PUEDA
            #MOVER FICHAS

        except Exception as e:
            raise e
        
    #def listacapturadas
        
