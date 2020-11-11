#Escribe un programa que escriba a los siguientes número (la separación entre
#número es para facilitar cuántos números se deben escribir en cada bucle) y en
#el que la función range que utilices tenga un ÚNICO argumento y que el valor 
#de este se corresponda con el número de elementos que aparecen en la lista 
#( por Ejemplo, para la primera lista range (10)).

print("Primera fila")

for i in range(10):
    
    print (i+1,end=" ")

print("")
print("Segona fila")
    
for j in range(10):
   
    print ((j+1)*2,end=" ")
 
print("")    
print("Tercera fila")

for k in range(10):
    
    print(k*2+20,end=" ")

print("")    
print("Cuarta fila")

for l in range(6):
    
    print(l*4+10,end=" ")
    
print("")    
print("Quinta fila")

for n in range(9):
    
    print(40-(n*5),end=" ")