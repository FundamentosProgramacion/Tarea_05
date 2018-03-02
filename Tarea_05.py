# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_05: Ciclos FOR

# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
import random
import getpass
from math import *
user = getpass.getuser()
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

def encontrarDiv():
    contador = 0
    for numero in range(1000, 10000):
        if numero % 17 ==0:
            contador+= 1
    return contador

def calcularPiramides():
    acumulador = 1
    acumulador2 = 0
    for numero in range(1, 10):
        total2 = acumulador**2
        print('%d * %d = %d' % (acumulador, acumulador, total2))
        total = 10**numero
        acumulador += total
    for numero in range(1, 10):
        acumulador2 += numero
        total2 = acumulador2 * 8 + numero
        print('%d * 8 + %d = %d'% (acumulador2, numero, total2))
        acumulador2 *= 10

def aproximarPI(divisor):
    acumulador = 0
    for numero in range(1, divisor):
        aproximado = 1/(numero**4)
        acumulador+= aproximado
    pi = (acumulador+90)**(1/4)
    return '\n-La aproximación de PI con %d valores es: %f\n' % (divisor, pi)

def drawCircleANDRect(ventana):
    for numero in range(1, ANCHO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), (numero), 1)
    for numero in range(1, ANCHO, 10):
        pygame.draw.rect(ventana, NEGRO, (numero, numero, ANCHO-2 * numero, ALTO-2 * numero), 1)

def dibujarArco(ventana):
    colorAzar = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for x in range(ANCHO//2, ANCHO, 10):
            y = x - ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x-ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)
    for x in range(ANCHO//2, ANCHO, 10):
            y = -x + ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x-ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)
    for x in range(0, ANCHO//2, 10):
            y = x - ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x+ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)
    for x in range(0, ANCHO//2, 10):
            y = -x + ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x+ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)

def dibujarCirculos(ventana):
    for numero in range(1, 361, 30):
        rad = int(radians(numero))
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), 150, 1)

def dibujarEspiral():
    pass

# Estructura básica de un programa que usa pygame para dibujar

def dibujar(opcion):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()
    # Inicializa el motor de pygame
         # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        #drawCircleANDRect(ventana)
        if opcion == 1:
            drawCircleANDRect(ventana)
        elif opcion == 2:
            dibujarArco(ventana)
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos(ventana)


        #dibujarArco(ventana)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    print('Bienvenido/a %s.'% user)
    print('Menu:\n'
          '1. Dibujar cuadros y círculos\n'
          '2. Dibujar parábolas\n'
          '3. Dibujar espiral\n'
          '4. Dibujar círculos\n'
          '5. Aproximar PI\n'
          '6. Contar divisibles entre 17\n'
          '7. Imprimir pirámide de números\n'
          '0. Salir\n')
    opcion = int(input('Que deseas ejecutar? '))
    while opcion != 0:
        if opcion >= 1 and opcion <=4:
            dibujar(opcion)
        elif opcion == 5:
            lentoDeAMadres = int(input('Aproximación de PI.\n'
                                       'Teclea el valor del divisor.\n'
                                       '(Mientras más grande sea, más se va a tardar): '))
            print(aproximarPI(lentoDeAMadres))
        elif opcion == 6:
            encontrarDiv()
        elif opcion == 7:
            print(calcularPiramides())
        print('Bienvenido/a %s.' % user)
        print('Menu:\n'
              '1. Dibujar cuadros y círculos\n'
              '2. Dibujar parábolas\n'
              '3. Dibujar espiral\n'
              '4. Dibujar círculos\n'
              '5. Aproximar PI\n'
              '6. Contar divisibles entre 17\n'
              '7. Imprimir pirámide de números\n'
              '0. Salir\n')
        opcion = int(input('Que deseas ejecutar? '))
    else:
        pass



main()