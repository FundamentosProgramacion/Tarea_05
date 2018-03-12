##Autor: David Medina Medina A01653311
##Tarea 5: Dibujar con pygame y usar ciclos For.

import pygame
from random import *
from math import *

ancho = 800
alto = 800
blanco = (255,255,255)
rojo = (255,0,0)
azul = (28,79,114)
negro = (0,0,0)
b = ancho//2
c = alto//2
p = 10
n = 90

def dibujarCiculosYRectangulos():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(blanco)
        dibujarCuadrosYCirculos(ventana,p)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujarCuadrosYCirculos(v,p):
    for x in range (390,0,-10):
        pygame.draw.circle(v, negro, (b, c), p // 2, 2)
        pygame.draw.rect(v, negro, (x+5, x+5, p, p), 2)
        p = p+20

def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(blanco)
        dibujarArco(ventana,)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujarArco(v):
    for x in range(0, 410, 10):
        cA = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.line(v, cA, (b,alto-x),(b-x,c))
        pygame.draw.line(v, cA, (b,alto-x), (b+x,c))
        pygame.draw.line(v, cA, (b, x), (b-x, c))
        pygame.draw.line(v, cA, (b, x), (b+x, c))

def dibujarEspirales():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(blanco)
        dibujar_espirales(ventana)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujar_espirales(v):
    for x in range (0,b,10):
        pygame.draw.line(v, negro, (b-x,c+x),(b+x+10,c+x),2)
        pygame.draw.line(v, negro, (b+x+10,c+x),(b+x+10,c-x-10),2)
        pygame.draw.line(v, negro, (b+x+10,c-x-10),(b-x-10,c-x-10),2)
        pygame.draw.line(v, negro, (b-x-10,c-x-10),(b-x-10, c+x+10),2)

def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(blanco)
        dibujar_circulos(ventana)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujar_circulos(v):
    for x in range(1,13):
        r = 150
        a = pi/6* x
        cc = int((cos(a))*r)
        sc = int((sin(a))*r)
        pygame.draw.circle(v, negro, (b+ cc, c+ sc),r, 2)

def calcularPi(n):
    a = 0
    for x in range(1, n+1):
        a = a+1/x**4
    return a

def divisibles():
    a=0
    for x in range (1000,10000):
        r =  x%17
        if r ==0:
            a+=1
    return a

def piramides():
    p1=0
    p2=0
    mp1=8
    for x in range (1,10):
        p1 = x+p1*10
        m1 = p1*mp1+x
        print(p1, "*", mp1, "+",x, "=", m1)
    print ("""
        """)
    for uno in range(9):
        p2= p2*10+1
        m2= p2**2
        print(p2, "*", p2, "=", m2)
    return ""

def main():
    opcion = 0

    while opcion != 8:

        print("""Seleccionar opciones solamente entre 1 y 8! 
Seleccione 1 para dibujar cuadros y circulos.
Seleccione 2 para dibujar parabolas.
Seleccione 3 para dibujar espiral.
Seleccione 4 para dibujar circulos.
Seleccione 5 para aproximar Pi.
Seleccione 6 para contar divisibles entre 17.
Seleccione 7 para imprimir piramides de numeros.
Seleccione 8 para Salir.""")
        opcion = int(input("Seleccionar opcion: "))

        if opcion == 1:
            dibujarCiculosYRectangulos()
        if opcion == 2:
            dibujarParabolas()
        if opcion == 3:
            dibujarEspirales()
        if opcion == 4:
            dibujarCirculos()
        if opcion == 5:
            calcularPi(n)
            print("Aproximacion al valor de Pi:",(calcularPi(n)))
        if opcion == 6:
            print ("Total de numeros de 4 digitos divisibles entre 17:",(divisibles()))
        if opcion == 7:
            print (piramides())
        if opcion ==8:
            print ("""Selecciono salir. Adios!
Si quiere voler al programa debe reiniciarlo.""" )
            break
main()
