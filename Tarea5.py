# Tarea 5
# Autor: Carlos Martínez Rodríguez
# Con ciclos se elaboraron distintos tipos de funciones. Algunos para hacer trazos y figuras
# utilizando pygame y otros para realizar calculos y operaciones.

# Librerías
import pygame, random
from math import radians, sin, cos

# Función para generar colores de manera aleatoria
def randomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Función que dibuja una espiral con pygame
def dibujarEspiral():
    # Dimensiones de pantalla
    ANCHO = 800
    ALTO = 800

    # Iniciar PyGame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    # Paleta de colores
    BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
    NEGRO = (0, 0, 0)

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

            # Medidas del centro para ambos ejes x & y
            centroX = ANCHO // 2
            centroY = ALTO // 2

            color = NEGRO
            position = 0
            # El ciclo for va de 5 en cinco y su rango es el valor del tamaño de la ventana
            for x in range(5, ALTO - 10, 5):
                sentido = position % 4
                if sentido == 0:
                    pygame.draw.line(ventana, color, (centroX, centroY), (centroX + x, centroY))
                    centroX += x
                if sentido == 1:
                    pygame.draw.line(ventana, color, (centroX, centroY), (centroX, centroY - x))
                    centroY -= x
                if sentido == 2:
                    pygame.draw.line(ventana, color, (centroX, centroY), (centroX - x, centroY))
                    centroX -= x
                if sentido == 3:
                    pygame.draw.line(ventana, color, (centroX, centroY), (centroX, centroY + x))
                    centroY += x

                pygame.draw.line(ventana, color, (centroX, centroY), (centroX, centroY))
                position += 1

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame

# Función que dibuja una serie de cuadradas con circulos dentro, aumentan de tamaño
def dibujarCuadrosCirculos():
    import pygame, math

    # Dimensiones de pantalla
    ANCHO = 800
    ALTO = 800

    # Iniciar PyGame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
    NEGRO = (0, 0, 0)

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

        # Centro de la pantalla en ambos ejes
        centroX = ALTO // 2
        centroY = ANCHO // 2

        for x in range(0, ALTO, 10):
            pygame.draw.rect(ventana, NEGRO, (centroX - x, centroY - x, x * 2, x * 2), 1)
            if x < 1:
                pygame.draw.circle(ventana, NEGRO, (centroX, centroY), 1, 1)
            else:
                pygame.draw.circle(ventana, NEGRO, (centroX, centroY), x, 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)


        # Después del ciclo principal
    pygame.quit()  # termina pygame

# Función para dibujar una estrella elaborada con parábolas
def dibujarParabolas():
    # Dimensiones de la pantalla
    ANCHO = 800
    ALTO = 800

    # Colores
    BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
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

        # Cuadrante I
        for x in range(0, ANCHO // 2, 10):
            color = randomColor()
            pygame.draw.line(ventana, color, (ANCHO // 2, 0 + x), (ANCHO // 2 - x, ALTO // 2))

        # Cuadrante II
        for x in range(0, ANCHO // 2, 10):
            color = randomColor()
            pygame.draw.line(ventana, color, (ANCHO // 2, ALTO // 2 - x), (ANCHO - x, ALTO // 2))

        # Cuadrante III
        for x in range(0, ANCHO // 2, 10):
            color = randomColor()
            pygame.draw.line(ventana, color, (ANCHO // 2 + x, ALTO // 2), (ANCHO // 2, ALTO - x))

        # Cuadrante IV
        for x in range(0, ANCHO // 2, 10):
            color = randomColor()
            pygame.draw.line(ventana, color, (0 + x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame

# Función para dibujar una serie de círculos que cambian de posición en relación con los grados
def dibujarCirculos():
    # Dimensiones de pantalla
    ANCHO = 800
    ALTO = 800

    # Iniciar PyGame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
    NEGRO = (0, 0, 0)

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

        # Centro de la pantalla en ambos ejes
        centroX = ALTO // 2
        centroY = ANCHO // 2


        radio = 150


        for circulos in range(12):
            angulo = radians(circulos * 30)
            x = int(sin(angulo) * radio + centroX)
            y = int(cos(angulo) * radio + centroY)
            pygame.draw.circle(ventana, NEGRO, (x, y), radio, 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)

    # Después del ciclo principal
    pygame.quit()  # termina pygame

# Función que se aproxima al valor de pi con una secuencia
def aproximacionPi(num):
    val = 0
    for num in range(1, num + 1):
        val = val + (1 / (num ** 4))
    return val

# Función que regresa todos los numeros que se pueden dividr entre 17 del 1000 al 10000
def calcularDigitos():
    contador = 0
    num = 1000
    while num < 10000:
        if num % 17 == 0:
            contador += 1
        num += 1
    print(contador)

# Función que escribe dos pirámides
def piramides():
    # Piramide de digitos
    n = 0
    for x in range(1, 10):
        n = (n * 10) + x
        a = n * 8 + x
        print(n, "* 8 +", x, "=", a)

    print("\n")
    # Pirámide del 1
    d = 0
    for x in range(9):
        d = (1 * (10 ** x)) + d
        b = d ** 2

        print(d, "*", d, "=", b)

# Función Main del programa
def main():

    #Menu
    print("Tarea 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 17")
    print("7. Imprimir pirámides de números")
    print("0. Salir \n")
    # EL usuario selecciona lo que quiere hacer
    a = int(input("Qué quieres hacer?"))
    # Mientras seleccione una opción diferente a la 8 podra seguir utilizando el programa
    while a != 0:
        if a == 1:
            dibujarCuadrosCirculos()
        if a == 2:
            dibujarParabolas()
        if a == 3:
            dibujarEspiral()
        if a == 4:
            dibujarCuadrosCirculos()
        if a == 5:
            val = int(input("Ingresa un valor para calcular la aproximación: "))
            print("La aproximación a pi es =", aproximacionPi(val))
        if a == 6:
            print("Entre el 1000 y 10000 hay", calcularDigitos(), "números que se pueden dividir entre 17")
            calcularDigitos()
        if a == 7:
            piramides()
        a = int(input("Qué quieres hacer? "))

main()