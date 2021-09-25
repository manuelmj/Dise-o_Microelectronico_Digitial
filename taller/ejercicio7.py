



def mesesAños(mes:int,anio:int)->None: 
    
    dic_meses={"enero":30,
            "febrero":28,
            "marzo":31,
            "abril":30,
            "mayo":31, 
            "junio":30, 
            "julio":31,
            "agosto":31, 
            "septiembre":30,
            "octubre":31,
            "noviembre":30,
            "diciembre":31
                            }      
    if(anio%4==0 or anio%100==0):
        dic_meses["febrero"]=29         
    keys_meses=list(dic_meses.keys())
   
    print("usted ingreso el mes de {mes} el cual tiene {dias} dias".format(mes=keys_meses[mes-1],
                                                                           dias=dic_meses[keys_meses[mes-1]]))


def main()->None:
       
    fecha=str(input("ingrese un mes y un año en formato mm/aaaa: "))
    print("\r\n")
    print("\r\n")
    mes=fecha[:2]
    anio=fecha[3:]
    
    if(len(mes)!=2 or len(anio)!=4):
        print("la fecha ingresada no es valida\r\n")
        return None 
             
    print("usted ingresó la fecha: {Mes}/{Anio}\r\n".format(Mes=mes,Anio=anio))
    
    mesesAños(int(mes),int(anio)) 
    
    pass

if __name__ == "__main__": 
    main() 
 