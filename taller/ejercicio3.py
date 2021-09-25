


def identificar_triangualo(angulos:list)->str:
    iguales=0
    triangulo=""
    
    print(iguales)
    for pos in range(2): 
        
        if angulos[pos] == angulos[pos+1]: 
            iguales+=1 
    
    if iguales == 2: 
        triangulo="equilatero"
    elif iguales ==1: 
        triangulo="isoseles"
    else : 
        triangulo="escaleno"
 
    return "el triangulo es de tipo -->"+triangulo            
         
     

def main():
    print("a ver ")
    
    lista_angulos=[]
    for a in range(3):
        lista_angulos.append(float(input("ingrese uno de los angulos\r\n")))
        
    print(identificar_triangualo(lista_angulos))
    
    pass

if __name__ == "__main__": 
    main() 
    
    