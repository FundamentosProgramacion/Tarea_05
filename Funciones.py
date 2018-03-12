# Autor: Guillermo Adrian Urbina Aguiñiga
# Programa para dibujar diversas figuras y calculos

import turtle
import pygame
import sys
import math
import random
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

BLANCO = (255,255,255)
# Estructura básica de un programa que usa pygame para dibujar
def dibujar(parametro):
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
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)

        if parametro == 1:
            distanciaV = 0
            n = 0
            i = 0
            while distanciaV <= ALTO//2  :
                distanciaV = distanciaV + 10
                n = n + 1
                i = i + 1
                pygame.draw.circle(ventana, (randint(0,255), randint(0,255), randint(0,255)), (ANCHO//2, ALTO//2), distanciaV, 1)
                pygame.draw.rect(ventana, (randint(0,255), randint(0,255), randint(0,255)),(distanciaV, distanciaV  , (ANCHO-distanciaV*2), (ALTO-distanciaV*2)) , 1)
                pygame.display.flip()   # Actualiza trazos)
                reloj.tick(40)          # 40 fps

        elif parametro == 2:
            distancia = 0
            while distancia <= ALTO//2:
                distancia = distancia + 1
                pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (0+distancia,ALTO//2),(ANCHO//2, ALTO//2-distancia), 1)
                pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (0+distancia,ALTO//2),(ANCHO//2, ALTO//2+distancia), 1)
                pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (ANCHO-distancia, ALTO//2),(ANCHO//2, ALTO//2-distancia), 1)
                pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (ANCHO-distancia, ALTO//2),(ANCHO//2, ALTO//2+distancia), 1)
                pygame.display.flip()   # Actualiza trazos)
                reloj.tick(40)          # 40 fps

        elif parametro == 3:
            distancia = 0
            turtle.setup(800, 800)
            while distancia <= 799:
                distancia = distancia + 10
                turtle.forward(distancia)
                turtle.left(90)
                distancia = distancia + 5
                turtle.forward(distancia)
                turtle.left(90)


        elif parametro == 4:
            radio = 150
            for angulo in range(0, 360+1 , 30):
                a = math.radians(angulo)
                cordenadax = int(radio * math.cos(a))
                cordenaday = int(radio * math.sin(a))
                pygame.draw.circle(ventana, (randint(0,255), randint(0,255), randint(0,255)), ((ANCHO//2+cordenadax), (ALTO//2-cordenaday)), 150, 1)
                pygame.display.flip()   # Actualiza trazos)
                reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame

def calcular(parametro):
    if parametro == 5:
        numero = int(input("Número: "))
        contar = 1
        for i in range(1,numero):
            resultado = 1/contar**4
            contar >= resultado
            pi = (contar*90)**(1/4)
            print (pi)

    elif parametro == 6:
        for i in range(1000, 10000):
            a = i % 17
            if a == 0:
                print (i)

    elif parametro == 7:
        n = 0
        l = 0
        k = 0
        for i in range(1,10):
            l = l + 1
            n = n * 10 + l
            nn = n * 8 + l
            print(n, " * 8 +", l, " = ", nn)

        for p in range(1,10):
            k = k *10 + 1
            kk = k * k
            print(k, "*", k, "=", kk)




def main():
    print("1. Dibujar cuadros y circulos")
    print("2. Dibujar Parábolas")
    print("3. Dibujar Espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 17")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("¿Qué desea hacer?")
    parametro = int(input("Dame el número de resultado que quieres: "))
    calcular(parametro)
    dibujar(parametro)


main()


































