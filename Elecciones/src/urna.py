from candidato import Candidato, Medio
from votos_rango_edad import Edad, Genero


class Urna:
    def __init__(self):
        self._candidato1 = Candidato("Andrea", "Combes", "Independiente", 27, 1)
        self._candidato2 = Candidato("Felipe", "Pitti", "Revolucionario", 26, 2)
        self._candidato3 = Candidato("Susanita", "Chirusi", "Tradicional", 26, 3)

    def dar_candidato1(self):
        return self._candidato1

    def dar_candidato2(self):
        return self._candidato2

    def dar_candidato3(self):
        return self._candidato3

    def buscar_candidato(self, numero):
        if self._candidato1.dar_numero() == numero:
            return self._candidato1
        elif self._candidato2.dar_numero() == numero:
            return self._candidato2
        elif self._candidato3.dar_numero() == numero:
            return self._candidato3
        return None

    def calcular_total_votos(self):
        return (self._candidato1.dar_cantidad_total_votos() +
                self._candidato2.dar_cantidad_total_votos() +
                self._candidato3.dar_cantidad_total_votos())

    def calcular_total_votos_genero_femenino(self):
        return (self._candidato1.dar_total_votos_genero_femenino() +
                self._candidato2.dar_total_votos_genero_femenino() +
                self._candidato3.dar_total_votos_genero_femenino())

    def calcular_total_votos_genero_masculino(self):
        return (self._candidato1.dar_total_votos_genero_masculino() +
                self._candidato2.dar_total_votos_genero_masculino() +
                self._candidato3.dar_total_votos_genero_masculino())

    def dar_total_votos_rango_edad(self, edad):
        if edad == Edad.EDAD_JOVEN:
            return (self._candidato1.dar_votos_rango1().dar_cantidad_total_votos() +
                    self._candidato2.dar_votos_rango1().dar_cantidad_total_votos() +
                    self._candidato3.dar_votos_rango1().dar_cantidad_total_votos())
        elif edad == Edad.EDAD_MEDIA:
            return (self._candidato1.dar_votos_rango2().dar_cantidad_total_votos() +
                    self._candidato2.dar_votos_rango2().dar_cantidad_total_votos() +
                    self._candidato3.dar_votos_rango2().dar_cantidad_total_votos())
        elif edad == Edad.EDAD_MAYOR:
            return (self._candidato1.dar_votos_rango3().dar_cantidad_total_votos() +
                    self._candidato2.dar_votos_rango3().dar_cantidad_total_votos() +
                    self._candidato3.dar_votos_rango3().dar_cantidad_total_votos())
        return 0

    def calcular_costo_promedio_campanha(self):
        total = (self._candidato1.dar_costo_campanha() +
                 self._candidato2.dar_costo_campanha() +
                 self._candidato3.dar_costo_campanha())
        return total / 3

    def calcular_porcentaje_votos_candidato(self, numero):
        candidato = self.buscar_candidato(numero)
        if not candidato:
            return 0
        total = self.calcular_total_votos()
        return (candidato.dar_cantidad_total_votos() / total) * 100 if total > 0 else 0

    def registrar_voto(self, numero, edad, genero, medio):
        candidato = self.buscar_candidato(numero)
        if candidato:
            candidato.registrar_voto(edad, genero, medio)

    def reiniciar(self):
        self._candidato1.reiniciar()
        self._candidato2.reiniciar()
        self._candidato3.reiniciar()

    # Métodos de extensión
    def metodo1(self):
        return "Respuesta 1"

    def metodo2(self):
        return "Respuesta 2"
