#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Menú de ciclos.

# Descripción:  Muestra un menu para acceder a los diferentes ejercicios.

#Importar funciones
import pygame
from math import *
from random import *

# Dimensiones de la pantalla
ancho = 800
alto = 800

# Colores
blanco = (255,255,255)
negro = (0,0,0)

#Dibuja cuadrados y circulos
def a ():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(blanco)
        for i in range(1,400,10):
            pygame.draw.circle(ventana, negro,(ancho//2,ancho//2),i,1)
            pygame.draw.rect(ventana,negro,(i,i, ancho-(2*i),alto-(2*i)),1)
        pygame.display.flip()
        reloj.tick(10)
    pygame.quit()

#Dibuja parábolas
def b ():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    ALTERNO = (randint(0, 255))
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(blanco)
        for i in range(1, 400, 10):
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,i),(400+i,400),)
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,i),(400-i,400),)
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,800-i),(400+i,400),)
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,800-i),(400-i,400),)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Dibuja espiral
def c ():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    ALTERNO = (randint(0, 255))
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(blanco)
        for i in range(0, 400, 10):
            pygame.draw.line(ventana,negro,(400-i,400+i),(410+i,400+i),)
            pygame.draw.line(ventana,negro,(410+i,400+i),(410+i,390-i),)
            pygame.draw.line(ventana,negro,(410+i,390-i),(390-i,390-i),)
            pygame.draw.line(ventana,negro,(390-i,390-i),(390-i,410+i),)
        pygame.display.flip()
        reloj.tick(10)
    pygame.quit()

#Dibuja círculos
def d ():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False
    ALTERNO = (randint(0, 255))
    radio = 150
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(blanco)
        for i in range(0,12):
            angulo = (pi/6)*i
            x = int((cos(angulo))*150)
            y = int((sin(angulo))*150)
            pygame.draw.circle(ventana, negro, (400+x,400+y),radio,1)
        pygame.display.flip()
        reloj.tick(10)
    pygame.quit()

#Aproximación
def Pi(numero):
        piCuad = 0
        for i in range(1, numero + 1):
            piCuad += (1 / (i ** 4))
        pi = sqrt((piCuad * 90))
        return pi

#numeros Divisibles
def NumerosDivi ():
    numerosD = 0
    for i in range(1000,9999):
        resultado = i % 17
        if resultado == 0:
            numerosD += 1
    return numerosD

#Pirámides de numeros
def Piramides ():
    numeroo = 1
    for i in range (1,10):
        resultado = (numeroo * 8) + i
        print(numeroo, "* 8 +",i,"=",resultado)
        numeroo = (numeroo * 10)+(i+1)
    print("")
    numeroo = 1
    for i in range (1,10):
        resultado = numeroo * numeroo
        print(numeroo, "*", numeroo, "=", resultado)
        numeroo = (numeroo*10)+1

#Menu
def main():
    print("Tarea 5. Seleccione qué te gustaría hacer" 
          "\n" 
         " 1. Dibujar cuadros y círculos "
          "\n"
          " 2. Dibujar espiral "
          "\n" 
          " 3. Dibujar círculos"
          "\n" 
          " 4. Dibujar parábolas "
          "\n" 
          " 5. Aproximar PI "
          "\n" 
          " 6. Contar divisibles entre 17 "
          "\n"    
          " 7. Imprimir pirámides de números"
          "\n"
          " 0. Salir "
          "\n")
    elegir = int(input(" ¿Qué te gustaría hacer? "))
    salir = False
    while not salir:
        if elegir == 0:
            salir=True
            quit()
        elif elegir == 1:
            a()
        elif elegir ==2:
            c()
        elif elegir ==3:
            d()
        elif elegir ==4:
            b()
        elif elegir ==5:
            respuesta = int(input("Escriba el numero que gustes: "))
            pi = Pi(respuesta)
            print(pi)
        elif elegir ==6:
            resultado = NumerosDivi()
            print(resultado)
        elif elegir ==7:
            Piramides()
        else:
            print("El número es invalido, intenta con otro")
        elegir=int(input(" ¿Qué te gustaría hacer? "))

main()