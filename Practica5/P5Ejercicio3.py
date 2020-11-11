#Escribe un programa que pida dos números y escriba la suma de enteros desde 
#el primero hasta el último.

print("Escribe dos numeros enteros.")

numero1=int(input("Escribe un numero:"))
numero2=int(input(f"Escribe un numero mayor {numero1} que:"))
suma=int()
numero2=numero2+1
for i in range(numero1,numero2):
    suma+=i
    if (i==numero2-1):
        print (i ,end=f"={suma}")
    else:
        print(i ,end="+")

  