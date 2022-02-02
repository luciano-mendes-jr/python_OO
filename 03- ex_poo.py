#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3. Classe Retangulo: Crie uma classe que modele um retangulo:
    
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura,
a escolher)

b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular 
Área e calcular Perímetro;

c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que 
informe as medidades de um local. Depois, deve criar um objeto com as medidas 
e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""
class Retangulo: 
    b_aux = 0
    h_aux = 0
    def __init__(self, base, altura):
        try:
            self.base   = b_aux = float(base) 
            self.altura = h_aux = float(altura)
        except ValueError:
            print("\033[1;31mValueError: \033[0;0m Tipo de dado invalido !")
            return
        
        
    def mudaLados(self, b = b_aux, h = h_aux):
        try:
            self.base   = float(b) 
            self.altura = float(h)
        except ValueError:
            print("\033[1;31mValueError: \033[0;0m Tipo de dado invalido !")
            return
        
        
    def retornaLados(self):
        return self.base, self.altura
    
    
    def area(self):
         b = self.base
         h = self.altura
         A = b*h 
         return A 
     
        
    def perimetro(self):
        P = 2*self.base + 2*self.altura
        return P 
    
    
print('Digite as medidas do local: ')
comp  = input("Comprimento: ")
larg  = input("Largura: ")
local = Retangulo(comp, larg)   

print('Digite as medidas do piso: ')
comp = input("Comprimento: ")
larg = input("Largura: ")
piso = Retangulo(comp, larg) 

print('Digite as medidas do rodapé: ')
comp = input("Comprimento: ")
larg = input("Largura: ")
rdpe = Retangulo(comp, larg)

quant_pisos = local.area()/piso.area()  
quant_rodps = local.perimetro()/rdpe.retornaLados()[0]

print(f'Você irá utilizar um total de {quant_pisos} pisos e {quant_rodps} rodapés.')

































