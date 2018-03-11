def calcularNumeros():
    n=0
    for i in range(1000,10001):
        if i%17==0:
            n+=1
    return n

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
    print("Los números divisibles entre 17 son:",calcularNumeros())


main()