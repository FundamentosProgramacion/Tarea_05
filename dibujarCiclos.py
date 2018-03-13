#Jossian Abimelec Garcia Quijano
#ejecuta la funcion que pida


import pygame
import math
import random
from random import randint

Ancho = 800
Alto = 800
Azul = (33, 81, 238)
BLANCO = (255, 255, 255)

def dibujar():

    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        #for x in range(,10):



        for x in range (10,400,10):
            pygame.draw.circle(ventana, Azul, (Ancho//2, Alto//2),x, 1)
            pygame.draw.rect(ventana, Azul, (400-x, 400-x ,2*x,2*x), 1)






        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def aproxPI(x):
    Suma = 0

    for fraccion in range(1, x + 1):
        Suma += (1 / (fraccion ** 4))
    pi = ((Suma) * 90) ** 0.25
    return pi

def divisores():
    suma=0
    for numeros in range(1000, 10000):
        if numeros%17==0:
            suma+=1
    return suma

def piramide():
    x=0
    y=0
    for contador in range(1,10):
        y=(y*10)+contador
        r=y*8+contador
        print(y,"*",8,"+",contador,"=",r)

    for contador in range(1, 10):
        x=(x*10)+1
        r=x*x
        print(x,"*",x,"=",r)


def dibujarespiral():
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))  # ventana de dibujo
    reloj = pygame.time.Clock()  # limita los fps
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)  # borrar

        for a in range(0, 400, 10):
            pygame.draw.line(ventana, Azul, (Ancho - a, Alto - a), (0 + a, Alto - a), 1)
            pygame.draw.line(ventana, Azul, (0 + a, Alto - a), (0 + a, 10 + a))
            pygame.draw.line(ventana, Azul, (0 + a, 10 + a), (Ancho - (a + 10), 10 + a), 1)
            pygame.draw.line(ventana, Azul, (Ancho - a, Alto - a), (Ancho - a, 10 + a - 10), 1)
        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()


def dibujarparabolas():
    pygame.init()  # inicia
    ventana = pygame.display.set_mode((Ancho, Alto))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for p in range(0, 400, 10):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            pygame.draw.line(ventana, color, (Ancho // 2 + p, Alto // 2), ( Alto // 2, p), 1)
            pygame.draw.line(ventana, color, (Ancho // 2 - p, Alto //2), (Alto // 2 , p), 1)

            pygame.draw.line(ventana, color, (Ancho // 2, Alto - p), (Ancho // 2 - p, Alto // 2), 1)
            pygame.draw.line(ventana, color, (Ancho // 2, Alto - p), (Ancho // 2 + p, Alto // 2) ,1)
        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()


def dibujarcircuilos():
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for r in range(1, 13,1):
            pygame.draw.circle(ventana, Azul, (int((math.cos(r * math.pi / 6) * 150) + Ancho // 2),int((math.sin(r * math.pi / 6) * 150) + Alto // 2)),(150), 1)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

def main():
    eleccion=int(input("Seleccione qué quiere hacer:\n1. Dibujar cuadros y círculos \n2. Dibujar parábolas \n3. Dibujar espiral \n4. Dibujar círculos \n5. Aproximar Pi \n6. Contar divisibles entre 17 \n7. Imprimir pirámides de números \n 0. Salir \nQué desea hacer? "))
    if eleccion ==1:
        dibujar()
    elif eleccion ==2:
        dibujarparabolas()
    elif eleccion==3:
        dibujarespiral()
    elif eleccion==4:
        dibujarcircuilos()
    elif eleccion==5:
        print(aproxPI(10))

    elif eleccion==6:
        print(divisores())
    elif eleccion==7:
        piramide()
    else: print("has salido")



main()