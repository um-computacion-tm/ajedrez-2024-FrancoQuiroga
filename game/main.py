from game.ajedrez import Ajedrez
from game.excepciones import (NoexisteFicha,NoPuedeatacar,
                              FueraDelTablero, MovimientoErróneo,
                              FichaAjena, HayfichaAliada, MovimSaltaFicha,ReyCapturado)    
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
                return False
            desde_col  = str(input('Ingrese la columna: '))
            if (desde_col.lower()=='q'):
                return False
            print('Elija la posicion a donde mover la ficha')
            hasta_fila = (input('Ingrese la fila objetivo: '))
            if (hasta_fila.lower()=='q'):
                return False
            hasta_col = str(input('Ingrese la columna objetivo: '))
            if (hasta_col.lower()=='q'):
                return False
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
    print("""
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
        print('1- Jugar al ajedrez')
        print('2- Cambiar el color del tablero(El color por defecto está pensado para consolas en modo oscuro)')
        print('3- Información Importante')
        print('4- Cerrar el Juego')
        try:
            inputuser = int('Elija una opción: ')
            if 1 > inputuser > 3:
                print('ERROR: Elija un número correcto (1-2-3)')
                continue
            if inputuser == 1:
                play(ajedrez)
            if inputuser == 2:
                ajedrez.cambiar_interfaz
            if inputuser == 3:
                print('- Para volver al menú durante el juego, presionar q o Q \n \
                      - Si usas tu consola en color claro, es recomendable cambiar la interfaz\n \
                    para una experiencia más agradable \
                      ')
                continue
            if inputuser == 4:
                exit('Cerrando Programa')
        except:
            print('ERROR: Ingrese un número correcto')
            
def main():
    menu()

if __name__ == '__main__':
    main()