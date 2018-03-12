# Autor: Andrés Reyes Rangel.
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
from math import *
from random import randint
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 255, 0)
NEGRO = (0, 0, 0)

#Dibuja Circulos y Cuadrados
def dibujarCirculosYCuadrados():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibuja cuadros y circulos
        colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
        for x in range(1, (ANCHO // 2) + 10, 10):
            pygame.draw.circle(ventana, colorAzar, (ANCHO // 2, ALTO // 2), x, 1)
        for x in range(10, (ANCHO // 2) + 1, 10):
            pygame.draw.rect(ventana, colorAzar, (ANCHO // 2 - x, ALTO // 2 - x, 2 * x, 2 * x), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Dibuja parábolas
def dibujarParabolas():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibuja cuadros y circulos
        for x in range(ANCHO // 2, ALTO + 1, 10):
            y = x - ANCHO / 2 + 10
            colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, colorAzar, (x - ANCHO // 2, ALTO // 2), (ANCHO // 2, y + ALTO // 2))
        for x in range(0, ANCHO // 2, 10):
            y = x - ANCHO / 2 + 10
            colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, colorAzar, (x + ANCHO // 2, ALTO // 2), (ALTO // 2, y + ALTO // 2))
        for x in range(0, (ANCHO // 2) + 1, 10):
            y = x - ANCHO / 2 + 10
            colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, colorAzar, (x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x))
        for x in range(0, (ANCHO // 2) + 1, 10):
            y = x - ANCHO / 2 + 10
            colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, colorAzar, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Dibuja el espiral
def dibujarEspiral():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        for x in range(0, (ANCHO // 2), 10):
            colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, colorAzar, (ANCHO + 3 - x, ALTO - x), (0 + x, ALTO - x), 1)
            pygame.draw.line(ventana, colorAzar, (0 + x, ALTO - x), (0 + x, 3 + x), 1)
            pygame.draw.line(ventana, colorAzar, (0 + x, 3 + x), (ANCHO - 6 - x, 3 + x), 1)
            pygame.draw.line(ventana, colorAzar, (ANCHO - 6 - x, 3 + x), (ANCHO - 6 - x, ALTO - 10 - x), 1)
        #pygame.draw.line(ventana, colorAzar, (ANCHO // 2, ALTO // 2), (404, 400))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame



#Dibuja Cirulos
def dibujarCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        for x in range(0, 360, 30):
            cos = (math.cos(x * math.pi / 180))
            sen = (math.sin(x * math.pi / 180))
            colorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.circle(ventana, colorAzar, (int(ANCHO / 2 + (150 * cos)), int(ALTO / 2 + (150 * sen))), 150, 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame

#Aproximación de PI
def aproximarPi(n):
    suma = 0
    for d in range (1,n+1):
        valorAproximado = 1/(d**4)
        suma += valorAproximado
    PI = (suma*90)**(1/4)
    return PI

#Cuenta los divisbles entre 17
def calcularDivisibles():
    sumaDivisores = 0
    for numero in range(1000,10000):
        if numero%17==0:
            sumaDivisores += 1
    return sumaDivisores

#Imprime piramides de números.

def imprimirPiramides():
    piramide1 = ""
    linea = 0
    for i in range(1,10):
        linea += int("1"*i)
        resultado = linea*8+i
        piramide1 = str(piramide1) + ("%d * 8 + %d = %d\n" % (linea, i, resultado))
    print(piramide1)
    piramide2 = ""
    linea2 = 0
    for k in range(1, 10):
        linea2 += int("1"*k)
        resultado = linea2 * linea2
        piramide2 = str(piramide2) + ("%d * %d = %d\n" % (linea2, k, resultado))
    print(piramide2)


def main():
    print("\nElija uno de los siguientes programas")
    print("1. Dibujar cuadros y circulos.")
    print("2. Dibujar parábolas.")
    print("3. Dibujar espiral.")
    print("4. Dibujar circulos.")
    print("5. Aproximar PI.")
    print("6. Contar divisibles entre 17.")
    print("7. Imprimir pirámides de números.")
    print("0. Salir.")
    print("-------------------------------")
    decision = int(input("¿Qué programa desea ejecutar?\nOpción: "))

    while decision != 0:
        if decision > 7:
            print("Porfavor elija una de las opciones anteriores")
        elif decision == 1:
            dibujarCirculosYCuadrados()
        elif decision == 2:
            dibujarParabolas()
        elif decision == 3:
            dibujarEspiral()
        elif decision == 4:
            dibujarCirculos()
        elif decision == 5:
            n = int(input("Ingrese la aproximación a PI: "))
            pi=aproximarPi(n)
            print("La aproximación de PI es:", pi)
        elif decision == 6:
            calcularDivisibles()
            print("El número de divisibles entre 17 es:", calcularDivisibles())
        elif decision == 7:
            imprimirPiramides()
        elif decision == 0:
            print("Fin del programa")
        print("-------------------------------")
        decision = int(input("¿Qué desea hacer?\nOpción: "))
        print("-------------------------------")
    print("Fin del programa")
main()