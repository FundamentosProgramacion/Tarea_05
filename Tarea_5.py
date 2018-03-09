# Autor: José Francisco Murillo Lozano A01374561
# Resuelve el problema de la Tarea_05 de 'Fundamentos de Programación'

import pygame
from math import cos
from math import sin
from math import radians

def dibujarCyC():
    ANCHO = 800
    ALTO = 800

    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        for radio in range(0, ANCHO//2, 10):
            pygame.draw.rect(ventana, NEGRO, (400-radio, 400-radio, radio*2, radio*2), 1)
            if radio == 0:
                radio = 1
            pygame.draw.circle(ventana, NEGRO, (400, 400), radio, 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarArco(ventana, ANCHO, ALTO, NEGRO):

    #Cuadrante 1
    for x in range(0, ANCHO//2, 10):
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2, ALTO // 2 - x), (ANCHO - x, ALTO // 2), 1)

    #Cuadrante 2
    for x in range(0, ANCHO//2, 10):
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + x, ALTO // 2), (ANCHO // 2, ALTO - x), 1)

    #Cuadrante 3
    for x in range(0, ANCHO//2, 10):
        pygame.draw.line(ventana, NEGRO, (0 + x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x), 1)

    #Cuadrante 4
    for x in range(0, ANCHO//2, 10):
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2, 0 + x), (ANCHO // 2 - x, ALTO // 2), 1)


def dibujarParabolas():
    ANCHO = 800
    ALTO = 800

    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarArco(ventana, ANCHO, ALTO, NEGRO)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarEspiral():
    ANCHO = 800
    ALTO = 800

    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        coor = 0
        x = 400
        y = 400
        for value in range(5, ANCHO-10, 5):
            relacion = coor % 4
            if relacion == 0:
                pygame.draw.line(ventana, NEGRO, (x, y), (x + value, y))
                x += value
            if relacion == 1:
                pygame.draw.line(ventana, NEGRO, (x, y), (x, y - value))
                y -= value
            if relacion == 2:
                pygame.draw.line(ventana, NEGRO, (x, y), (x - value, y))
                x -= value
            if relacion == 3:
                pygame.draw.line(ventana, NEGRO, (x, y), (x, y + value))
                y += value

            pygame.draw.line(ventana, NEGRO, (400,400), (405,400))
            coor+=1

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarCirculos():
    ANCHO = 800
    ALTO = 800

    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras

        xi = 400
        yi = 400
        for num in range(12):
            angulo = radians(num * 30)
            xReal = int(xi + sin(angulo) * 150)
            yReal = int(yi + cos(angulo) * 150)
            pygame.draw.circle(ventana, NEGRO, (xReal, yReal), 150, 1)


        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def aproximarPi(valor):
    y = 0
    for num in range(1, valor+1):
        y = y + (1/(num**4))
    return y


def contarDivisibles():
    cont = 0
    for num in range(1000, 10000, 1):
        if num%17 == 0:
            cont += 1
    return cont


def imprimirPiramides():
    x = 0
    y = 0
    print('\n\n')
    for value in range (1, 10):
        x = x*10 + value
        pira1 = x*8 + value
        print(pira1)
    print('\n')
    for value in range(9):
        y = y*10 + 1
        pira2 = y**2
        print(pira2)


def main():
    print("Tarea 5. Seleccione qué quiere hacer. \n1. Usar Pygame \n2. Aproximar PI \n3. Contar divisibles entre 17 \n4. Imprimir pirámides de números \n0. Salir \n¿Qué desea hacer?")
    funcion = int(input("Eleccion: "))
    if funcion != 0:
        if funcion == 1:
            print("Seleccione ejercicio de PyGame desea correr. \n1. Dibujar cuadros y círculos \n2. Dibujar parábolas \n3. Dibujar espiral \n4. Dibujar círculos \n0. Salir")
            funcion = int(input("Eleccion: "))
            while funcion != 0:
                if funcion == 1:
                    dibujarCyC()
                if funcion == 2:
                    dibujarParabolas()
                if funcion == 3:
                    dibujarEspiral()
                if funcion == 4:
                    dibujarCirculos()
                funcion = int(input("Eleccion: "))
        if funcion == 2:
            valor = int(input("Valor del divisor máximo para aproximar Pi: "))
            print('El valor aproximado de Pi dados los', valor, 'denominadores es:', aproximarPi(valor))
        if funcion == 3:
            print(contarDivisibles())
        if funcion == 4:
            imprimirPiramides()


main()