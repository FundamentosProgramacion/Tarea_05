#Jossian Abimelec García Quijano


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
    piramide()
main()
