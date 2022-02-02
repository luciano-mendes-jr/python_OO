#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    1. Classe Bola: Crie uma classe que modele uma bola:
                a. Atributos: Cor, circunferência, material
                b. Métodos: trocaCor e mostraCor
"""

class Bola: 
    def __init__(self, cor, circ, material):
        self.cor  = cor 
        self.circ = circ 
        self.material = material  
        
    def trocaCor(self, nova_cor):
        self.cor = nova_cor 
        
    def mostraCor(self):
        print('Cor da bola:', self.cor)
        
        
bola1 = Bola('Branca', 3.14, 'couro')
bola1.mostraCor() 
bola1.trocaCor('Azul')
bola1.mostraCor() 
