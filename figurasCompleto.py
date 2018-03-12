#Autor: Diana Patricia Aguilar Martínez
#Descripción: Tarea 5 - menu de figuras y  numeros


import pygame

import math

import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]. Paleta de colores.
NEGRO = (0,0,0)

def dibujarEspiral():

    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range(0,400,10):

            #horizontales abajo:
            pygame.draw.line(ventana, NEGRO, (ANCHO-x, ALTO-x),(0+x, ALTO-x), 1)

            #Vertical Izquierda:
            pygame.draw.line(ventana,NEGRO,(0+x, ALTO-x),(0+x,10+x),1)

            #Horizontal Arriba
            pygame.draw.line(ventana, NEGRO, (0+x,10+x), (ANCHO-(x+10), 10 + x), 1)

            #derecha arriba
            pygame.draw.line(ventana, NEGRO, (ANCHO-x, ALTO-x), (ANCHO-x, 10 + x-10),1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(30)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarArco():

    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Cambio de color:
        RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        #Dibujo de parábolas:
        for y in range(0, 400, 10):#Separación de 10 pixeles. 40 línes generadas
            RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))

            #Cuadrante 1=
            pygame.draw.line(ventana, RANDOM, (ANCHO // 2 + y, ALTO // 2), (ALTO // 2, y), 1)
            #Cuadrante 2=
            pygame.draw.line(ventana, RANDOM, (ANCHO//2 - y, ALTO//2),(ALTO//2,y),1)
            # Cuadrante 3=
            pygame.draw.line(ventana, RANDOM, (ANCHO // 2, ALTO - y), (ANCHO // 2 - y, ALTO // 2), 1)
            #Cuadrante 4=
            pygame.draw.line(ventana, RANDOM, (ANCHO//2, ALTO-y), (ANCHO//2+y, ALTO//2), 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(30)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarFlor():
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar patrón de círculos.
        for r in range(1, 13,1):  # El ángulo máximo
            pygame.draw.circle(ventana, NEGRO, (
            int((math.cos(r * math.pi / 6) * 150) + ANCHO // 2), int((math.sin(r * math.pi / 6) * 150) + ALTO // 2)),(150), 1)# Se multiplica por pi
        pygame.display.flip()  # Actualiza trazos
        reloj.tick(60)  # 40 fps

    pygame.quit()  # termina pygame


def dibujarCirculoCuadrado():

        pygame.init()  # Inicializa pygame
        ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
        reloj = pygame.time.Clock()  # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
        termina = False  # Bandera para saber si termina la ejecución

        while not termina:
            # Procesa los eventos que recibe
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                    termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

            for l in range(1, 400, 10):
                # DibujarCírculo
                pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), y, 1)
                # DibujarCuadrado
                pygame.draw.rect(ventana, NEGRO, (l, l, ANCHO - y * 2, ALTO - l * 2), 1)

            pygame.display.flip()  # Actualiza trazos
            reloj.tick(60)  # 40 fps

        pygame.quit()  # termina pygame

def imprimirPiramides():

    #Para columna del 8:
    mas = 1
    for p in range(1,10,1):
        r = mas * 8 + p #Primer resultado.
        print(mas, "* 8 +", p, "=", r) #Imprime el primer resultado.

        mas = (mas * 10) + (p+1)#El valor del incremento cambia.
    print("---------------------------------")

    #Para columna del 8:
    mas2=1

    for p2 in range(1,10,1):
        r2 = mas2*mas2 #Primer resultado.
        print(mas2,"*",mas2, "=", r2) #Imprime el primer resultado.

        mas2 = (mas2 * 10) + (1)#El valor del incremento cambia.

def calcularDivisibles():
        d = 0
        for x in range(1000, 10000, 1): #Comienza desde el 1000 para los numeros de 4 dígitos.

            if x % 17 == 0:
                d += 1

        return d

def aproximarPI(valor):
    incremento=0 #Contador

    for x in range (1,valor+1):
        incremento=incremento+(1/x**2)
    pi=(incremento*6)**(1/2)

    return pi

def main():

    print("Tarea 5. Seleccione qué quiere hacer:")

    print("""
    1. Dibujar cuadros y círculos
    2. Dibujar espiral
    3. Dibujar círculos
    4. Dibujar parábolas
    5. Aproximar PI
    6. Contar divisibles entre 17
    7. Imprimir pirámides de números
    0. Salir""")

    print("")
    seleccion=int(input("¿Qué desea hacer?:"))
    print("---------------------------------")

    while seleccion>=0:
        if seleccion==1:
            dibujarCirculoCuadrado()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 2:
            dibujarEspiral()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion==3:
            dibujarFlor()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 4:
            dibujarArco()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion == 6:

            print("Número de divisibles entre 17 es:", calcularDivisibles())

            seleccion = int(input("¿Qué desea hacer?:"))

            print("---------------------------------")


        elif seleccion == 5:

            pi = int(input("Ingresa el rango de pi:"))

            print("PI vale:", aproximarPI(pi))

            seleccion = int(input("¿Qué desea hacer?:"))

            print("---------------------------------")
        elif seleccion==7:
            imprimirPiramides()
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")



        elif seleccion>=8:
            print("Selecciones un número del 1 al 7.")
            print("")
            seleccion = int(input("¿Qué desea hacer?:"))
            print("---------------------------------")

        elif seleccion==0:
            print("El programa finalizó, vuelva pronto")
            break

main()