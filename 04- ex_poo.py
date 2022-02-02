#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Classe Pessoa: Crie uma classe que modele uma pessoa:
        a. Atributos: nome, idade, peso e altura
        b. Métodos: Envelhercer, engordar, emagrecer, crescer. 
        Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a 
        idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura): 
        self.nome   = nome
        self.idade  = idade
        self.peso   = peso 
        self.altura = altura
        self.info   = [self.nome, self.idade, self.peso, self.altura]
   
    def envelhecer(self, anos):
        print()
        print(self.nome," envelheceu ", anos, " anos.")
        print("Agora ", self.nome," tem ", self.idade + anos," anos de idade. ") 
        ida = self.idade
        self.idade   = self.idade + anos
        self.info[1] = self.idade 
        
        if ida < 21.0:
            self.altura  = self.altura + 0.5*anos 
            self.info[3] = self.altura 
            
    def engordar(self, kg):
        print()
        print(self.nome," engordou ", kg, "Kg")
        print("Agora ", self.nome, " pesa ", self.peso + kg, " Kg.") 
        self.info[2] = self.peso + kg
        
    def emagrecer(self, kg):
        print()
        print(self.nome," emegreceu ", kg, "Kg")
        print("Agora ", self.nome, " pesa ", self.peso - kg, " Kg.") 
        self.peso   = self.peso - kg
        self.info[2] = self.peso
       
        
    def crescer(self, cm):
        print()
        if self.idade < 21: 
            ida = self.idade + cm/0.5  
            if ida > 21.0:
                print('Invalido ! O crescimento excede a taxa de 0.5cm/ano')
                cm = (21.0 - self.idade)/0.5 
                print(self.nome, 'poderá crescer apenas ', cm , 'cm até os 21 anos.')
                return 
            self.idade = self.idade + cm/0.5  
            self.info[1] = self.idade
            print(self.nome," cresceu ", cm, "cm")
            print("Agora ", self.nome, " tem altura de ",self.altura + cm, " cm.")
        elif self.idade > 21:
            print(self.nome,'já passou dos 21 anos e não cresce mais.' )
            
     
    def infos(self):
        print()
        print('Informaões da pessoa: ')
        labels = ['nome','idade (anos)', 'peso (kg)', 'altura (cm)']
        for i in range(len(labels)):
            print(labels[i],":",self.info[i])
        
        
pessoa1 = Pessoa('Luciano', 20, 85, 190) 
 
pessoa1.engordar(5) 
pessoa1.emagrecer(5) 
pessoa1.emagrecer(5) 
pessoa1.envelhecer(2) 
pessoa1.envelhecer(5) 
pessoa1.infos() 