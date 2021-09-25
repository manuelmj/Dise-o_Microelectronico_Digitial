





def main()->None:
    
    listaDenominador=[]
    contador=2
    for i in range (1,16):
        
        listaNumeros=[]
        for j in range(3):
            listaNumeros.append(contador)
            contador+=1
        contador-=1
        
        multiplicacion=1
        for valor in listaNumeros:
            multiplicacion*=valor
                
        listaDenominador.append(multiplicacion)    
     #   print(listaDenominador)
    
    
    pi=3
    contador=2
    for denominador in listaDenominador: 

        if contador%2==0:
            pi+=(4/denominador)
        else: 
            pi-=(4/denominador)    
        print("{pi:.{decimales}f}\r\n".format(pi=pi,decimales=contador))
        contador+=1
        pass
    
    
    
    pass


if __name__ == "__main__":
    main()