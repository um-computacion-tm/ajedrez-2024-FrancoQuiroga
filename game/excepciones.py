class NoPuedeatacar(Exception):
    ...
class NoexisteFicha(Exception):
    """ Excepción
    
    Usada cuando se elige una casilla que no tiene ninguna ficha"""
    ...
class FueraDelTablero(Exception):
    """ Excepción
    
    Usada cuando se quiere hacer un movimiento con un tablero
    de mayor tamaño que un 8x8"""
    ...
class MovimientoErróneo(Exception):
    """Excepción

    Usada cuando una ficha no puede efectuar el movimiento,
    porque es un mov inválido. 
    """
    ...
class FichaAjena(MovimientoErróneo):
    ...
class HayfichaAliada(MovimientoErróneo):
    ...

class MovimSaltaFicha(MovimientoErróneo):
    """Excepción
    Usada cuando una ficha, que no sea el caballo,
    intenta atacar pasando sobre otra ficha(aliada o enemiga)"""
