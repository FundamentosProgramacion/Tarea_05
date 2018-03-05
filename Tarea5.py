# Autor: Fernando Sebastian Silva Miramontes
# Lista de comando que realiza diversas operaciones con ciclos for.

import math
import pygame

def dibujar(x):
    # Dimensiones de la pantalla
    ANCHO = 800
    ALTO = 800
    # Colores R,G,B en el rango [0,255]
    BLANCO = (255, 255, 255)
    VERDE_BANDERA = (0, 122, 0)
    ROJO = (255, 0, 0)
    NEGRO = (0,0,0)

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
###########################################################################################

        # Realiza un patron con círculos y cuadros.
        def dibujarCirculos_y_Cuadrados():
          b = 10
          for l in range(395, -1, -10):
            pygame.draw.rect(ventana,NEGRO, (l,l,b,b),1)
            pygame.draw.circle(ventana, NEGRO, (ALTO // 2, ANCHO // 2), b//2, 1)
            b = b + 20

        # Realiza una figura de estrella con parabolas. Se dibuja mediante sectores.
        def dibujarParabolas():
            for y in range(0,401,10):
                # SECTOR +/+
                pygame.draw.line(ventana,NEGRO,(400,y),(y+400,400),1)
                # SECTOR -/+
                pygame.draw.line(ventana, NEGRO, (400, y), (400-y, 400), 1)
                # SECTOR -/-
                pygame.draw.line(ventana, NEGRO, (400, 800-y), (y + 400, 400), 1)
                # SECTOR +/-
                pygame.draw.line(ventana, NEGRO, (400, 800-y), (400 - y, 400), 1)

        # Dibuja una espiral
        def dibujarEspiral():
            for y in range(0, 401, 10):
                # LINEAS ABAJO
                pygame.draw.line(ventana, NEGRO, (400 - y, 400 + y), (y + 410, 400 + y), 1)
                # LINEAS DERECHA
                pygame.draw.line(ventana, NEGRO, (410 + y, 400 + y), (410 + y, 390 - y), 1)
                # LINEAS ARRIBA
                pygame.draw.line(ventana, NEGRO, (410 + y, 390 - y), (390 - y, 390 - y), 1)
                # LINEAS IZQUIERDA
                pygame.draw.line(ventana, NEGRO, (390 - y, 390 - y), (390 - y, 410 + y), 1)

        # Dibuja 12 círculos cada 30° de un círculo imaginario.
        def dibujar12Circulos():
            # Función que calcula la coordenada "x" del circulo correspondiente
            def calcularX(deg):
                xrad = math.radians(deg)
                x = 150 * math.cos(xrad) + 400
                return int(x)
            # Función que calcula la coordenada "y" del círculo correspondiente
            def calcularY(deg):
                yrad = math.radians(deg)
                y = 150 * math.sin(yrad) + 400
                return int(y)

            for deg in range(30, 361, 30):
                pygame.draw.circle(ventana, NEGRO, (calcularX(deg), calcularY(deg)), 150, 1)
########################################################################################################
        if x ==1:
            dibujarCirculos_y_Cuadrados()
        elif x == 2:
            dibujarParabolas()
        elif x == 3:
            dibujarEspiral()
        elif x == 4:
            dibujar12Circulos()


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def imprimirPiramideNumeros():
    # Esta es la piramide de los numeros consecutivos
    cnc = 1
    for sigN in range(1, 10):
        if sigN > 1:
            cnc = str(cnc) + str(sigN)

        resultado = int(cnc) * 8 + sigN
        print("%s * 8 + %i = %i" % (cnc, sigN, resultado))
    print("")
    # Esta es la funcion de la piramide de unos.
    unos = 1
    for pot in range(0, 9):
        if pot != 0:
            x = unos + 1 * 10 ** pot
            unos = x
        resultado = unos ** 2
        print("%i * %i = %i" % (unos, unos, resultado))

# Aproxima a Pi con una aproximaxion otorgada.
def aproximarPi():
    n = int(input("Por cuanto aproximar? : "))
    cnt = 0
    for fr in range(1, n + 1):
        cnt += 1 / fr ** 4
    print ("Pi =", (cnt * 90) ** 0.25)

# Cuenta cuantos multiplos de 17 hay del 1000 al 9999.
def contarMultDe17():
    #Función que prueba si el número es multiplo o no.
    def esMultiplo(cnt):
        if cnt % 17 == 0:
            return True

        return False

    multiplos = 0
    for cnt in range(1000, 10000):
        if esMultiplo(cnt) == True:
            multiplos += 1

    print(multiplos, "son los números divisibles entre 17")



def main():

    x = 1
    while x != 0:
        x = int(input("Tarea 5. Qué desea hacer?\n1. Dibujar cuadros y círculos\n"
                      "2. Dibujar parábolas\n3. Dibujar espiral\n4. Dibujar círculos\n"
                      "5. Aproximar Pi\n6. Contar divisibles entre 17\n7. imprimir pirámides de números\n"
                      "0. salir\nQué desea hacer? "))
        if x >= 1 and x <= 4:
            dibujar(x)
        elif x == 5:
            print("")
            aproximarPi()
        elif x == 6:
            print("")
            contarMultDe17()
        elif x == 7:
            print("")
            imprimirPiramideNumeros()


main()