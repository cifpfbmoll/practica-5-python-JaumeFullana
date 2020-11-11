#Escribe un programa que pida la altura de un triángulo y lo dibuje de la 
#siguiente manera:

print ("Vamos a dibujar un triangulo boca a bajo!")

altura=int(input("Ponga la altura del triangulo:"))

for i in range (altura,0,-1):
    
    print ("")
    
    for j in range (i):
        
        print("*",end="")
