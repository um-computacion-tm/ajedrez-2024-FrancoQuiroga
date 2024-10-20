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

        except:
            raise 
    @property
    def cambiar_interfaz(self):
          self.__tablero__.cambiar_str_piezas
    @property
    def decir_turno(self):
        return self.__turno__
    
    @property
    def longitud_lista_blancas(self):
        return len(self.__listacapturadasporblanco__)
    @property
    def longitud_lista_negras(self):
        return len(self.__listacapturadaspornegro__)
    
    
    @property
    def listar_blancas(self):
        for i in self.__listacapturadasporblanco__:
            print(i, end=' ')
    @property
    def listar_negras(self):
        for i in self.__listacapturadaspornegro__:
            print(i, end=' ')
    

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
    
    def mostrar_pie_pagina(self):
        '''Método que imprime la cabecera del tablero
        No recibe ningún parámetro
        SOLO DEBE SER USADO POR mostrar_tablero()'''
        print( ' \n  └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘ ')
        print( '     A       B       C       D       E       F       G       H      ')
        
    def mostrar_cabecera(self):
        '''Método que imprime el pie de página del tablero,
        y además las letras de las columnas
        No recibe ningún parámetro
        SOLO DEBE SER USADO POR mostrar_tablero()'''
        print('  ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐ ')
    def mostrar_num_fila(self,numero):
        '''Método que imprime la correspondiente fila ingresado el número
        No recibe ningún parámetro
        SOLO DEBE SER USADO POR mostrar_tablero()'''
        print(abs(numero-8),end=' ')
    def mostrar_intermedio(self):
        '''Método que imprime la separación intermedia del tablero
        No recibe ningún parámetro
        SOLO DEBE SER USADO POR mostrar_tablero()'''
        print(' \n  ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤ ')
    def print_casilla_vacía(self,numero_col):
        if numero_col == 7:
                        print(f'├       ┤', end='')    
        elif numero_col == 0:
                        print(f'├       ', end='')    
        else :
                        print(f'┼       ', end='')
    def print_casilla_ocupada(self,numero_col,columna):
        if numero_col == 7:
                        print(f'├   {columna}   ┤', end='')
        elif numero_col == 0:
                        print(f'├   {columna}   ', end='')
        else:    
                        print(f'┼   {columna}   ', end='')
    def mostrar_tablero(self):
        #Llamar funcion que imprime la cabecera
        #Imprimir el tablero y las fichas
        #Llamar funcion que imprime el pie de página
        tableroactual = self.__tablero__.obtener_tablero
        
        self.mostrar_cabecera()
        for numerofila, fila in enumerate(tableroactual):
            self.mostrar_num_fila(numerofila)
            for numero_col,columna in enumerate(fila):
                if columna == None:
                    self.print_casilla_vacía(numero_col)
                else:
                    self.print_casilla_ocupada(numero_col,columna)
            if numerofila != 7:
                self.mostrar_intermedio()
        self.mostrar_pie_pagina()

#if __name__ == '__main__':
#    ajedrez = Ajedrez()
#    ajedrez.mostrar_tablero()