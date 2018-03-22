# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_05: Ciclos FOR

# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
import random
import getpass
import math
user = getpass.getuser()
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

def piramide2(numero, acumulador):
    total = acumulador * 8 + numero
    return '%d * 8 + %d = %d' % (acumulador, numero, total)

def piramide1(x):
    total = x**2
    return ('%d * %d = %d' % (x, x, total))

def encontrarDiv():                   #encuentra los divisores de 17 en un rango de 1000 a 9999 (solo los numeros de 4 digitos)
    contador = 0
    for numero in range(1000, 10000):
        if numero % 17 ==0:
            contador+= 1
    return contador
'''
def calcularPiramides():        #imprime una serie de pirámides
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
'''
def aproximarPI(divisor):       # aproxima PI con los calores integrados
    acumulador = 0
    for numero in range(1, divisor):
        aproximado = 1/(numero**4)
        acumulador+= aproximado
    pi = (acumulador*90)**(1/4)
    return '\n-La aproximación de PI con %d valores es: %f\n' % (divisor, pi)

def drawCircleANDRect(ventana):     # dibuja una serie de circulos y cuadrados entrelazados
    for numero in range(1, ANCHO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), (numero), 1)
    for numero in range(1, ANCHO, 10):
        pygame.draw.rect(ventana, NEGRO, (numero, numero, ANCHO-2 * numero, ALTO-2 * numero), 1)

def dibujarArco(ventana):       # dibuja unas parabolas que cambian de color 40 veces por segundo
    colorAzar = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for x in range(ANCHO//2, ANCHO+1, 10):
            y = x - ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x-ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)
    for x in range(ANCHO//2, ANCHO+1, 10):
            y = -x + ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x-ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)
    for x in range(0, ANCHO//2+1, 10):
            y = x - ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x+ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)
    for x in range(0, ANCHO//2+1, 10):
            y = -x + ANCHO//2
            pygame.draw.line(ventana, colorAzar, (x+ANCHO//2, ALTO//2), (ANCHO//2, y+ALTO//2), 1)

def dibujarCirculos(ventana):  #dibuja la flor de circulos en la ventana
    for numero in range(1, 14):
        angulo = (math.pi/6)*numero
        y = int(math.sin(angulo)*150)
        x = int(math.cos(angulo)*150)
        x += 400
        y +=400
        pygame.draw.circle(ventana, NEGRO, (x, y), 150, 1)


def dibujarEspiral(ventana):            # dibuja una espiral en la pantalla
    for numero in range(0, ANCHO//2, 10):       #lado inferior
        pygame.draw.line(ventana, NEGRO, (ANCHO + 3 - numero, ALTO - numero), (0+numero , ALTO -numero), 1)
    for numero in range(0, ANCHO//2, 10):        # lado superior
        pygame.draw.line(ventana, NEGRO, (0+numero, 3+numero), (ANCHO - 6 - numero, 3 + numero), 1)
    for numero in range(0, ALTO//2, 10):        # lado izquierdo
        pygame.draw.line(ventana, NEGRO, (0 + numero, ALTO - numero), (0+ numero, 3 + numero), 1)
    for numero in range(0, ALTO//2, 10):        # lado derecho
        pygame.draw.line(ventana, NEGRO, (ALTO - 6 - numero, 3 + numero), (ALTO - 6 - numero, ALTO - 10 - numero))

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
            dibujarEspiral(ventana)
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
            acumulador = 0
            acumulador2 = 0
            for numero in range(1, 10):
                acumulador2 *= 10
                acumulador2 += numero
                print(piramide2(numero, acumulador2))
            print('\n')
            for numero in range(9):
                acumulador *= 10
                acumulador += 1
                print(piramide1(acumulador))
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
        print('Apagando...\n\nAdios %s.'%user)



main()