__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

import random
class Curso:
    
    ######################################################
    # Constantes
    ######################################################
    
    TOTAL_EST = 12
    
    def __init__(self):
        self.notas = []
        self.LlenarNotas()
    
    def LlenarNotas(self):
        est_Cont=0
        while est_Cont < self.TOTAL_EST:
            self.notas[est_Cont]= random.uniform(1.0, 5.0)
            est_Cont +=1
    
    def Promedio(self):
        # promedio=0
        # est=0
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        # est += 1
        # promedio += self.notas[est]
        
        # return promedio/self.TOTAL_EST
        
        promedio = 0
        est = 0
        while est<self.TOTAL_EST:
            promedio += self.notas[est]
            est += 1
        
        return promedio/self.TOTAL_EST
    
    def promedioFor(self):
        
        promedio = 0
        for nota in self.notas:
            promedio += nota
        
        return promedio/self.TOTAL_EST
    
    def notaMasRecurrente(self):
        
        notaRecurrente:float=0.0
        cantidadOcurrencias = 0
        
        for i in range(self.TOTAL_EST):
            notaBuscada = self.notas[i]
            contador = 0
            for j in range(self.TOTAL_EST):
                if self.notas[j] == notaBuscada:
                    contador+=1
            
            if contador > cantidadOcurrencias:
                notaRecurrente = notaBuscada
                cantidadOcurrencias = contador
        
        return notaRecurrente