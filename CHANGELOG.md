# Usuario de github: FrancoQuiroga
# Apellido y Nombre: Quiroga, Franco
## [ V 0.0.7] 2025/10/18:
## Adiciones:
- Funcion para cambiar la fichas de las piezas, dependiendo del color del usuario.
- Menú para mejorar la experiencia del usuario.
- Funciones en Ajedrez y en main que acceden a una funcion nueva en tablero, que en conjunto permiten cambiar el color de las fichas, para que se adaptan a consolas con temas/colores claros.
## Arreglos:
- Arreglado un bug de main, que cambiaba el dato de la columna inicial.
- Arreglado un error con el ataque del peon.
- play() en main arreglado para que se cierre el programa con más facilidad.
- Separadas las funcionalidades de tomar_inputs y play, para intentar mejora la complejidad
- Tests para main

## [ V 0.0.7] 2025/10/14:
## Adiciones:
- Tests para ciertas funciones de main.
## Arreglos:
- Función play() en main arreglada, casi lista para terminar(Solo falta que la condicion de salida funcione mejor).
## [ V 0.0.6] 2024/10/14:
## Adiciones:
- Funcion que traduce las posiciones que completa el usuario
con datos usables por el tablero
- Funciones en main que le piden informacion a la clase ajedrez
- Métodos en ajedrez para devolver las piezas capturadas durante el juego

## Arreglos:
- Funcion validar_movimiento terminada, y agregada la verificación
que valida que el usuario sea del mismo color con la ficha
- Las excepciones ahora tienen un comentario asociado, que es utilizado en main para comunicarle al jugador que error cometió

## [ V 0.0.5] 2024/09/26:
## Arreglos:
- Funcion de validar_movimiento casi completa, y testeada

##  [ V 0.0.4] 2024/09/15:
## Adiciones:
- Funcion de validación de movimiento en el tablero
- Verificaciones reglas del Ajedrez en el tablero [WIP]
## Arreglos:
- Funcion val_nosaltarfichas de la clase Tablero [WIP]

##  [ V 0.0.3] 2024/08/29:
## Adiciones:
- Clase Rey y su función de movimiento, incluyendo sus tests.
- Verificaciones de movimientos en el tablero
- Verificaciones de reglas del ajedrez en el tablero


##  [V 0.0.2] 2024/08/15:
### Adiciones:
- Clases Peon, Alfil, Reina. También tienen funciones 
que verifica los movimientos en el tablero.
- Test para las clases de arriba.

### Arreglos:
- Test y función de movimiento en la clase Peon 

### Obsolecente:
- Atributo de inicio en la clase Alfil, llamado 'semueveenblancos'
y tests de dicho atributo
- Funciónes de movimiento de la clase Peon, ya que no cumplen su
objetivo de verificar los movimientos

## [V 0.0.1] 2024/08/15:

### Adiciones: 
- Clases Ajedrez, Piezas, Tablero, Torres. Se van a utilizar para 
hacer posible jugar al ajedrez.
- Tests para las clases mencionadas arriba.