from ajedrez import Ajedrez
def main():
    ajedrez = Ajedrez()
    
def play(Ajedrez):
    try:
        #Pedir Input
        desde_fila = int(input('desde_fila: '))#Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro
        desde_col = int(input('desde_col: '))#Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro
        hasta_fila = int(input('hasta_fila: '))#Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro
        hasta_col = int(input('hasta_col: ')) #Aca se le pide al usuario 4 datos, fila-columna, desde un lugar hasta otro|
        #Verificar el Movimiento
        ajedrez.mover(desde_fila,desde_col,hasta_fila,hasta_col)
        #Mover la pieza
        #Cambiar de Turno
    except Exception as e:
        print('Error')
if __name__ == '__main__':
    main()