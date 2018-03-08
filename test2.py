# encoding: UTF-8
# Sebastian Morales Martin
# pruebas 2


def piramide2(numero, acumulador):
    total = acumulador * 8 + numero
    return '%d * 8 + %d = %d' % (acumulador, numero, total)

def piramide1(x):
    total = x**2
    return ('%d * %d = %d' % (x, x, total))
def contador():
    acumulador = 0
    acumulador2 = 0
    for numero in range(9):
        acumulador*= 10
        acumulador += 1
        print(piramide1(acumulador))
    for numero in range(1, 10):
        acumulador2 *= 10
        acumulador2 += numero
        print(piramide(numero, acumulador2))




contador()