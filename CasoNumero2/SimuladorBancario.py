__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

################################
# Importacines
################################

from CuentaAhorros import CuentaAhorros
from CDT import CDT
from CuentaCorriente import CuentaCorriente

class SimuladorBancario:
    nombre = ""
    cedula = ""
    mesActual = ""
    
    # Asociaciones
    cuentaAhorros = CuentaAhorros()
    cuentaCorriente = CuentaCorriente()
    cuentaCDT = CDT()
    
    ################################################################
    # Metodos
    ################################################################
    
    __method__ = "ConsignarCuentaCorriente"
    __params__ = "monto"
    __return__ = "Nada"
    __description__ = "Metodo que permite consignar dinero en la cuenta corriente"
    def ConsignarCuentaCorriente(self, monto):
        # Aqui va mi codigo
        self.cuentaCorriente.DepositarDinero(monto)
        
    __method__ = "SaldoTotal"
    __params__ = "Ninguno"
    __return__ = "SaldoTotal"
    __description__ = "Metodo que permite obtener el saldo total de las cuentas"
    def SaldoTotal(self):
        # Aqui va mi codigo
        """
        # Forma 1
        saldoTotal = self.cuentaAhorros.DarSaldo()
        saldoTotal = saldoTotal + self.cuentaCorriente.DarSaldo()
        saldoTotal = saldoTotal + self.cuentaCDT.DarInversion()
        
        return saldoTotal
        """
        # # Forma 2 
        # saldoTotal = self.cuentaAhorros.DarSaldo()+self.cuentaCorriente.DarSaldo()+self.cuentaCDT.DarInversion()
        # return saldoTotal
        
        # Forma 3
        return self.cuentaAhorros.DarSaldo() + self.cuentaCorriente.DarSaldo() + self.cuentaCDT.DarInversion()
    
    __method__ = "PasarAhorroCorriente"
    __params__ = "Ninguno"
    __return__ = "Nada"
    __description__ = "Metodo que permite pasar los ahorros a la cuenta corriente"
    def PasarAhorroCorriente(self):
        # Aqui va mi codigo
        ahorros = self.cuentaAhorros.DarSaldo()
        self.cuentaAhorros.RetirarDinero(ahorros)
        self.cuentaCorriente.DepositarDinero(ahorros)