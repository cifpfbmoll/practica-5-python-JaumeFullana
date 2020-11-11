#Escribe un programa que pida la anchura y la altura de un rectángulo y 
#lo dibuje de la siguiente manera:
print("Vamos a dibujar un rectangulo!")
altura=int(input("ponga la altura aqui:"))
ancho=int(input("pon el ancho aqui:"))


for i in range (altura):
    
    print ("")
    
    if (i==0 or i==altura-1):
        
         for j in range (ancho):
             print ("*",end="")
        
    else:
        
        for k in range (ancho):
            
            if (k==0 or k==ancho-1):
                print ("*",end="")
                
            else:
                print(" ",end="")
                
            
            