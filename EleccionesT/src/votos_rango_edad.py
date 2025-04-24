from enum import Enum, auto

class Edad(Enum):
    """
    Enumeradores para los rangos de edad.
    """
    EDAD_JOVEN = auto() # 18 A 34
    EDAD_MEDIA = auto() # 35 A 54
    EDAD_MAYOR = auto() # 55 AÑOS EN ADELANTE
    

class Genero(Enum):
    """
    Enumeradores para género.
    """
    MASCULINO = auto()
    FEMENINO = auto()
    

class VotosRangoEdad:
    """
    Votos de un rango de edad.
    """

    def __init__(self, edad: Edad):
        """
        Crea los votos en un rango de edad.
        La cantidad de votos del género masculino y femenino se inicializan en 0.
        """
        self.cantidad_masculino = 0
        self.cantidad_femenino = 0
        self.edad = edad
        

    def dar_cantidad_masculino(self) -> int:
        """
        Retorna la cantidad de votos de personas con género masculino.
        """
        return self.cantidad_masculino

    def dar_cantidad_femenino(self) -> int:
        """
        Retorna la cantidad de votos de personas con género femenino.
        """
        return self.cantidad_femenino

    def dar_edad(self) -> Edad:
        """
        Retorna la edad del rango.
        """
        return self.edad

    def dar_cantidad_total_votos(self) -> int:
        """
        Retorna la cantidad total de votos.
        """
        return self.cantidad_masculino + self.cantidad_femenino

    def registrar_voto(self, genero: Genero):
        assert genero in Genero, "Genero no valido"
        
        """
        Registra un voto al género dado por parámetro.
        """
        
        if genero == Genero.MASCULINO:
            self.cantidad_masculino += 1
        elif genero == Genero.FEMENINO:
            self.cantidad_femenino += 1

    def reiniciar(self):
        """
        Reinicia el conteo de votos.
        """
        self.cantidad_masculino = 0
        self.cantidad_femenino = 0
        
