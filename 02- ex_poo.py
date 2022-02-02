#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    2. Classe Quadrado: Crie uma classe que modele um quadrado:
        a. Atributos: Tamanho do lado
        b. Métodos:   Mudar valor do Lado, Retornar valor do Lado 
                      e calcular Área;
"""
class Quadrado: 
    def __init__(self, L):
        self.L = L
        
    def novoLado(self, novo_L):
        self.L = novo_L 
        
    def valorLado(self):
        return self.L
    
    def area(self):
        A = self.L**2 
        print('Area do quadrado é: ', A)
        

q1 = Quadrado(2)
print('Lado do quadrado 1 é: ', q1.valorLado())
q2 = Quadrado(3)
print('Lado do quadrado 2 é: ', q2.valorLado())
q1.novoLado(5)
print('Lado do quadrado 1 é: ', q1.valorLado())
q2.novoLado(7.5)
print('Lado do quadrado 2 é: ', q2.valorLado())
q1.area()
q2.area()