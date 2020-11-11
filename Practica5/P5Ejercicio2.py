#Escribe un programa que pida dos números y escriba qué números entre ese par 
#de números son pares y cuáles impares

print("Escribe dos numeros enteros.")

numero1=int(input("Escribe un numero:"))
numero2=int(input(f"Escribe un numero mayor que {numero1}:"))

for i in range(numero1+1,numero2):
    if (i%2==0):
        print ("El numero",i,"es par")
    else:
        print ("El numero",i,"es impar")



