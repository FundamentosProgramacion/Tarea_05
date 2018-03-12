#Mirna Fernanda Zertuhe Calvillo
# Un programa que a traves de un menu selecciona que acción se queire realizar
import pygame
from math import radians,cos,sin,sqrt
from random import randint
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
NEGRO = (0, 0, 0)  # R,G,B en el rango [0,255]
AL = (243, 192, 100)
m=150
k=6


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCirculosCuadros(ventana):
    for r in range (ANCHO//ANCHO,ANCHO//2+1,10):
        ColorAzar= (randint(0,255),randint(0,255),randint(0,255))
        pygame.draw.circle(ventana,AL,(ANCHO//2,ALTO//2),r,1)
    for x in range(10, (ANCHO//2)-1,10):
        ColorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.line(ventana, AL,(ANCHO//2-x,ALTO//2+x),(ANCHO//2+x,ALTO//2+x))#abajo
        pygame.draw.line(ventana, AL,((ANCHO//2-x-1), ALTO // 2+x),(ANCHO//2-x-1, ALTO//2-x))#izq
        pygame.draw.line(ventana, AL,((ANCHO//2-x), ALTO // 2-x-1),(ANCHO//2+x, ALTO//2-x-1))#arriba
        pygame.draw.line(ventana, AL,((ANCHO//2+x), ALTO // 2-x),(ANCHO//2+x, ALTO//2+x))

def dibujarParabolas(ventana):
    for x in range (ANCHO// 2, ANCHO+1,10):
        y = x- ANCHO//2 +10
        ColorAzar= (randint(0,255),randint(0,255),randint(0,255))
        pygame.draw.line (ventana, ColorAzar, (x-ANCHO//2, ALTO//2),(ANCHO//2, y+ALTO//2))
        pygame.draw.line(ventana, ColorAzar, (x - ANCHO // 2, ALTO // 2), (ANCHO // 2, ALTO //2-y))
        pygame.draw.line(ventana, ColorAzar, ((ANCHO+(ANCHO//2))-x, ALTO//2), (ANCHO//2, y+ALTO//2))
        pygame.draw.line(ventana, ColorAzar, ((ANCHO+(ANCHO//2))-x, ALTO // 2), (ANCHO // 2, ALTO // 2 - y))

def dibujarEspiral(ventana):
    x1 = ANCHO // 2
    y1 = ALTO // 2
    for x in range(0, ANCHO, 20):
        ColorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.line(ventana, ColorAzar, (x1, y1), (x1, y1 + (x + 0)))
        x1 = x1
        y1 = y1 + (x + 0)
        pygame.draw.line(ventana, ColorAzar, (x1, y1), ((x1 + (x + 5)), y1))
        x1 = x1 + (x + 5)
        y1 = y1
        pygame.draw.line(ventana, ColorAzar, (x1, y1), (x1, y1 - (x + 10)))
        x1 = x1
        y1 = y1 - (x + 10)
        pygame.draw.line(ventana, ColorAzar, (x1, y1), (x1 - (x + 15), y1))
        x1 = x1 - (x + 15)
        y1 = y1


def dibujarCirculos(ventana):
    for alfa in range(0,360, 30):# 0,360,1
        alfaRad = radians(alfa)
        r= m* cos(k*alfaRad)
        x= int(r*cos(alfaRad))+ ANCHO//2
        y = ALTO//2 - int(r*sin(alfaRad))
        ColorAzar = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.circle(ventana, ColorAzar, (x,y),150,1)


def aproximarPI(numAprox):
    piCuad = 0
    for i in range(1, numAprox + 1):
        piCuad += (1 / (i ** 4))
    pi = sqrt((piCuad * 90))
    return pi

def contarDivisibles17():
    numerosD = 0
    for i in range(1000, 9999):
        resultado = i % 17
        if resultado == 0:
            numerosD += 1
    return numerosD


def imprimirPiramides():
    numeroo = 1
    for i in range(1, 10):
        resultado = (numeroo * 8) + i
        print(numeroo, "* 8 +", i, "=", resultado)
        numeroo = (numeroo * 10) + (i + 1)
    print("")
    numeroo = 1
    for i in range(1, 10):
        resultado = numeroo * numeroo
        print(numeroo, "*", numeroo, "=", resultado)
        numeroo = (numeroo * 10) + 1



def dibujar(accion):
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
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        if accion==1:
            dibujarCirculosCuadros(ventana)
        elif accion==2:
            dibujarParabolas(ventana)
        elif accion==3:
            dibujarEspiral(ventana)
        elif accion==4:
            dibujarCirculos(ventana)



        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    salir = False
    while not salir:
        accion = int(input("Tarea 5. seleccione qué quiere hacer.\n 1. Dibujar cuadros y círculos\n 2. Dibujar parabolas\n 3. Dibujar espiral\n 4. Dibujar círculos\n 5. Aproximar PI\n 6. Contar divisibles entre 17\n 7. Imprimir pirámides de números\n 0. Salir del menu \n ¿Qué desea hacer?"))
        if 5>accion>0:
            dibujar(accion)
        elif accion==5:
            numAprox= int(input("¿qué número deseas aproximar?: "))
            aproximacion= aproximarPI(numAprox)
            print(aproximacion)

        elif accion==6:
            numeroDeDivisibles= contarDivisibles17()
            print(numeroDeDivisibles)
        elif accion==7:
            imprimirPiramides()
        elif accion>=8:
            print("No se ha seleccionado ninguna acción disponible, intente de nuevo")
        else:
          salir =True



main()