#Autor: Eduardo Roberto Müller Romero, A01745219
#Tarea 05: Ciclos "for"

import pygame
import math
from random import randint

ANCHO = 800
ALTO = 800
centroX = ANCHO//2
centroY = ALTO//2

NEGRO = (0, 0, 0)

def dibujarcirculoconcuadrado():
	#Esta función usa un ciclo for para generar circulos y cuadrados en el rango de la ventana
	#El ciclo lo que hace es aumentar el tamaño de los circulos y de los cuarados
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))
	reloj = pygame.time.Clock()
	termina = False
	while not termina:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				termina = True

		ventana.fill(NEGRO)

		for x in range(10, ANCHO+1, 10):
			randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
			pygame.draw.rect(ventana, randomColor, (x, x, ANCHO - 2 * x, ALTO - 2 * x), 1)
			pygame.draw.circle(ventana, randomColor, (centroX, centroY), x, 1)

		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()


def circulos(): #Esta función dibuja la figura de los circulos
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
	reloj = pygame.time.Clock()  # Para limitar los fps
	termina = False  # Bandera para saber si termina la ejecución

	while not termina:
		# Procesa los eventos que recibe
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
				termina = True

		ventana.fill(NEGRO)
	#Usando el circulo unitario, se puede determinar que cada circulo se dibuja a 150 px del centro, formando una circunferencia
	#Cada 30 grados se dibuja un circulo
		unit_circle = 360
		for ang in range(0, unit_circle+1, 30):
			randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
			rad = math.radians(ang)
			x = int(150 * (math.cos(rad)))
			y = int(150 * (math.sin(rad)))
			pygame.draw.circle(ventana, randomColor, (centroX + x, centroY + y), 150, 1)

		pygame.display.flip()  # Actualiza trazos
		reloj.tick(550)  # 40 fps

	pygame.quit()  # termina pygame

def parabolas():
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))
	reloj = pygame.time.Clock()
	termina = False

	while not termina:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
				termina = True

		ventana.fill(NEGRO)

		# Dibujar, aquí haces todos los trazos que requieras
		for x in range(0, centroX+1, 10):
			randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
			pygame.draw.line(ventana, randomColor, (x, centroY), (centroX, (centroY + x)), 1)

		for x in range(0, centroX+1, 10):
			randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
			pygame.draw.line(ventana, randomColor, (x, centroY), (centroX, centroY - x), 1)
			randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
			pygame.draw.line(ventana, randomColor, (ANCHO - x, centroY), (centroX, (centroY + x)), 1)

		for x in range(0, centroX+1, 10):
			randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
			pygame.draw.line(ventana, randomColor, ((ANCHO - x), centroY), (centroX, (centroY - x)), 1)

		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def espiral():

	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))
	reloj = pygame.time.Clock()
	termina = False
	while not termina:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				termina = True
		ventana.fill(NEGRO)
#Si cada linea aumenta 5, para dibujar cada cuadrante (arriba, abajo, izquierda, derecha) el aumento del tamaño es de 20
		for n in range(0, 411, 10): #ciclo for para generar el patrón de lineas
			randomColor = (randint(0, 255), randint(0, 255), randint(0, 255))
			pygame.draw.line(ventana, randomColor,(centroX-n, centroY+n), (centroX+5+n, centroY+n), 1)#cada linea va a aumentar 10 a la izq y 10 a la der
			pygame.draw.line(ventana, randomColor, ((centroX+5)+n, centroY+n), (centroX+5+n, centroY-10-n))
			#Ya siendo más grande que la anterior, van cambiando sus posiciones iniciales y finales(difieren del centro)
			pygame.draw.line(ventana, randomColor, (centroX+5+n, centroY-10-n), (centroX-10-n, centroY-10-n), 1)
			pygame.draw.line(ventana, randomColor, (centroX-10-n, centroY-10-n), (centroX-10-n, centroY+10+n), 1)
		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def aproximarPi(n):
	sum = 0
	a = n + 1
	for x in range(1, n):
		div = 1/(x**4)
		sum += div
	pi = (sum * 90)**(1/4)
	return pi

def piramide1():
	contador = 0
	for x in range(9):
		operacion = (contador * 10) + x
		contador = operacion
		resultado = contador * 8 + x
		print(operacion, "* 8 +", x, "=", resultado)

def divisible():
	cuantos = 0
	for n in range(1000, 10000):
		a = n%17
		if a == 0:
			cuantos += 1
	return cuantos

def piramide2():
	a = 1
	for x in range(10):
		n = 10 ** x
		if x < 1:
			print("1 * 1 = 1")
		else:
			a = a + n
			b = a**2
			print(a, "*", a, "=", b)

def main():
	print("Tarea 5: Ciclos 'for' y dibujos en pygame")
	user = randint(1, 10)
	while user != 0:
		print("Menú:")
		print("1. Cuadros con Círculos")
		print("2. Parábolas")
		print("3. Dibujo: Rectas")
		print("4. Circulos")
		print("5. Aproximar el valor de pi")
		print("6. Múltiplos con 4 dígitos de 17")
		print("7. Piramides de operaciones")
		print("0. Salir")
		user = int(input("Selecciona una opción para correrla: "))
		if user == 1:
			dibujarcirculoconcuadrado()
		elif user == 2:
			parabolas()
		elif user == 3:
			espiral()
		elif user == 4:
			circulos()
		elif user == 5:
			n = int(input("Ultimo divisor: "))
			print(aproximarPi(n))
		elif user == 6:
			print(divisible(), "números de 4 dígitos son divisibles entre 17")
		elif user == 7:
			piramide1()
			piramide2()
	print("FIN")

main()
