numero=int(input("Escribe un número:"))

lista = [numero]

numero=int(input(f"Escribe un número mayor que {numero}:"))

lista += [numero]

while lista[-2] < numero:

    numero=int(input(f"Escribe un número mayor que {numero} :"))

    lista += [numero]


del lista[-1]

print ("Los números que has escrito son:",end=" ")

for i in lista:
    print (i,end=", ")