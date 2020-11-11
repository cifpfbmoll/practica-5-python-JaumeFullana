#Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje 
#de la siguiente manera:
print("Vamos a dibujar un rectangulo!")
altura=int(input("ponga la altura aqui:"))
ancho=int(input("pon el ancho aqui:"))


for i in range (altura):
    print ("")
    for j in range (ancho):
        print ("*",end="")
