#Jossian Abimelec Garcia Quijano
#Dibuja....


import pygame



def dibujar():
    Ancho=800
    Alto=800
    Azul= (33, 81, 238)
    BLANCO=(255, 255, 255)
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        #for x in range(,10):

        pygame.draw.circle(ventana, Azul, (Ancho//2, Alto//2), Ancho//2, 2)
        pygame.draw.rect(ventana, Azul, (10, 10, Ancho-10, Alto-10), 2)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
def main():
    dibujar()



main()