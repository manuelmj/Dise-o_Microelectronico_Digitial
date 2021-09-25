

def media(Numeros:list)->float: 
    sumaNumeros=sum(Numeros)
    cantidadNumeros=len(Numeros)
    return(sumaNumeros/cantidadNumeros)
    
def desviacionEstadar(Numeros:list)->float:
    
    cantidadNumeros=len(Numeros)
    sumatoria=0
    x=media(Numeros) 
    
    for numero in Numeros:
        sumatoria+=((numero-x)**2)
    
    resultadoDE=(sumatoria/(cantidadNumeros))**(1/2)    
    return(resultadoDE)    
    

def main()->None:
    
    numeros=[]
    comprobar=1
    while(comprobar):
        comprobar=float(input("ingrese un numero, para salir ingrese el cero: "))
        numeros.append(comprobar)
    numeros.pop(); 
        
    print("\r\nel resultado de la media de los numeros es:  {md}\r\n".format(md=(media(numeros))))
    print("la desviacion estandar de los datos es: {dvc}\r\n".format(dvc=desviacionEstadar(numeros)))
    pass


if __name__ == "__main__":
    main()