from enum import Enum
from votos_rango_edad import VotosRangoEdad, Edad, Genero


class Medio(Enum):
    INTERNET = 1
    RADIO = 2
    TELEVISION = 3


class Candidato:
    COSTO_INTERNET = 100
    COSTO_RADIO = 500
    COSTO_TELEVISION = 1000

    def __init__(self, nombre: str, apellido: str, partido_politico: str, edad: int, numero: int):
        assert nombre, "El nombre no puede ser vacio"
        assert apellido, "El apellido no puede ser vacio"
        assert partido_politico, "El partido politico no puede ser vacio"
        assert edad >= 18, "La edad debe ser mayor o igual a 18"
        assert numero > 0, "El numero debe ser mayor de 0"
        
        self.__nombre:str = nombre
        self.__apellido:str =apellido
        self.__partido_politico:str = partido_politico
        self.__edad:int = edad
        self.__costo_campanha:int = 0
        self.__numero:int = numero
        
        self.__votos_rango1:VotosRangoEdad = VotosRangoEdad(Edad.EDAD_JOVEN)
        self.__votos_rango2:VotosRangoEdad = VotosRangoEdad(Edad.EDAD_MEDIA)
        self.__votos_rango3:VotosRangoEdad = VotosRangoEdad(Edad.EDAD_MAYOR)
        
    def dar_nombre(self):
        return self.__nombre
        

    def dar_apellido(self):
        return self.__apellido
        

    def dar_partido_politico(self):
        return self.__partido_politico

    def dar_edad(self):
        return self.__edad

    def dar_costo_campanha(self):
        return self.__costo_campanha

    def dar_numero(self):
        return self.__numero

    def dar_cantidad_total_votos(self):
        return (
            self.__votos_rango1.dar_cantidad_total_votos()+
            self.__votos_rango2.dar_cantidad_total_votos()+
            self.__votos_rango3.dar_cantidad_total_votos()
        )

    def dar_total_votos_genero_femenino(self):
        return (
            self.__votos_rango1.dar_cantidad_femenino()+
            self.__votos_rango2.dar_cantidad_femenino()+
            self.__votos_rango3.dar_cantidad_femenino()
        )

    def dar_total_votos_genero_masculino(self):
        return (
            self.__votos_rango1.dar_cantidad_masculino()+
            self.__votos_rango2.dar_cantidad_masculino()+
            self.__votos_rango3.dar_cantidad_masculino()
        )

    def dar_votos_rango1(self):
        return self.__votos_rango1

    def dar_votos_rango2(self):
        return self.__votos_rango2

    def dar_votos_rango3(self):
        return self.__votos_rango3

    def registrar_voto(self, edad: Edad, genero: Genero, medio: Medio):
        assert edad in Edad, "Edad no valida"
        assert genero in Genero, "Error"
        assert medio in Medio, "medio no valido"
        
        if edad == Edad.EDAD_JOVEN:
            self.__votos_rango1.registrar_voto(genero)
        elif edad == Edad.EDAD_MEDIA:
            self.__votos_rango2.registrar_voto(genero)
        elif edad == Edad.EDAD_MAYOR:
            self.__votos_rango3.registrar_voto(genero)
        
        if medio == Medio.INTERNET:
            self.__costo_campanha += self.COSTO_INTERNET
        elif medio == Medio.RADIO:
            self.__costo_campanha += self.COSTO_RADIO
        elif medio == Medio.TELEVISION:
            self.__costo_campanha += self.COSTO_TELEVISION

    def reiniciar(self):
        self.__votos_rango1.reiniciar()
        self.__votos_rango2.reiniciar()
        self.__votos_rango3.reiniciar()
        self.__costo_campanha = 0