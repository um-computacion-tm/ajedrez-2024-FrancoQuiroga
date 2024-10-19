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
    
def moverpieza(ajedrez,desde_fila,desde_col,hasta_fila,hasta_col):
            print('INTENTANDO REALIZAR EL MOVIMIENTO INDICADO')
            ajedrez.mover(desde_fila,desde_col,hasta_fila,hasta_col)
def play(ajedrez):
    while True:
        print('Tablero Actual: ')
        print(f'El jugador actual es: {turno_actual(ajedrez)}')
        mostrar_tablero(ajedrez)

        # Pide el input del jugador
        
        try:
            
            print('Elija la Fila y Columna de la ficha que quiere mover')
            desde_fila = (input('Ingrese la fila: '))
            if (desde_fila.lower()=='q'):
                exit('CERRANDO')
            desde_col  = str(input('Ingrese la columna: '))
            if (desde_col.lower()=='q'):
                exit('CERRANDO')
            print('Elija la posicion a donde mover la ficha')
            hasta_fila = (input('Ingrese la fila objetivo: '))
            if (hasta_fila.lower()=='q'):
                exit('CERRANDO')
            hasta_col = str(input('Ingrese la columna objetivo: '))
            if (hasta_col.lower()=='q'):
                exit('CERRANDO')
            desde_fila = int(desde_fila)
            hasta_fila = int(hasta_fila)
            desde_col = desde_col.upper()
            hasta_col = hasta_col.upper()
            movimiento = ajedrez.traducir_posiciones(desde_fila,desde_col,hasta_fila,hasta_col)
            desde_fila,desde_col,hasta_fila,hasta_col = movimiento

        except ValueError:
            print('ERROR: ELIJA EN LAS FILAS NÚMEROS DEL 1-8 y EN LAS COLUMNAS LETRAS DE A-H')
            continue
        
        except KeyError:
            print('ERROR: ELIJA EN LAS FILAS NÚMEROS DEL 1-8 y EN LAS COLUMNAS LETRAS DE A-H')
            continue
        
        try:
            moverpieza(ajedrez,desde_fila,desde_col,hasta_fila,hasta_col)
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