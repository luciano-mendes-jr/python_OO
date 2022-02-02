#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informaro número do canal e aumentar ou diminuir o 
volume. Certifique-se de que o número do canal e o nível do volume permanecem 
dentro de faixas válidas.
"""

class TV:
    def __init__(self, canal, volume, status = 'OFF'):
        
        self.canal  = canal 
        self.volume = volume 
        self.status = status
        
    def muda_canal(self, new_canal):
        
        if self.status == 'ON' :
            if 0 <= new_canal <= 20: 
                self.canal = new_canal  
                print('Você está assistindo o canal: ', self.canal)
            else:
                print('Canal inexistente !')
                
        else:
            print('A TV está desligada')
    
    def muda_volume(self, new_volume):
        
        if self.status == 'ON' :
            if 0 <= new_volume <= 100: 
                self.volume = new_volume  
                print(' A tv está no volume:', self.volume)
            else:
                print('Faixa de volume inexistente.')
                
        else:
            print('A TV está desligada')
            
    def modo(self, stat): 
        self.status = stat
        if self.status == 'ON':
            print('TV ligada.')
            return
        print('TV desligada')

tv = TV(8, 20) 
tv.muda_canal(10)
tv.modo('ON')
tv.muda_canal(10)
tv.muda_volume(100)
tv.modo('OFF')
tv.muda_canal(8)



        
        