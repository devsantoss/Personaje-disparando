"""
@author: David s

"""
import pygame

#heredar el Sprite
class Misil(pygame.sprite.Sprite):
    
    #constructor de la clase Misil
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenMisil = pygame.image.load("imagenes/laser.png")
        self.imagenMisil = pygame.transform.flip(self.imagenMisil, True, False)
        self.rect = self.imagenMisil.get_rect()
        self.velocidadDisparo = 20
        self.rect.top=posY
        self.rect.left=posX
    #funcion para determinar el desplazamiento del misil
    def recorrido(self):
        self.rect.left=self.rect.left+self.velocidadDisparo
    #funcion para dibujar el misil
    def dibujar(self,superficie):
        superficie.blit(self.imagenMisil,self.rect)
