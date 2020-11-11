#Escribe un programa que pida un número y escriba si primo o no

numero=int(input("Escribe un numero:"))

esprimo = True

if (numero==1):
    
    print ("Este numero no es primo")

else:
    
    for i in range (1,numero):
    
        if (i>1 and i<numero and numero%i==0):
        
            esprimo = False   
    
    if (esprimo):
    
        print ("Este numero es primo")
    
    else:
    
        print ("este numero no es primo")


