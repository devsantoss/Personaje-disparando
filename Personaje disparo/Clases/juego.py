"""
@author: David s

"""
import pygame,sys
from pygame.locals import *
#importar la clase jugador
from jugador import *


#Variables
ANCHO=1000
ALTO=640
#Variable boolean
jugando = True

#funcion principal
def juego():
    pygame.init()
    colorTexto = (125,10,212)
    #texto indicativo
    fuente = pygame.font.SysFont('Arial',30)
    texto = fuente.render("Presione la barra espaciadora"+
                          "para disparar",0,colorTexto)

    ventana = pygame.display.set_mode((ANCHO,ALTO))
    #imagen de fondo
    fondo = pygame.image.load('imagenes/backg.png')
    
    #Titulo
    pygame.display.set_caption('Animacion personaje disparando')
    #crear objeto jugador
    personaje=Personaje()    

    #Ciclo del juego
    while True:
        #"dibuja" la imagen de fondo y el texto indicativo
        ventana.blit(fondo,(0,0))
        ventana.blit(texto,(300,100))
        personaje.dibujar(ventana)
        if len(personaje.listaDisparo)>0:
            for x in personaje.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.left<-10:
                    personaje.listaDisparo.remove(x)
        personaje.mover()
        for evento in pygame.event.get():
            if jugando == True:                
            #para cerrar con X
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                #eventos en que se utilizan teclas     
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        personaje.rect.left-=personaje.velocidad
                    elif evento.key == K_RIGHT:
                        personaje.rect.right+=personaje.velocidad
                    elif evento.key==K_SPACE:
                        x,y=personaje.rect.center
                        personaje.disparar(x,y)
        pygame.display.update()
#llamada a funcion principal
juego()
