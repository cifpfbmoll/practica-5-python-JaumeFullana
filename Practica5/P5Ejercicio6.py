#Escribe un programa que pida la altura de un triángulo y lo dibuje de la 
#siguiente manera:

print ("Vamos a dibujar un triangulo!")

altura=int(input("Ponga la altura del triangulo:"))


for i in range (1,altura+1):
    
    print ("")
    
    for j in range (i):
        
        print ("*",end="")