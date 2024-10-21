from game.ajedrez import Ajedrez
from game.excepciones import (NoexisteFicha,NoPuedeatacar,
                              FueraDelTablero, MovimientoErróneo,
                              FichaAjena, HayfichaAliada, MovimSaltaFicha,ReyCapturado,TerminaJuego)    
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

def tomar_input()-> list:
    desde_fila = (input('Ingrese la fila: '))
    if (desde_fila.lower()=='q'):
        raise TerminaJuego('CERRANDO PARTIDA')
        
    desde_col  = str(input('Ingrese la columna: '))
    if (desde_col.lower()=='q'):
        raise TerminaJuego('CERRANDO PARTIDA')
    print('Elija la posicion a donde mover la ficha')
    hasta_fila = (input('Ingrese la fila objetivo: '))
    if (hasta_fila.lower()=='q'):
        raise TerminaJuego('CERRANDO PARTIDA')
    hasta_col = str(input('Ingrese la columna objetivo: '))
    if (hasta_col.lower()=='q'):
        raise TerminaJuego('CERRANDO PARTIDA')
    else:
        return desde_fila,desde_col,hasta_fila,hasta_col


def play(ajedrez):
    while True:
        print('Tablero Actual: ')
        print(f'El jugador actual es: {turno_actual(ajedrez)}')
        mostrar_tablero(ajedrez)

        # Pide el input del jugador
        
        try:
            print('Elija la Fila y Columna de la ficha que quiere mover')
            
            desde_fila,desde_col,hasta_fila,hasta_col = tomar_input()
            
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
        except TerminaJuego :
            print('CERRANDO PARTIDA\n')
            break
        
        try:
            moverpieza(ajedrez,desde_fila,desde_col,hasta_fila,hasta_col)
        except ReyCapturado as e:
            print(e)
            if ajedrez.decir_turno == 'WHITE':
                print('El jugador blanco es el ganador')
            else: 
                print('El jugador negro es el ganador')
                exit()

        except Exception as e:
              print(e)
              continue
def menu():
    ajedrez = Ajedrez()
    print(r"""
  ______                            __                              
 /      \                          |  \                             
|  $$$$$$\      __   ______    ____| $$  ______    ______  ________ 
| $$__| $$     |  \ /      \  /      $$ /      \  /      \|        |
| $$    $$      \$$|  $$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$\ \$$$$$$$$
| $$$$$$$$     |  \| $$    $$| $$  | $$| $$   \$$| $$    $$ /    $$ 
| $$  | $$     | $$| $$$$$$$$| $$__| $$| $$      | $$$$$$$$/  $$$$_ 
| $$  | $$     | $$ \$$     \ \$$    $$| $$       \$$     \  $$    |
 \$$   \$$__   | $$  \$$$$$$$  \$$$$$$$ \$$        \$$$$$$$\$$$$$$$$
         |  \__/ $$                                                 
          \$$    $$                                                 
           \$$$$$$                                                  
""")
    while True:
        try:
            print('1- Jugar al ajedrez')
            print('2- Cambiar el color del tablero(El color por defecto está pensado para consolas en modo oscuro)')
            print('3- Información Importante')
            print('4- Cerrar el Juego')
            eleccion = input('Elija una opción: ')
            eleccion = int(eleccion)
            if 1 > eleccion > 3:
                print('ERROR: Elija un número correcto (1-2-3)')
                continue
            if eleccion == 1:
                play(ajedrez)
            if eleccion == 2:
                print('COLOR CAMBIADO EXITOSAMENTE\n')
                ajedrez.cambiar_interfaz
            if eleccion == 3:
                print('''- Para volver a este menú durante el juego, presionar 'q' o 'Q'
- Si usas tu consola en color claro, es recomendable cambiar la interfaz para una experiencia más agradable
- Las fichas de la parte inferior son SIEMPRE del jugador BLANCO, y las de la parte superior son del jugador NEGRO \n
                      ''')
                continue
            if eleccion == 4:
                print('CERRANDO PROGRAMA')
                return False
            eleccion = 0
        except:
            print('ERROR: Ingrese un número correcto')
            continue
            
def main():
    menu()
    #ajedrez= Ajedrez()
    #play(ajedrez)
    

if __name__ == '__main__':
    main()