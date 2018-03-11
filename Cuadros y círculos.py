#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Crear cuadros y círculos a partir de una función.

import pygame


#Dimensiones de la pantalla
ANCHO=800
ALTO=800

#Colores
Rojo=(255,0,0)
Blanco=(255,255,255)
Negro=(0,0,0)
Verde=(0, 122, 0)


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



def main():
    dibujarCC()

main()
