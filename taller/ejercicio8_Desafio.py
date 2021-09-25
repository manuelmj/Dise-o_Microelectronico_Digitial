
import math 


def funcion(x)->float:
    return(math.exp(x)+((x)**3)-5)

def funcionDerivada(x)->float:
    return math.exp(x)+ (3*(x**2))

def newtonR()->list: 
    lista_soluciones=[]
    x=0
    for i in range(100): 
        
        x=(x)-(funcion(x)/funcionDerivada(x))
        
        lista_soluciones.append(x)  
    return lista_soluciones    


def newtonR_condicion(exilon:float)->list: 
    lista_soluciones=[]
    x=0
    x=(x)-(funcion(x)/funcionDerivada(x))
    lista_soluciones.append(x)  
    aux=0
   # while(True): 
    for i in range(20):    
        aux=x
        x=(x)-(funcion(x)/funcionDerivada(x))
        lista_soluciones.append(x) 
        a=(x-aux)<exilon  
        print(x,aux, (aux-x),a)
        if(a and (a-aux)!=0)<exilon:
            break
    return lista_soluciones    




def main()->None:
   # print(newtonR())
    
    print(newtonR_condicion(0.0001))
    pass


if __name__=="__main__": 
    main()