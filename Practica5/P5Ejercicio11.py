#Escribe un programa que pida un número e imprima todos sus divisores.

numero=int(input("Escriba un numero para que le pueda decir sus divisores:"))

for i in range(1,numero+1):
    if (numero%(i)==0):
        
        if (i!=numero):
            print (i,end=", ")
        
        else:
            print (i)