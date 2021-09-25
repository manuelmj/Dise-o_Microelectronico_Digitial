import numpy as np 



def crearMtraix(numeroFilas:int,numeroColumnas:int)->np.empty: 
    
    array=np.empty((numeroFilas,0),float) 

    listaFilas=[]
    for a in range(numeroFilas) :   
        listaaux=[]
        print("---valores de la fila numero: {numero}---".format(numero=a))
        for b in range(numeroColumnas): 
            listaaux.append(input("posicion {numero1} en la fila {numero2}-->[{numero1},{numero2}]: ".format(numero1=a,numero2=b)))
        listaFilas.append(listaaux)
    
    return(np.append(array,np.array(listaFilas),axis=1))
    
    


def main()->None:
    
    listaMtraices=[]
    numeroFilas=int(input("ingrese el numero de filas: "))
    numeroColumnas=int(input("ingrese el numero de columnas: "))
    for i in range(2):
        print("--MATRIZ NUMERO {numero}".format(numero=i+1))
        listaMtraices.append(crearMtraix(numeroFilas,numeroColumnas))
    else:             
        print(listaMtraices[0])
        print("\r\n",listaMtraices[1])
            
    print(listaMtraices[0]*listaMtraices[1])
    
    
    
    

if __name__ == "__main__": 
    main()