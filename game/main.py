from game.ajedrez import Ajedrez
from game.excepciones import (NoexisteFicha,NoPuedeatacar,
                              FueraDelTablero, MovimientoErróneo,
                              FichaAjena, HayfichaAliada, MovimSaltaFicha)    
def mostrar_fichas_capturadas(ajedrez):
    print('Fichas caputuradas por el jugador blanco: ')
    ajedrez.listar_blancas
    print('Fichas capturadas por el jugador negro: ')
    ajedrez.listar_negras

def mostrar_tablero(ajedrez):
    return ajedrez.mostrar_tablero()

def turno_actual(ajedrez):
    return(ajedrez.decir_turno)

def verificar_ganador(ajedrez):
    #Si alguno de los jugadores tiene 16 piezas, gana automaticamente
    if ajedrez.longitud_lista_negras == 16:
        return False
    
    if ajedrez.longitud_lista_blancas == 16:
        return True
    
def play(ajedrez):
    while True:
        print('Tablero Actual: ')
        print(f'El jugador actual es: {turno_actual(ajedrez)}')
        mostrar_tablero(ajedrez)

        # Pide el input del jugador
        desde_fila = 0
        desde_col = 0
        hasta_fila = 0
        hasta_col = 0
        desde_fila_elegida = 0
        desde_col_elegida = 0
        hasta_fila_elegida = 0
        hasta_col_elegida = 0
        try:
            
            print('Elija la Fila y Columna de la ficha que quiere mover')
            desde_fila = input('Ingrese la fila: ')
            desde_col  = str(input('Ingrese la columna: '))
            print('Elija la posicion a donde mover la ficha')
            hasta_fila = input('Ingrese la fila objetivo: ')
            hasta_col = str(input('Ingrese la columna objetivo: '))
            inputsverif = [desde_fila,desde_col,hasta_fila,hasta_col]
            for iter in range(4):
                if (inputsverif[iter] == 'Q') or (inputsverif[iter] == 'q'):
                    exit('Cerrando el programa')
            desde_fila = int(desde_fila)
            hasta_fila = int(hasta_fila)
            desde_col = desde_col.upper()
            hasta_col = hasta_col.upper()
            movimiento = ajedrez.traducir_posiciones(desde_fila,desde_col,hasta_fila,hasta_col)
        except AttributeError:
            print('ERROR: Asegurese que en las columnas haya escrito una letra')
            continue
        except ValueError:
            print('ERROR: Elija un número en las filas')
            continue
        
        except KeyError:
            print('ERROR: ELIJA EN LAS FILAS NÚMEROS DEL 1-8 y EN LAS COLUMNAS LETRAS DE A-H')
            continue
        
        try:
            print('INTENTANDO REALIZAR EL MOVIMIENTO INDICADO')
            desde_fila_elegida,desde_col_elegida,hasta_fila_elegida,hasta_col_elegida = movimiento
            ajedrez.mover(desde_fila_elegida,desde_col_elegida,hasta_fila_elegida,hasta_col_elegida)
        except Exception as e:
              print(e)
              continue
        
def main():
    ajedrez = Ajedrez()
    #print('PARA CERRAR EL JUEGO EN CUALQUIER MOMENTO PRESIONE , CUANDO ELIGE SU COLUMNA')
    #print('PARA CERRAR EL JUEGO CUANDO ELIGE COLUMNA PRESIONE T, CUANDO ELIGE SU COLUMNA')
    jugar = play(ajedrez)

if __name__ == '__main__':
    main()