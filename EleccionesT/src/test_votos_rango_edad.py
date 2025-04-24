import pytest
from votos_rango_edad import VotosRangoEdad, Edad, Genero

def test_creacion_votos_rango_edad():
    votos = VotosRangoEdad(Edad.EDAD_JOVEN)
    assert votos.dar_cantidad_masculino() == 0
    assert votos.dar_cantidad_femenino() == 0
    assert votos.dar_edad() == Edad.EDAD_JOVEN

def test_registro_voto_masculino():
    votos = VotosRangoEdad(Edad.EDAD_MEDIA)
    votos.registrar_voto(Genero.MASCULINO)
    assert votos.dar_cantidad_masculino() == 1
    assert votos.dar_cantidad_femenino() == 0

def test_registro_voto_femenino():
    votos = VotosRangoEdad(Edad.EDAD_MAYOR)
    votos.registrar_voto(Genero.FEMENINO)
    assert votos.dar_cantidad_masculino() == 0
    assert votos.dar_cantidad_femenino() == 1

def test_cantidad_total_votos():
    votos = VotosRangoEdad(Edad.EDAD_JOVEN)
    votos.registrar_voto(Genero.MASCULINO)
    votos.registrar_voto(Genero.FEMENINO)
    votos.registrar_voto(Genero.FEMENINO)
    assert votos.dar_cantidad_total_votos() == 3

def test_reiniciar_votos():
    votos = VotosRangoEdad(Edad.EDAD_MEDIA)
    votos.registrar_voto(Genero.MASCULINO)
    votos.registrar_voto(Genero.FEMENINO)
    votos.reiniciar()
    assert votos.dar_cantidad_masculino() == 0
    assert votos.dar_cantidad_femenino() == 0
    assert votos.dar_cantidad_total_votos() == 0
