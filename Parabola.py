#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Crear parábolas a partir de una función.

import pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO= (0,0,0)

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
        ventana.fill(NEGRO)

        for i in range(1, 400, 10):
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i, ALTO / 2), (ANCHO / 2, i + ALTO / 2))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i, ALTO / 2), (ANCHO / 2, -i + ALTO / 2))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (ANCHO - i, ALTO / 2), (ANCHO / 2, ALTO / 2 + i))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO - i, ALTO / 2), (ANCHO / 2, ALTO / 2 - i))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujarParabola()


main()