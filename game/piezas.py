class Piezas:
    def __init__(self,COLOR:str) -> None:
        """Parametros:
        ---------
        __color__: str

        Tiene que ser 'BLACK' o 'WHITE'
            """
        self.__color__ = COLOR
    
    @property
    def decircolor(self)-> str:
        return self.__color__