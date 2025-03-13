__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Fecha:
    #aqui inicia mi codigo
    dia=0
    mes=0
    anio=0
    
    ################################################################
    # Constructor
    ################################################################
    def __init__(self, dia=1, mes=1, anio=1900):
        #Aqui va mi codigo
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    ################################
    # Metodos
    ################################
    
    __method__ = "DarDia"
    __params__ = "Nada"
    __returns__ = "Dia"
    __descriptions__ = "Metodo que sirve para dar el dia de la fecha"
    def DarDia(self):
        #Aqui va mi codigo
        return self.dia
    
    __method__ = "DarMes"
    __params__ = "Nada"
    __returns__ = "Mes"
    __descriptions__ = "Metodo que sirve para dar el mes de la fecha"
    def DarMes(self):
        #Aqui va mi codigo
        return self.mes
       
    __method__ = "DarAnio"
    __params__ = "Nada"
    __returns__ = "Anio"
    __descriptions__ = "Metodo que sirve para dar el anio de la fecha"
    def DarAnio(self):
        #Aqui va mi codigo
        return self.anio
    
    __method__ = "CambiarDia"
    __params__ = "nuevoDia"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el dia de la fecha"
    def CambiarDia(self, nuevoDia):
        #Aqui va mi codigo
        self.dia = nuevoDia
    
    __method__ = "CambiarMes"
    __params__ = "nuevoMes"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el mes de la fecha"
    def CambiarMes(self, nuevoMes):
        #Aqui va mi codigo
        self.mes = nuevoMes
        
    __method__ = "CambiarAnio"
    __params__ = "nuevoAnio"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el anio de la fecha"
    def CambiarAnio(self, nuevoAnio):
        #Aqui va mi codigo
        self.anio = nuevoAnio
        
    __method__ ="DarFecha"
    __params__ = "Ninguno"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para mostrar la fecha"
    def DarFecha(self):
        # Aqui va mi codigo
        return f"{self.DarDia()}/{self.DarMes()}/{self.DarAnio()}"