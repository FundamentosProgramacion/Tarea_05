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



        for x in range (10,400,10):
            pygame.draw.circle(ventana, Azul, (Ancho//2, Alto//2),x, 1)
            pygame.draw.rect(ventana, Azul, (400-x, 400-x ,2*x,2*x), 1)






        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def aproxPI(x):
    Suma = 0

    for fraccion in range(1, x + 1):
        Suma += (1 / (fraccion ** 4))
    pi = ((Suma) * 90) ** 0.25
    return pi

def divisores():
    suma=0
    for numeros in range(1000, 10000):
        if numeros%17==0:
            suma+=1
    return suma

def piramide():
    x=0
    y=0
    for contador in range(1,10):
        y=(y*10)+contador
        r=y*8+contador
        print(y,"*",8,"+",contador,"=",r)

    for contador in range(1, 10):
        x=(x*10)+1
        r=x*x
        print(x,"*",x,"=",r)

def main():
    eleccion=int(input("Seleccione qué quiere hacer:\n1. Dibujar cuadros y círculos \n2. Dibujar parábolas \n3. Dibujar espiral \n4. Dibujar círculos \n5. Aproximar Pi \n6. Contar divisibles entre 17 \n7. Imprimir pirámides de números \n 0. Salir \nQué desea hacer? "))
    if eleccion ==1:
        dibujar()
    elif eleccion ==2:
        pass
    elif eleccion==3:
        pass
    elif eleccion==4:
        pass
    elif eleccion==5:
        print(aproxPI(10))

    elif eleccion==6:
        print(divisores())
    elif eleccion==7:
        piramide()
    else: print("has salido")



main()