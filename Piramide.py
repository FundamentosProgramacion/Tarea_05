# encoding: UTF-8
# Autor: Genaro Ortiz Durán
# Descripción: Crear una piramide de números a partir de una función.
import pygame

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def calcularCadena():
    numero=0
    viii=8
    for i in range (0,10):
        numero= numero* 10+ i
        total=numero*viii+i
        print(numero,"*",viii,"+",i,"=",total)
    print("============================================")
    UNo = 0

    for i in range(0, 10):
        UNo = UNo * 10 + (i + (1 - i))
        total = UNo**2
        print(UNo, "*", UNo, "=", total)

def main():
    calcularCadena()


main()