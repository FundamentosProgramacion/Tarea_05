#Autor Karla Fabiola Ramirez Martinez
#Descripcion; Dibuja una espiral cuadrada


#Importamos las librerias necesarias
import pygame
from random import randint
import math
#Ancho y alto de la pantalla
ANCHO = 800
ALTO = 800
# Colores y lo que seria el centro
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
x = ANCHO // 2
y = ALTO // 2

#La funcion para la figura 1, Cuadrados y circulos
def dibujarCirculos_Cuadrados():
    pygame.init()#Con esto iniciamos Pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO)) #Dimensiones de la ventana
    reloj = pygame.time.Clock()
    termina = False
    #Esto nos dice que no acabara el proceso hasta que lo cierres
    while not termina:
        for evento in pygame.event.get(): #Procesa los eventos que recibe el programa
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        #Funcion para los rectangulos
        for espacio in range (2, ALTO+1, 10):
            pygame.draw.rect(ventana, NEGRO,(x - (espacio // 2), y - (espacio // 2), espacio, espacio), 1)
            #Primero va la ventana, color de la linea,area del rectangulo(Las cuatro esquinas), y el ancho, si tiene cero entonces es llenita

        #Funcion para loa circulos
        for espacio in range (1, (y)+ALTO//100, 10):
            pygame.draw.circle(ventana, NEGRO, (x, y), espacio, 1)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()

# Con esta función se puede dibujar una espiral cuadrada que abarca toda la pantalla
def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        #Funcion que va creando las lineas para darles forma de espiral
        for cambio in range(0, y, 10):
            #(Ventana,color,coordenadas,grosor)
            pygame.draw.line(ventana, NEGRO, ((x + 5) - cambio, y + cambio), ((x + 5) + cambio, y + cambio), 1)
            pygame.draw.line(ventana, NEGRO, ((x + 5) + cambio, y + cambio), ((x + 5) + cambio, (y - 5) - cambio), 1)
            pygame.draw.line(ventana, NEGRO, ((x + 5) + cambio, (y - 5) - cambio), ((x - 5) - cambio, (y - 5) - cambio), 1)
            pygame.draw.line(ventana, NEGRO, ((x - 5) - cambio, (y - 5) - cambio), ((x - 5) - cambio, (y + 10) + cambio), 1)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()

# Dibuja unos circulos formando una flor en el centro
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for separacion in range(0, 12):
            radio = 150
            angulo = (math.pi / 6) * separacion
            xC = int((math.cos(angulo)) * 150)
            yC = int((math.sin(angulo)) * 150)
            pygame.draw.circle(ventana, NEGRO, (x + xC, y + yC), radio, 1)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()

# Con esta funcion se puede dibujar una parabola que da forma a una estrella de colores
def dibujarParabolas_Color():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for cambio in range(0, y, 10):
            COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, COLOR, (cambio, y),(x, y + cambio))
            pygame.draw.line(ventana, COLOR, (ANCHO - cambio, y),(x, y + cambio))
            pygame.draw.line(ventana, COLOR, (ANCHO - cambio, y),(x, y - cambio))
            pygame.draw.line(ventana, COLOR, (cambio, y),(x, y - cambio))
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Funcion principal
def main():
    print("Seleccione qué quiere hacer.")
    print("     1. Dibujar cuadrados y circulos ")
    print("     2. Dibujar parábolas ")
    print("     3. Dibujar espiral")
    print("     4. Dibujar círculos")
    print("     0. Salir")
    opcion = 1
    #While que repite que quiere hacer
    while opcion > 0:
        opcion = int(input("Intoduzca opción: "))
        if opcion == 1:
            dibujarCirculos_Cuadrados()
            print(" ")
        elif opcion == 2:
            dibujarParabolas_Color()
            print(" ")
        elif opcion == 3:
            dibujarEspiral()

            print(" ")
        elif opcion == 4:
            dibujarCirculos()
            print(" ")
        elif opcion > 4:
            print("Elija un número válido.")
            print(" ")
    print("El programa ha finalizado.")

main()
