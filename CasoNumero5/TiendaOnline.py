__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

################################
# Asociacion
################################

from Clientes import Clientes
from Productos import Productos

class TiendaOnline:
    nombre = ''
    
    # Asociaciones
    cliente = Clientes()
    Producto = Productos()