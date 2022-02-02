#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tamagushi:
    
    def __init__(self, nome, idade, fome = True, saude = False):
        
        self.nome  = nome 
        self.fome  = fome 
        self.saude = saude 
        self.idade = idade
        
    
    def status(self):

        fome  = 'Sem fome'
        saude = 'Saudavel' 
        humor = 'De boa'
        if self.fome == True: 
            fome = 'Com fome' 
        if self.saude == False :
            saude = 'Doente'
        
        if self.fome == True or self.saude == False:
            humor = 'Ruim'
        
        print(f'Nome: {self.nome:>15}')
        print(f'Idade:{self.idade:>15}')
        
        print(f'Fome: {fome:>15}')
        print(f'Saúde:{saude:>15}')
        print(f'Humor:{humor:>15}')
        
    def alteraNome(self, new_nome):    
        self.nome = new_nome 
        print('Nome alterado com sucesso !')
        return 
    
    def alteraFome(self, new_fome):
        self.fome = new_fome 
        return 
    
    def alteraSaude(self, new_saude):
        self.saude = new_saude 
        return 
    
    def alteraIdade(self, new_idade):
        self.idade = new_idade 
        return 
    
            
bichinho1 = Tamagushi('Veloso', 15)
bichinho1.alteraFome(False)
bichinho1.alteraSaude(True)
