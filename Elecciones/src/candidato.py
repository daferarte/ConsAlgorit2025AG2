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
        self._nombre = nombre
        self._apellido = apellido
        self._partido_politico = partido_politico
        self._edad = edad
        self._costo_campanha = 0
        self._numero = numero

        self._votos_rango1 = VotosRangoEdad(Edad.EDAD_JOVEN)
        self._votos_rango2 = VotosRangoEdad(Edad.EDAD_MEDIA)
        self._votos_rango3 = VotosRangoEdad(Edad.EDAD_MAYOR)

    def dar_nombre(self):
        return self._nombre

    def dar_apellido(self):
        return self._apellido

    def dar_partido_politico(self):
        return self._partido_politico

    def dar_edad(self):
        return self._edad

    def dar_costo_campanha(self):
        return self._costo_campanha

    def dar_numero(self):
        return self._numero

    def dar_cantidad_total_votos(self):
        return (
            self._votos_rango1.dar_cantidad_total_votos()
            + self._votos_rango2.dar_cantidad_total_votos()
            + self._votos_rango3.dar_cantidad_total_votos()
        )

    def dar_total_votos_genero_femenino(self):
        return (
            self._votos_rango1.dar_cantidad_femenino()
            + self._votos_rango2.dar_cantidad_femenino()
            + self._votos_rango3.dar_cantidad_femenino()
        )

    def dar_total_votos_genero_masculino(self):
        return (
            self._votos_rango1.dar_cantidad_masculino()
            + self._votos_rango2.dar_cantidad_masculino()
            + self._votos_rango3.dar_cantidad_masculino()
        )

    def dar_votos_rango1(self):
        return self._votos_rango1

    def dar_votos_rango2(self):
        return self._votos_rango2

    def dar_votos_rango3(self):
        return self._votos_rango3

    def registrar_voto(self, edad: Edad, genero: Genero, medio: Medio):
        if edad == Edad.EDAD_JOVEN:
            self._votos_rango1.registrar_voto(genero)
        elif edad == Edad.EDAD_MEDIA:
            self._votos_rango2.registrar_voto(genero)
        elif edad == Edad.EDAD_MAYOR:
            self._votos_rango3.registrar_voto(genero)

        if medio == Medio.INTERNET:
            self._costo_campanha += self.COSTO_INTERNET
        elif medio == Medio.RADIO:
            self._costo_campanha += self.COSTO_RADIO
        elif medio == Medio.TELEVISION:
            self._costo_campanha += self.COSTO_TELEVISION

    def reiniciar(self):
        self._votos_rango1.reiniciar()
        self._votos_rango2.reiniciar()
        self._votos_rango3.reiniciar()
        self._costo_campanha = 0
