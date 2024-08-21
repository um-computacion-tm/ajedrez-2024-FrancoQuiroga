class NoPuedeatacar(Exception):
    ...

class Puedeatacar(Exception):
    ...

class MovimientoErróneo(Exception):
    """Excepción

    Usada cuando una ficha no puede efectuar el movimiento,
    porque es un mov inválido. 
    """
    ...

class HayfichaAliada(MovimientoErróneo):
    ...

class MovimSaltaFicha(MovimientoErróneo):
    """Excepción
    Usada cuando una ficha, que no sea el caballo,
    intenta atacar pasando sobre otra ficha(aliada o enemiga)"""
