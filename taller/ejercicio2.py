



def suma_numeros(numero:dict,keys:list)->None:
    
    print("""\r\nel resultado\r\n 
          {numero_1}+{numero_2}+{numero_3}+{numero_4}+{numero_5}={resultado}
          """.format(numero_1=numero[keys[0]],numero_2=numero[keys[1]],numero_3=numero[keys[2]],
                     numero_4=numero[keys[3]],numero_5=numero[keys[4]] ,resultado=(numero[keys[0]])
                     +(numero[keys[1]])+(numero[keys[2]])+(numero[keys[3]])+(numero[keys[4]])))
    pass 
    

def main()->None:
    
    numeros={"primer":0,"segundo":0,"tercer":0,"cuarto":0,"quinto":0}
    key=list(numeros.keys())
        
    for a in key:
       numeros[a]=float(input("ingrese el {numero} numero:  ".format(numero=a)))
         
    suma_numeros(numeros,key)       
 

if __name__=="__main__": 
    main() 