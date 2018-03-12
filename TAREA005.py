#Autor: Ricardo Cornejo Lozano
#Programa que contiene 7 programas para escoger. Entre este programa podras dibujar figuras geometricas, aproximarPi, imprimir piramides de numeros y calcular cuantos numeros de pueden dividir entre 17.
import random
from math import*
import math
import pygame

ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO =(0,0,0)


def CirculosYcuadros():
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

        # Dibujar, aquí haces todos los trazos que requieras

        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        for radio in range(1, ANCHO, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio , 1)
        for width in range (1, ANCHO,10):
                pygame.draw.rect(ventana, NEGRO, (ANCHO//2,ALTO//2, width,width), 1)
                pygame.draw.rect(ventana, NEGRO, (ANCHO // 2, ALTO // 2, -width, -width), 1)
                pygame.draw.rect(ventana, NEGRO, (ANCHO // 2, ALTO // 2, width,-width), 1)
                pygame.draw.rect(ventana, NEGRO, (ANCHO // 2, ALTO // 2, -width, width), 1)


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame




def dibujarEspiral():
    import turtle
    for longitud in range(5, 800, 10):
        turtle.forward(longitud)
        turtle.left(90)
        turtle.forward(longitud)
        turtle.left(90)

def dibujarCirculo(ventana, m):

    for alfa in range (0, 360,15): #grados
        Rad = radians(alfa)
        r = m * cos(Rad)
        x = int(r*cos(Rad)) + ANCHO//3
        y = ALTO//2 +int(r*sin(Rad))
        colorAzar = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(ventana, colorAzar, (x,y), 150,1)


def dibujar():
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
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarCirculo(ventana, 300)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def aproximarPI(n):
    suma = 0 #sumatoria de las fracciones
    cf =1
    for d in range (1, n+1,2):
        if cf%2 ==1:
            suma += 1/d
        else:
            suma -= 1/d
        cf += 1
    print (4*suma)


def calcularDiv():
    count = 0
    for x in range (1000,9999):
        numero = x%17
        if numero == 0:
            count += 1

    resultado = count
    print(resultado)

def piramideDeUnos():
    for i in range(10):
        X = 1
        for j in range(i):
            X = X * 10 + 1
        print ("%d x %d = %d" % (X,X,X*X))

def piramideDe1a9():
    n=1
    mult = 8
    print ("%d x %d + %d = %d" % (n,mult,n,n*mult+n))

    for c in range(2,10):
        r = (str(n)+str(c))
        n = r
        resultado = (int(n)*8+int(c))
        print("%d x %d + %d = %d" % (int(n),8,int(c),int(resultado)))

def main():
    print("Tarea 05. Seleccione que quiere hacer.", "\n1.Dibujar cuadros y circulos","\n2.DibujarParabola", "\n3.Dibujar espiral", "\n4.Dibujar Circulos", "\n5.Aproximar PI", "\n6.Contar divisibles entre 17", "\n7.Imprimir piramide de unos", "\n8.Imprimir piramide de 1-9","\n0.Salir")
    seleccion= int(input("Que desea hacer?: "))
    if seleccion == 1:
        CirculosYcuadros()
    elif seleccion ==2:
        dibujarParabola()
    elif seleccion == 3:
        dibujarEspiral()
    elif seleccion ==4:
        dibujar()
    elif seleccion == 5:
        aproximarPI(100)
    elif seleccion ==6:
        calcularDiv()
    elif seleccion == 7:
        piramideDeUnos()
    elif seleccion ==8:
        piramideDe1a9()
    elif seleccion == 0:
        exit()



main()