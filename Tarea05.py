import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)



# Estructura básica de un programa que usa pygame para dibujar
def figura1():
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

        distanciaRect=ALTO//2
        distanciaCircle=0
        distancia=0
        n = 0
        i = 0

        while distanciaCircle <= ALTO//2:
            distanciaCircle = distanciaCircle + 10
            distancia = distancia + 10
            n = n + 1
            i = i + 1
            pygame.draw.circle(ventana, (randint(0,255) , randint(0,255), randint(0,255)), (ANCHO//2, ALTO//2), distanciaCircle, 1)
            pygame.draw.rect(ventana, (randint(0,255), randint(0,255), randint(0,255)), (distancia, distancia , (ANCHO-distancia*2), (ALTO-distancia*2)),1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def figura2():
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

        distancia = 0
        while distancia<= ALTO//2:
            distancia = distancia+1
            pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (0+distancia, ALTO//2), (ANCHO//2, ALTO//2-distancia),1)
            pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (0+distancia, ALTO//2), (ANCHO//2, ALTO//2+distancia),1)
            pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (ANCHO-distancia,ALTO//2), (ANCHO//2, ALTO//2-distancia),1)
            pygame.draw.line(ventana, (randint(0,255), randint(0,255), randint(0,255)), (ANCHO-distancia,ALTO//2), (ANCHO//2, ALTO//2+distancia),1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def Pi(divisor):
    contador = 0
    for digito in range(1,divisor):
        aprox = 1/(digito**4)
        contador += aprox
    pi = (contador*90)**(1/4)
    return pi


def Entre17():
    for digito in range(1000,10000):
        if digito%7 == 0:
            print (digito)


def piramides():
    n = 1
    for i in range(1, 9):
        if i == 1:
            n == n
        if i != 1:
            n = (n * 10) + i
        serie = (n * 8) + i

        print(n, "*8 +", i, "=", serie)

    print("")

    m=1
    for k in range(1,10):
        if k==1:
            serie = m
        if k!=1:
            m=m*10+1
            serie=m*m
        print(m, "*", m, "=", serie)

def main():
    print("Menu")
    print("1º Dibujar cuadros y circulos")
    print("2º Dibujar parabolas")
    print("3º Dibujar espiral")
    print("4º Dibujar circulos")
    print("5º Aproximar pi")
    print("6º Contar divisibles entre 17")
    print("7º Imprimir piramide de numeros 1")
    print("8º Imprimir piramide de numeros 2")
    print("0º Salir")

    opcion=int(input("¿Que quiere hacer?: "))

    if opcion==1:
        figuraI=figura1()
        print(figuraI)

    if opcion==2:
        figuraII=figura2()
        print(figuraII)

    if opcion==5:
        divisor=int(input("Cual es el divisor: "))
        aproxPi=Pi(divisor)
        print ("El pi es", aproxPi)

    if opcion==6:
         entre=Entre17()
         print(entre)

    if opcion==7:
        escalera=piramides()
        print (escalera)

    if opcion==0:
        print ("Terminado")

main()
        
