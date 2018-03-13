#Jossian Abimelec García Quijano
#calcula y cuántos números de 4 dígitos son divisibles entre 17




def divisores():
    suma=0
    for numeros in range(1000, 10000):
        if numeros%17==0:
            suma+=1
    return suma

def main():
    print(divisores())
main()