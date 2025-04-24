import pytest
from urna import Urna
from votos_rango_edad import Edad, Genero
from candidato import Medio


@pytest.fixture
def urna():
    return Urna()


def test_candidatos_iniciales(urna):
    assert urna.dar_candidato1().dar_nombre() == "Andrea"
    assert urna.dar_candidato2().dar_apellido() == "Pitti"
    assert urna.dar_candidato3().dar_partido_politico() == "Tradicional"


def test_buscar_candidato(urna):
    assert urna.buscar_candidato(1).dar_nombre() == "Andrea"
    assert urna.buscar_candidato(2).dar_nombre() == "Felipe"
    assert urna.buscar_candidato(3).dar_nombre() == "Susanita"
    assert urna.buscar_candidato(4) is None


def test_votos_y_porcentaje(urna):
    urna.registrar_voto(1, Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.INTERNET)
    urna.registrar_voto(2, Edad.EDAD_MEDIA, Genero.MASCULINO, Medio.RADIO)
    urna.registrar_voto(3, Edad.EDAD_MAYOR, Genero.FEMENINO, Medio.TELEVISION)
    assert urna.calcular_total_votos() == 3
    assert urna.calcular_porcentaje_votos_candidato(1) == pytest.approx(100 / 3, 0.1)
    assert urna.calcular_porcentaje_votos_candidato(2) == pytest.approx(100 / 3, 0.1)
    assert urna.calcular_porcentaje_votos_candidato(3) == pytest.approx(100 / 3, 0.1)


def test_votos_por_genero(urna):
    urna.registrar_voto(1, Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.INTERNET)
    urna.registrar_voto(2, Edad.EDAD_JOVEN, Genero.MASCULINO, Medio.RADIO)
    assert urna.calcular_total_votos_genero_femenino() == 1
    assert urna.calcular_total_votos_genero_masculino() == 1


def test_votos_por_edad(urna):
    urna.registrar_voto(1, Edad.EDAD_JOVEN, Genero.MASCULINO, Medio.INTERNET)
    urna.registrar_voto(2, Edad.EDAD_MEDIA, Genero.FEMENINO, Medio.RADIO)
    urna.registrar_voto(3, Edad.EDAD_MAYOR, Genero.FEMENINO, Medio.TELEVISION)
    assert urna.dar_total_votos_rango_edad(Edad.EDAD_JOVEN) == 1
    assert urna.dar_total_votos_rango_edad(Edad.EDAD_MEDIA) == 1
    assert urna.dar_total_votos_rango_edad(Edad.EDAD_MAYOR) == 1


def test_costo_promedio_campanha(urna):
    # Cada voto debería aumentar el costo de campaña
    urna.registrar_voto(1, Edad.EDAD_MEDIA, Genero.FEMENINO, Medio.INTERNET)
    urna.registrar_voto(2, Edad.EDAD_MEDIA, Genero.FEMENINO, Medio.INTERNET)
    urna.registrar_voto(3, Edad.EDAD_MEDIA, Genero.FEMENINO, Medio.INTERNET)
    promedio = urna.calcular_costo_promedio_campanha()
    assert promedio > 0


def test_reiniciar(urna):
    urna.registrar_voto(1, Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.RADIO)
    urna.registrar_voto(2, Edad.EDAD_MAYOR, Genero.MASCULINO, Medio.TELEVISION)
    urna.reiniciar()
    assert urna.calcular_total_votos() == 0
    assert urna.calcular_costo_promedio_campanha() == 0

def test_multiples_votos_mismo_candidato(urna):
    for _ in range(10):
        urna.registrar_voto(1, Edad.EDAD_MEDIA, Genero.FEMENINO, Medio.RADIO)
    assert urna.buscar_candidato(1).dar_cantidad_total_votos() == 10
    assert urna.calcular_total_votos() == 10
    assert urna.calcular_porcentaje_votos_candidato(1) == 100.0


def test_porcentaje_sin_votos(urna):
    porcentaje = urna.calcular_porcentaje_votos_candidato(1)
    # Si no hay votos, debería evitar división por cero
    assert porcentaje == 0.0


def test_voto_candidato_inexistente(urna):
    urna.registrar_voto(5, Edad.EDAD_JOVEN, Genero.MASCULINO, Medio.INTERNET)
    # No debería lanzar excepción, simplemente ignorar
    assert urna.calcular_total_votos() == 0


def test_reiniciar_variado(urna):
    urna.registrar_voto(1, Edad.EDAD_JOVEN, Genero.FEMENINO, Medio.TELEVISION)
    urna.registrar_voto(2, Edad.EDAD_MEDIA, Genero.MASCULINO, Medio.RADIO)
    assert urna.calcular_total_votos() == 2
    urna.reiniciar()
    assert urna.calcular_total_votos() == 0
    urna.reiniciar()  # Reinicio extra no debería causar error
    assert urna.calcular_total_votos() == 0


def test_extensiones(urna):
    assert urna.metodo1() == "Respuesta 1"
    assert urna.metodo2() == "Respuesta 2"
