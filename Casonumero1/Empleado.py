__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

################################
# Importaciones
################################
from Fecha import Fecha

class Empleado:
    #aqui inicia mi codigo
    nombres = ''
    apellidos = ''
    salario = 0
    # 1=Masculino, 2=Femenino
    sexo = 0
    # Asociaciones
    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()
    
    ################################################################
    # Constructor
    ################################################################
    
    def __init__(self, nombres, apellidos, salario, sexo):
        #Aqui va mi codigo
        self.nombres = nombres
        self.apellidos = apellidos
        self.salario = salario
        self.sexo = sexo
    
    ################################
    # Metodos
    ################################
    
    __method__ = "CambiarSalario"
    __params__ = "nuevoSalario"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        #Aqui va mi codigo
        self.salario = nuevoSalario
    
    __method__ = "DarSalario"
    __params__ = "Nada"
    __returns__ = "Salario"
    __descriptions__ = "Metodo que sirve para dar el salario del empleado"
    def DarSalario(self):
        #Aqui va mi codigo
        return self.salario
    
    __method__ = "DarSalarioAnual"
    __params__ = "Nada"
    __returns__ = "SalarioAnual"
    __descriptions__ = "Metodo que sirve para dar el salario anual del empleado"
    def DarSalarioAnual(self):
        #Aqui va mi codigo
        return self.salario * 12
    
    __method__ = "DuplicarSalario"
    __params__ = "Nada"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para duplicar el salario del empleado"
    def DuplicarSalario(self):
        #Aqui va mi codigo
        self.salario = self.salario * 2
        
    __method__ = "CalcularImpuestoAnual"
    __params__ = "Nada"
    __returns__ = "ImpuestoAnual"
    __descriptions__ = "Metodo que sirve para calcular el impuesto anual del empleado"
    
    def CalcularImpuestoAnual(self):
        #Aqui va mi codigo
        # forma 1
        total = self.DarSalarioAnual()
        return total * 19 / 100
    
        # forma 2
        # return self.DarSalarioAnual() * 0.19
        
    ################################################################
    # Lamado a Asociacion
    ################################################################
    
    __method__ = "DarDiaNacimiento"
    __params__ = "Nada"
    __returns__ = "DiaNacimiento"
    __descriptions__ = "Metodo que sirve para dar el dia de nacimiento del empleado"
    def DarDiaNacimiento(self):
        #Aqui va mi codigo
        return self.fechaNacimiento.DarDia()