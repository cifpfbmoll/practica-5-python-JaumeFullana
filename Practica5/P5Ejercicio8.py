#Escribe un programa que pida la anchura de un triángulo y lo dibuje de la 
#siguiente manera:

anchura=int(input("Escribe la anchura que quieres que tenga el triangulo:"))

for i in range(1,anchura*2):
    
    print ("")
    
    if (i<=anchura):
        
        for j in range(i):
            
            print ("*",end="")
            
    else:
            
        for k in range((anchura*2)-i):
            
            print ("*",end="")
            
            
        
            
    