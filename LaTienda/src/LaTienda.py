__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from Producto import Producto
from Tipo import Tipo

class Tienda:
    
    def __init__(self):
        self.__producto1=Producto("Lapiz", Tipo.PAPELERIA, 550.0, 18, 5, 'A' )
        self.__producto2=Producto("Aspirina", Tipo.DROGUERIA, 109.5, 25, 8, 'A' )
        self.__producto3=Producto("Borrador", Tipo.PAPELERIA, 207.3, 30, 10, 'A' )
        self.__producto4=Producto("pan", Tipo.SUPERMERCADO, 150.0, 15, 20, 'A' )
        self.__dineroCaja:float=0