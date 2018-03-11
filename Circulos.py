import pygame
from math import *
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
radio=150
NEGRO=(0,0,0)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCírculos():
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
        ventana.fill ( BLANCO )

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        for i in range ( 0, 12 ):
            pygame.draw.circle ( ventana, NEGRO, (int ( ANCHO // 2 + radio * math.cos ( math.pi * i / 6 ) ),int ( ALTO // 2 + radio * math.sin ( math.pi * i / 6 ) )), radio, 1 )
        pygame.display.flip ()  # Actualiza trazos
        reloj.tick ( 40 )  # 40 fps

    # Después del ciclo principal
    pygame.quit ()  # termina pygame


def main():
    dibujarCírculos ()


main ()