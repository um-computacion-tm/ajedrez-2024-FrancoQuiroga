from game.ajedrez import Ajedrez
from game.excepciones import (NoexisteFicha,NoPuedeatacar,
                              FueraDelTablero, MovimientoErróneo,
                              FichaAjena, HayfichaAliada, MovimSaltaFicha)    
def mostrar_fichas_capturadas(ajedrez):
    print('Fichas caputuradas por el jugador blanco: ')
    ajedrez.lista_blancas
    print('Fichas capturadas por el jugador negro: ')
    ajedrez.lista_negras

def mostrar_tablero():
    pass

def turno_actual(ajedrez):
    return ajedrez.decir_turno

def verificar_ganador(ajedrez):
    #Si alguno de los jugadores tiene 16 piezas, gana automaticamente
    if len(ajedrez.lista_negras) == 16:
        return False
    
    if len(ajedrez.lista_blancas) == 16:
        return True
    
def play(ajedrez):
    while True:
        print('Tablero Actual: ')
        mostrar_tablero()
        # Pide el input del jugador
        try:
            print('Elija la Fila y Columna de la ficha que quiere mover')
            desde_fila = int(input('Ingrese la fila: '))
            desde_col  = str(input('Ingrese la columna: '))
            print('Elija la posicion a donde mover la ficha')
            hasta_fila = int(input('Ingrese la fila objetivo: ')) 
            hasta_col = str(input('Ingrese la columna objetivo: '))
            desde_col = hasta_col.upper()
            hasta_col = hasta_col.upper()
            ajedrez.traducir_posiciones(desde_fila,desde_col,hasta_fila,hasta_col)

        except ValueError:
            print('Elija un número correcto')
            continue
        
        except KeyError:
            print('Elija una fila de 1-8 y una columna de A-H')
            continue
    
def main():
    ajedrez = Ajedrez()
    jugar = play(ajedrez)

if __name__ == '__main__':
    main()