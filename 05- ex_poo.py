#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
                       A classe deve possuir os seguintesatributos: número 
                       da conta, nome do correntista e saldo. Os métodos são 
                       os seguintes: alterarNome, depósito e saque; No construtor,
                       saldo é opcional, com valor default zero e os demais 
                       atributos são obrigatórios.
"""



class ContaCorrente:
    
    def __init__(self, numC, nome, saldo = 0.0):

        self.numC  = numC 
        self.nome  = nome 
        self.saldo = saldo 
        
    def alterarNome(self,num , novo_nome):
        
        if num == self.numC:
            self.nome = novo_nome 
            return 
    
        else:
            print('ERRO: Número da conta.')
            return 
        
    def deposito(self, num, valor):
        
        if num == self.numC:
            self.saldo += valor 
            return 
        else:
            print('ERRO: Número da conta')

    def saque(self, num, valor):
        
        if num == self.numC:
            if self.saldo > 0.0 and self.saldo - valor > 0.0: 
                self.saldo -= valor 
            else:
                print(' Saldo Insuficiente  ')
            return 
        else:
            print('ERRO: Número da conta')
   

    def exibe(self):
        print('Correntista: ', self.nome)
        print('Número da conta: ', self.numC)
        print('Seu saldo é de R$: ', self.saldo)
        
        
        
        
conta1 = ContaCorrente(160244, 'Luciano Mendes')
conta1.exibe() 
conta1.deposito(160244, 250)
conta1.exibe() 
conta1.deposito(160242, 250)
conta1.exibe() 
conta1.saque(160244, 300)
conta1.exibe() 
















