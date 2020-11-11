#Escribe un programa que pida un número y calcule su factorial.

numero=int(input("Escriba un numero entero para calcular su factorial:"))

numero=numero+1

mult=int(1)

for i in range(1,numero):
    mult*=i
    if (i==numero-1):
        print (i,end=f"={mult}")
    else:
        print(i,end="*")