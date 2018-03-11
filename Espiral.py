#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Crear una espiral a partir de una función.

import pygame
import random

#Dimensiones de la pantalla
ANCHO=800
ALTO=800

#Colores
Rojo=(255,0,0)
Blanco=(255,255,255)
Negro=(0,0,0)
Verde=(0, 122, 0)



def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)

        for i in range(1, 400, 10): # Va 1, 11, 21, 31...
            pygame.draw.line(ventana,random.randint(0,255), (i,ALTO-i),(ANCHO-i,ALTO-i))
            pygame.draw.line(ventana, random.randint(0,255), (i, i), (i, ALTO - i))
            pygame.draw.line(ventana, random.randint(0,255), (ANCHO - (10 + i), i), (ANCHO - (10 + i), ALTO - (10 + i)))
            pygame.draw.line(ventana, random.randint(0,255), (i, i), (ANCHO - (10 + i), (i)))





        pygame.display.flip()
        reloj.tick(40)



def main():
    dibujarEspiral()

main()
