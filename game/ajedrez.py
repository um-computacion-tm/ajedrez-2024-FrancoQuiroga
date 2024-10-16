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
                 
            #VERIFICAR QUE EL JUGADOR BLANCO NO PUEDA --------
            #MOVER FICHAS NEGRAS -------

        except Exception as e:
            raise e
    @property
    def decir_turno(self):
        return self.__turno__
    @property
    def lista_blancas(self):
        for i in self.__listacapturadasporblanco__:
            print(i, end=' ')
            return self.__listacapturadasporblanco__

    @property
    def lista_negras(self):
        for i in self.__listacapturadaspornegro__:
            print(i, end=' ')
            return self.__listacapturadaspornegro__

    def traducir_posiciones(self,desde_fila:int,desde_col:str
                            ,hasta_fila:int,hasta_col:str):
        """Método usado por main, para traducir las direcciones del usuario
        en direcciones usables por el tablero
        
        Parámetros:
        (desde/hasta)_col: str, mayúscula de la A-H, 

        (desde/hasta)_fila: entero, entre 0 y 7, posición final del movimiento


        """

        diccionario_filas = {8:0,7:1,6:2,5:3,
                             4:4,3:5,2:6,1:7}
        
        diccionario_col = {'A':0,'B':1,'C':2,'D':3,
                           'E':4,'F':5,'G':6,'H':7}

        return diccionario_filas[desde_fila],diccionario_col[desde_col],diccionario_filas[hasta_fila],diccionario_col[hasta_col]