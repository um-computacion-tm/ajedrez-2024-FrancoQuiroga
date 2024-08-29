from game.piezas import Piezas

class Rey(Piezas):
    def __init__(self, COLOR: str) -> None:
        super().__init__(COLOR)
    
    
    def movimiento(self,desde_fila:str,desde_col:str,
                   hasta_fila:str,hasta_col:str,)-> bool:
        tupladeemparejamientofila = (desde_fila-1, desde_fila+1)
        tupladeemparejamientocolumn = (desde_col -1, desde_col +1)

        if hasta_fila in tupladeemparejamientofila \
            or hasta_fila == desde_fila:
            
            if hasta_col in tupladeemparejamientocolumn \
                or hasta_col == desde_col:
                
                return True
            # El código funciona correctamente esté o no este código
            #(No tengo idea por qué pero funciona igual :/ )
            #else: 
            #    return False
        else: 
            return False    
        
    