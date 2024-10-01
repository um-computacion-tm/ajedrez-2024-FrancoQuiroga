from game.ajedrez import Ajedrez
from game.excepciones import (NoexisteFicha,NoPuedeatacar,
                              FueraDelTablero, MovimientoErróneo,
                              FichaAjena, HayfichaAliada, MovimSaltaFicha)    
def mostrar_fichas_capturadas():
    pass
def mostrar_tablero():
    pass

def turno_actual():
    pass

def verificar_ganador():
    #Si alguno de los jugadores tiene 16 piezas, gana automaticamente
    pass

def play(ajedrez):
    while True:
        print('Tablero Actual: ')
        mostrar_tablero()
        try:
            print('Elija la Fila y Columna de la ficha que quiere mmover')
            desde_fila = int(input('Ingrese la fila: '))
            desde_col  = int(input('Ingrese la columna: '))
            print('Elija la posicion a donde mover la ficha')
            hasta_fila = int(input('Ingrese la fila: ')) 
            hasta_col = int(input('Ingrese la columna: '))


        except ValueError:
            print('Elija un número correcto')
            continue
        
        except:
            pass
    #try:
    #    #Pedir Input
    #    desde_fila = int(input('desde_fila: '))#Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro
    #    desde_col = int(input('desde_col: '))#Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro
    #    hasta_fila = int(input('hasta_fila: '))#Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro
    #    hasta_col = int(input('hasta_col: ')) #Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro|
    #    #Verificar el Movimiento
    #    ajedrez.mover(desde_fila,desde_col,hasta_fila,hasta_col)
    #    #Mover la pieza
    #    #Cambiar de Turno
    #except Exception as e:
    #    print('Error')
def main():
    ajedrez = Ajedrez()
    jugar = play(ajedrez)

if __name__ == '__main__':
    main()