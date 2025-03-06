__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class CuentaAhorros:
    saldo = 0
    interes = 0.6
    
    ################################################################
    # Metodos
    ################################################################
    
    __method__ = "DarSaldo"
    __params__ = ""
    __return__ = "Saldo"
    __description__ = "Metodo que permite visualizar el saldo de la cuenta ahorros"
    def DarSaldo(self):
        # Aqui va mi codigo
        return self.saldo
    
    __method__ = "RetirarDinero"
    __params__ = "monto"
    __return__ = "Nada"
    __description__ = "Metodo que permite retirar dinero de la cuenta ahorros"
    def RetirarDinero(self, monto):
        # Aqui va mi codigo
        self.saldo = self.saldo - monto
        
    __method__ = "DepositarDinero"
    __params__ = "monto"
    __return__ = "Nada"
    __description__ = "Metodo que permite depositar dinero en la cuenta ahorros"
    def DepositarDinero(self, monto):
        # Aqui va mi codigo
        self.saldo = self.saldo + monto    