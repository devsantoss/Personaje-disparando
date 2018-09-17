"""
@author: David s

"""
import pygame,sys
from disparo import *

#Hereda de Sprite
class Personaje(pygame.sprite.Sprite):
    
    #constructor de la clase Personaje
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgPersonaje = pygame.image.load("imagenes/personaje.png")
        self.imgPersonaje = pygame.transform.scale(self.imgPersonaje, (200,200))
        #toma el rectangulo imagen
        self.rect = self.imgPersonaje.get_rect()
        #se situa en la pantalla
        self.rect.centerx=200
        self.rect.centery=500
        #agrega la velocidad de desplazamiento
        self.velocidad=20
        self.vida=True
        #arreglo de disparos que ejecutara el personaje
        self.listaDisparo=[]
    #define hasta donde el personaje se desplaza
    def mover(self):
        if self.vida == True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>1000:
                self.rect.right=1000
    #funcion para que el personaje dispare
    def disparar(self,x,y):
        #crea el objeto de la clase Misil
        misil = Misil(x,y)
        self.listaDisparo.append(misil)
    #funcion para que se dibuje el personaje    
    def dibujar(self,superficie):
        superficie.blit(self.imgPersonaje,self.rect)
    
