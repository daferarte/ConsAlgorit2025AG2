__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from enum import Enum
from Pasajero import Pasajero

class Clase(Enum):
    EJECUTIVA = 1
    ECONOMICA = 2
    
class Ubicacion(Enum):
    VENTANA = 1
    PASILLO = 2
    CENTRO = 3

class Silla:
    
    def __init__(self, numero, clase:Clase, ubicacion:Ubicacion, pasajero:Pasajero = None):
        self.__numero = numero
        self.__clase = clase
        self.__ubicacion = ubicacion
        self.__pasajero = pasajero
        
    __method__ = "DarNumero"
    __params__ = "ninguno"
    __returns__ = "Numero"
    __descriptions__ = "Metodo que sirve para conocer el numero de la silla"
    def DarNumero(self):
       return self.__numero

    __method__ = "CambiarNumero"
    __params__ = "numero"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para cambiar el numero de la silla"
    def CambiarNumero(self, numero):
       self.__numero = numero
       
    __method__ = "DarClase"
    __params__ = "ninguno"
    __returns__ = "Clase"
    __descriptions__ = "Metodo que sirve para conocer la clase de la silla"
    def DarClase(self):
       return self.__clase

    __method__ = "CambiarClase"
    __params__ = "clase"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para cambiar la clase de la silla"
    def CambiarClase(self, clase:Clase):
       self.__clase = clase
       
    __method__ = "DarUbicacion"
    __params__ = "ninguno"
    __returns__ = "ubicacion"
    __descriptions__ = "Metodo que sirve para conocer la ubicacion de la silla"
    def DarUbicacion(self):
       return self.__ubicacion

    __method__ = "CambiarUbicacion"
    __params__ = "ubicacion"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para cambiar la ubicacion de la silla"
    def CambiarUbicacion(self, ubicacion:Ubicacion):
       self.__ubicacion = ubicacion
       
    __method__ = "DarPasajero"
    __params__ = "ninguno"
    __returns__ = "Pasajero"
    __descriptions__ = "Metodo que sirve para conocer el pasajero de la silla"
    def DarPasajero(self):
       return self.__pasajero
       
    __method__ = "AsignarPasajero"
    __params__ = "pasajero"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para asignar el pasajero de la silla"
    def AsignarPasajero(self, pasajero:Pasajero):
       self.__pasajero = pasajero
       
    __method__ = "DesasignarPasajero"
    __params__ = "ninguno"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para desasignar el pasajero de la silla"
    def DesasignarPasajero(self):
       self.__pasajero = None
       
    __method__ = "SillaAsignada"
    __params__ = "ninguno"
    __returns__ = "Estado de la silla ocupada = true, libre = false"
    __descriptions__ = "Metodo que sirve para verificar el estado de la silla"
    def SillaAsignada(self) -> bool:
       return self.__pasajero is not None