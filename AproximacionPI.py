#Jossian Abimelec García Quijano
#Aproxima a PI


def aproxPI(x):
    Suma=0

    for fraccion in range(1, x+1):

        Suma+=(1/(fraccion**4))
    pi=((Suma)*90)**0.25
    return pi
def main():
   print( aproxPI(10))



main()