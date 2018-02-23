#Jossian Abimelec Garcia Quijano
#Dibuja....


import pygame



def dibujar():
    Ancho=800
    Alto=800

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

         ventana.fill(BLANCO)
        for cuadrado in range(10,800,10):
            pygame.draw.circle(pass)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
def main():
    dibujar()



main()