__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from Tipo import Tipo
import constantes

class Producto:
        
    def __init__(self, nombre:str, tipo:Tipo, valorUnitario:float, cantidadBodega:int, cantidadMinima:int,calidad:str):
       self.__nombre:str = nombre
       self.__tipo:Tipo=tipo
       self.__valorUnitario:float = valorUnitario
       self.__cantidadBodega:int = cantidadBodega
       self.__cantidadMinima:int = cantidadMinima
       self.__subsidio:bool = False
       self.__calidad:str = calidad
       self.__unidadesVendidas=0
       
    
    __method__ = "DarValorUnitario"
    __params__ = "Ninguno"
    __returns__ = "valorUnitario"
    __descriptions__ = "Metodo que sirve para conocer el valor unitario de un producto"
    def DarValorUnitario(self):
        return self.__valorUnitario
    
    __method__ = "CambiarValorUnitario"
    __params__ = "valorUnitario"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el valor unitario de un producto"
    def CambiarValorUnitario(self, valorUnitario:float):
        self.__valorUnitario = valorUnitario
    
    __method__ = "DarSubsidio"
    __params__ = "Ninguno"
    __returns__ = "subsidio"
    __descriptions__ = "Metodo que sirve para conocer si un producto tiene subsidio"
    def DarSubsidio(self):
        return self.__subsidio
    
    __method__ = "CambiarSubsidio"
    __params__ = "subsidio"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el estado de subsidio de un producto"
    def CambiarSubsidio(self, subsidio:bool):
        self.__subsidio=subsidio
    
    __method__ = "DarCalidad"
    __params__ = "Ninguno"
    __returns__ = "calidad"
    __descriptions__ = "Metodo que sirve para conocer la calidad de un producto"
    def DarCalidad(self):
        return self.__calidad
    
    __method__ = "CambiarCalidad"
    __params__ = "calidad"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar la calidad de un producto"
    def CambiarCalidad(self, calidad:float):
        self.__calidad = calidad
        
    __method__ = "DarValorProductoSupermercado"
    __params__ = "Ninguno"
    __returns__ = "valorProductoSupermercado"
    __descriptions__ = "Metodo que sirve para conocer el valor de un producto de supermercado"
    def DarValorProductoSupermercado(self):
        # Forma1
        # total = (self.__valorUnitario*self.__IVA_SUPERMERCADO)+self.__valorUnitario
        # return total

        # Forma2
        return (self.__valorUnitario*constantes.IVA_SUPERMERCADO)+self.__valorUnitario
    
    
    __method__ = "Vender"
    __params__ = "cantidad"
    __returns__ = "Mensaje de confirmacion"
    __descriptions__ = "Metodo que sirve para vender productos"
    def Vender(self, cantidad:int):
        # aqui va el codigo
        if cantidad <= self.__cantidadBodega:
            self.__unidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad
            return 'Venta exitosa'
        else:
            return f'No se cuenta con {cantidad} de unidades disponibles de {self.__nombre} para su venta'
        
    __method__ = "HaySuficiente"
    __params__ = "cantidad"
    __returns__ = "suficiente"
    __descriptions__ = "Metodo que sirve para verificar si existen suficientes productos"
    def HaySuficiente(self, cantidad):
        # aqui va el codigo
        # Forma 1
        # suficiente:bool
        
        # if cantidad <= self.__cantidadBodega:
        #     suficiente = True
        # else: 
        #     suficiente = False
            
        # return suficiente
        
        # Forma 2
        # suficiente:bool = False
        
        # if cantidad <= self.__cantidadBodega:
        #     suficiente = True 
        
        # return suficiente
        
        # Forma 3
        return cantidad <= self.__cantidadBodega
    
    __method__ = "DarPrecioPapeleria"
    __params__ = "conIVA"
    __returns__ = "precio"
    __descriptions__ = "Metodo que sirve para retornar el precio de un producto"
    def DarPrecioPapeleria(self, conIVA:bool):
        precioFinal:float = self.__valorUnitario
        
        if conIVA:
            precioFinal *= (1+constantes.IVA_PAPELERIA)
            
        return precioFinal
    
    __method__ = "AjustarPrecio"
    __params__ = "ninguno"
    __returns__ = "nada"
    __descriptions__ = "Metodo que sirve para ajustar el precio de un producto"
    def AjustarPrecio(self):
        if self.__unidadesVendidas < 100:
            self.__valorUnitario *= (80/100)
        else:
            self.__valorUnitario *= 1.1
    
    __method__ = "DarIva"
    __params__ = "ninguno"
    __returns__ = "IVA producto"
    __descriptions__ = "Metodo que sirve para conocer el iva de un producto"
    def DarIva(self):
        
        if self.__tipo== Tipo.DROGUERIA:
            return constantes.IVA_DROGUERIA
        elif self.__tipo== Tipo.PAPELERIA:
            return constantes.IVA_PAPELERIA
        else:
            return constantes.IVA_SUPERMERCADO