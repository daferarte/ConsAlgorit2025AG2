__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Pasajero:

    def __init__(self, cedula, nombre):
        self.__cedula = cedula
        self.__nombre = nombre
        
    __method__ = "DarCedula"
    __params__ = "ninguno"
    __returns__ = "cedula"
    __descriptions__ = "Metodo que sirve para conocer la cedula del pasajero"
    def DarCedula(self):
       return self.__cedula

    __method__ = "CambiarCedula"
    __params__ = "cedula"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para cambiar la cedula del pasajero"
    def CambiarCedula(self, cedula):
       self.__cedula = cedula
       
    __method__ = "DarNombre"
    __params__ = "ninguno"
    __returns__ = "nombre"
    __descriptions__ = "Metodo que sirve para conocer el nombre del pasajero"
    def DarNombre(self):
       return self.__nombre

    __method__ = "CambiarNombre"
    __params__ = "nombre"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para cambiar el nombre del pasajero"
    def CambiarNombre(self, nombre):
       self.__nombre = nombre