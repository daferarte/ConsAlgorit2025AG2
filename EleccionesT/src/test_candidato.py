import pytest
from candidato import Candidato, Medio
from votos_rango_edad import Edad, Genero, VotosRangoEdad


@pytest.fixture
def candidato():
    return Candidato("Ana", "Pérez", "Partido Verde", 45, 1)


def test_creacion_candidato(candidato):
    assert candidato.dar_nombre() == "Ana"
    assert candidato.dar_apellido() == "Pérez"
    assert candidato.dar_partido_politico() == "Partido Verde"
    assert candidato.dar_edad() == 45
    assert candidato.dar_numero() == 1
    assert candidato.dar_costo_campanha() == 0
    assert candidato.dar_cantidad_total_votos() == 0


def test_registrar_voto_internet(candidato):
    candidato.registrar_voto(Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.INTERNET)
    assert candidato.dar_cantidad_total_votos() == 1
    assert candidato.dar_total_votos_genero_femenino() == 1
    assert candidato.dar_costo_campanha() == Candidato.COSTO_INTERNET


def test_registrar_voto_radio(candidato):
    candidato.registrar_voto(Edad.EDAD_MEDIA, Genero.MASCULINO, Medio.RADIO)
    assert candidato.dar_cantidad_total_votos() == 1
    assert candidato.dar_total_votos_genero_masculino() == 1
    assert candidato.dar_costo_campanha() == Candidato.COSTO_RADIO


def test_registrar_voto_television(candidato):
    candidato.registrar_voto(Edad.EDAD_MAYOR, Genero.FEMENINO, Medio.TELEVISION)
    assert candidato.dar_cantidad_total_votos() == 1
    assert candidato.dar_total_votos_genero_femenino() == 1
    assert candidato.dar_costo_campanha() == Candidato.COSTO_TELEVISION


def test_varios_votos(candidato):
    candidato.registrar_voto(Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.INTERNET)
    candidato.registrar_voto(Edad.EDAD_MEDIA, Genero.MASCULINO, Medio.RADIO)
    candidato.registrar_voto(Edad.EDAD_MAYOR, Genero.FEMENINO, Medio.TELEVISION)

    assert candidato.dar_cantidad_total_votos() == 3
    assert candidato.dar_total_votos_genero_femenino() == 2
    assert candidato.dar_total_votos_genero_masculino() == 1
    assert candidato.dar_costo_campanha() == (
        Candidato.COSTO_INTERNET + Candidato.COSTO_RADIO + Candidato.COSTO_TELEVISION
    )


def test_reiniciar(candidato):
    candidato.registrar_voto(Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.INTERNET)
    candidato.registrar_voto(Edad.EDAD_MEDIA, Genero.MASCULINO, Medio.RADIO)
    candidato.reiniciar()

    assert candidato.dar_cantidad_total_votos() == 0
    assert candidato.dar_total_votos_genero_femenino() == 0
    assert candidato.dar_total_votos_genero_masculino() == 0
    assert candidato.dar_costo_campanha() == 0


# --- NUEVAS PRUEBAS ---

def test_votos_por_rango(candidato):
    candidato.registrar_voto(Edad.EDAD_JOVEN, Genero.MASCULINO, Medio.INTERNET)
    candidato.registrar_voto(Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.RADIO)
    candidato.registrar_voto(Edad.EDAD_MEDIA, Genero.MASCULINO, Medio.TELEVISION)
    assert candidato.dar_votos_rango1().dar_cantidad_total_votos() == 2
    assert candidato.dar_votos_rango2().dar_cantidad_total_votos() == 1
    assert candidato.dar_votos_rango3().dar_cantidad_total_votos() == 0


def test_acumulacion_costos(candidato):
    candidato.registrar_voto(Edad.EDAD_JOVEN, Genero.MASCULINO, Medio.INTERNET)
    candidato.registrar_voto(Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.INTERNET)
    assert candidato.dar_costo_campanha() == 2 * Candidato.COSTO_INTERNET


def test_dar_votos_rango_instancias(candidato):
    assert isinstance(candidato.dar_votos_rango1(), VotosRangoEdad)
    assert isinstance(candidato.dar_votos_rango2(), VotosRangoEdad)
    assert isinstance(candidato.dar_votos_rango3(), VotosRangoEdad)


def test_votos_todos_masculinos(candidato):
    for edad in [Edad.EDAD_JOVEN, Edad.EDAD_MEDIA, Edad.EDAD_MAYOR]:
        candidato.registrar_voto(edad, Genero.MASCULINO, Medio.RADIO)
    assert candidato.dar_total_votos_genero_masculino() == 3
    assert candidato.dar_total_votos_genero_femenino() == 0


def test_votos_todos_femeninos(candidato):
    for edad in [Edad.EDAD_JOVEN, Edad.EDAD_MEDIA, Edad.EDAD_MAYOR]:
        candidato.registrar_voto(edad, Genero.FEMENINO, Medio.TELEVISION)
    assert candidato.dar_total_votos_genero_femenino() == 3
    assert candidato.dar_total_votos_genero_masculino() == 0
