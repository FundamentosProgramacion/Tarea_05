import pygame
import random
from math import *
import math

#Dimensiones de la pantalla
ANCHO=800
ALTO=800

#Colores
Rojo=(255,0,0)
Blanco=(255,255,255)
Negro=(0,0,0)
Verde=(0, 122, 0)
radio=150

def dibujarCC():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)

        for n in range(1, 400, 10): # Va 1, 11, 21, 31...
            pygame.draw.line(ventana,Rojo, (n,ALTO-n),(ANCHO-n,ALTO-n))
            pygame.draw.line(ventana, Rojo, (n, n), (n, ALTO - n))
            pygame.draw.line(ventana, Rojo, (ANCHO - (10 + n), n), (ANCHO - (10 + n), ALTO - (10 + n)))
            pygame.draw.line(ventana, Rojo, (n, n), (ANCHO - (10 +n), (n)))
            pygame.draw.circle(ventana, Rojo, (ANCHO // 2, ALTO // 2), 400-n, 1)

        pygame.display.flip()
        reloj.tick(40)

def dibujarParabola():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(Negro)

        for i in range(1, 400, 10):
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i, ALTO / 2), (ANCHO / 2, i + ALTO / 2))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i, ALTO / 2), (ANCHO / 2, -i + ALTO / 2))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (ANCHO - i, ALTO / 2), (ANCHO / 2, ALTO / 2 + i))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO - i, ALTO / 2), (ANCHO / 2, ALTO / 2 - i))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)

        for i in range(1, 400, 10): # Va 1, 11, 21, 31...
            pygame.draw.line(ventana,random.randint(0,255), (i,ALTO-i),(ANCHO-i,ALTO-i))
            pygame.draw.line(ventana, random.randint(0,255), (i, i), (i, ALTO - i))
            pygame.draw.line(ventana, random.randint(0,255), (ANCHO - (10 + i), i), (ANCHO - (10 + i), ALTO - (10 + i)))
            pygame.draw.line(ventana, random.randint(0,255), (i, i), (ANCHO - (10 + i), (i)))





        pygame.display.flip()
        reloj.tick(40)

def dibujarCirculos():
    # Inicializa el motor de pygame
    pygame.init ()
    ventana = pygame.display.set_mode ( (ANCHO, ALTO) )  # Crea la ventana de dibujo
    reloj = pygame.time.Clock ()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get ():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill ( Blanco )

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        for i in range ( 0, 12 ):
            pygame.draw.circle ( ventana, Negro, (int ( ANCHO // 2 + radio * math.cos ( math.pi * i / 6 ) ),int ( ALTO // 2 + radio * math.sin ( math.pi * i / 6 ) )), radio, 1 )
        pygame.display.flip ()  # Actualiza trazos
        reloj.tick ( 40 )  # 40 fps

    # Después del ciclo principal
    pygame.quit ()  # termina pygame

def aproximarPi(numero):
    suma=0
    for i in range(1,numero+1):
        serie=1/i**2
        suma=suma+serie
    aproximacion=suma
    ValorExacto=math.pi**2/6
    print("su aproximacion es de:",aproximacion)
    print("------------------------------------")
    print("El valor exacto de Pi**2/6 es de:",ValorExacto)

def calcularNumeros():
    n=0
    for i in range(1000,10001):
        if i%17==0:
            n+=1
    return n

def calcularPiramide():
    numero=0
    viii=8
    for i in range (0,10):
        numero= numero* 10+ i
        total=numero*viii+i
        print(numero,"*",viii,"+",i,"=",total)
    print("============================================")
    UNo = 0

    for i in range(0, 10):
        UNo = UNo * 10 + (i + (1 - i))
        total = UNo**2
        print(UNo, "*", UNo, "=", total)


def main():
    print ( """
        0. Salir
        1. Cuadros y Círculos
        2. Parábola
        3. Espiral   
        4. Círculos
        5. Aproximar pi
        6. Contar divisibles entre 17
        7.Pirámide de número

       """ )

    print ( "" )
    seleccion = int ( input ( "¿Qué desea hacer?:" ) )

    while seleccion >= 0:
        if seleccion == 1:
            dibujarCC()
            seleccion = int ( input ( "¿Qué desea hacer?:" ) )

        elif seleccion == 2:
            dibujarParabola()
            seleccion = int ( input ( "¿Qué desea hacer?:" ) )

        elif seleccion == 3:
            dibujarEspiral()

            seleccion = int ( input ( "¿Qué desea hacer?:" ) )

        elif seleccion == 4:
            dibujarCirculos()

        elif seleccion == 5:
            numero = int(input("¿Cual es el valor que quieres usar:"))
            print ( aproximarPi(numero))
            seleccion = int ( input ( "¿Qué desea hacer?:" ) )

        elif seleccion == 6:
            print("Los números divisibles entre 17 son:",calcularNumeros())
            seleccion = int ( input ( "¿Qué desea hacer?:" ) )

        elif seleccion == 7:
            calcularPiramide()
            seleccion = int(input("¿Que desea hacer?"))

        elif seleccion == 0:
            print ( "Adios!" )
            break


main ()











