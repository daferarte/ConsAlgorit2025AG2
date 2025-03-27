class Producto:
    
    def __init__(self, valorUnitario:float):
       self.valorUnitario:float = valorUnitario
       self.subsidio:bool = False
    
    __method__ = "DarValorUnitario"
    __params__ = "Ninguno"
    __returns__ = "valorUnitario"
    __descriptions__ = "Metodo que sirve para conocer el valor unitario de un producto"
    def DarValorUnitario(self):
        return self.valorUnitario
    
    __method__ = "CambiarValorUnitario"
    __params__ = "valorUnitario"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el valor unitario de un producto"
    def CambiarValorUnitario(self, valorUnitario:float):
        self.valorUnitario = valorUnitario
    
    __method__ = "DarSubsidio"
    __params__ = "Ninguno"
    __returns__ = "subsidio"
    __descriptions__ = "Metodo que sirve para conocer si un producto tiene subsidio"
    def DarSubsidio(self):
        return self.subsidio
    
    __method__ = "CambiarSubsidio"
    __params__ = "subsidio"
    __returns__ = "Nada"
    __descriptions__ = "Metodo que sirve para cambiar el estado de subsidio de un producto"
    def CambiarSubsidio(self, subsidio:bool):
        self.subsidio=subsidio
    