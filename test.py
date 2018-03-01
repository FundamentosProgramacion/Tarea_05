# Sebastian Morales martin
# aqui pruebo las funciones una por una antes de ser integradas
def piramides():
    acumulador = 1
    acumulador2 = 0
    for numero in range(1, 10):
        total2 = acumulador**2
        print('%d * %d = %d' % (acumulador, acumulador, total2))
        total = 10**numero
        acumulador += total
    for numero in range(1, 10):
        acumulador2 += numero
        total2 = acumulador2 * 8 + numero
        print('%d * 8 + %d = %d'% (acumulador2, numero, total2))
        acumulador2 *= 10
piramides()