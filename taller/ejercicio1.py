

import math 


def suma(numero1 : float , numero2 : float)->float: 
    return(numero1+numero2)


def resta (numero1 : float, numero2 :float )->float: 
    return(numero1-numero2)

def multiplicacion(numero1:float,numero2 : float  )->float:
    return(numero1*numero2)

def division(numero1:float, numero2:float )->float: 
    return(numero1/numero2)

def  logaritmo(numero1:float)->float:
    return(math.log10(numero1))

def potencia(numero1:float, numero2:float)->float:
    return(numero1**numero2)

def euler(numero1:float)->float:
    return(math.exp(numero1))

def raiz(numero1:float,numero2:float)->float:
    return ((numero2)**(1/numero1))


def main()->None:
    numero1=float(input("\r\ningrese el primer numero: "))
    numero2=float(input("\r\ningrese el segundo numero:"))
    
    print("\r\nnel resultado de la suma es: {}".format(suma(numero1,numero2)))
    print("\r\nel resultado de la resta es: {}".format(resta(numero1,numero2)))
    print("\r\nel resultado de la multiplicacion es: {}".format(multiplicacion(numero1,numero2))) 
    print("\r\nel resultado de la division es: {}".format(division(numero1,numero2)))
    print("\r\nel resultado del logaritmo es: {}".format(logaritmo(numero1)))
    print("\r\nel resultado de la potencia es: {}".format(potencia(numero1,numero2)))
    print("\r\nel resultado del euler a la {} es: {}".format(numero1,euler(numero1)))
    print("\r\nel resultado de la raiz es: {}".format(raiz(numero1,numero2)))


if __name__ == "__main__": 
    main()      