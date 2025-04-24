__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Curso:
    
    TOTAL_EST = 12
    
    def __init__(self):
        
        self.__notas=[]
        self.__notas[0] = 2
        self.__notas[1] = 1
        self.__notas[2] = 2
        self.__notas[3] = 1
        self.__notas[4] = 2.4
        self.__notas[5] = 2.6
        self.__notas[6] = 3
    
    def noHaceNadaUtil(self, valor:float):
        
        indice:int = 10
        self.__notas[0] = 3.5
        if valor < 2.5 and len(self.__notas) == self.TOTAL_EST:
            self.__notas[indice] = self.__notas[0]
            self.__notas[0] = valor + 1.0
        else:
            self.__notas[indice] = self.__notas[0]-valor
        
    