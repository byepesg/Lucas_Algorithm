#!/usr/bin/env python
# coding: utf-8

# # Punto 6. Taller ecuaciones en diferencias
# # Los números de Lucas están relacionado con los números de Fibonacci, y están definidos por la siguiente secuencia 𝐿𝑛+2=𝐿𝑛+1+𝐿𝑛, 𝐿0=2, 𝐿1=1. Escriba un programa que imprima la siguiente información. El 18-th número de Lucas, el número de Lucas más cercano a 1000, y el primer número de Lucas más grande que 100.

# In[1]:



l0 = 2
l1 = 1
iterador = 0
i = 0
lista1 = []
for i in range (2,18):
      iterador = l0 + l1
      l0 =l1
      l1 = iterador
      lista1.append(iterador)
      
print("Los 18 primeros numeros de Lucas son:")
print(lista1)
print("_________________________________________________")
print("Parte 1: Numero 18 de Lucas")
print("_________________________________________________")
print("El 18 es:")    
print(iterador)


######################################
######Restableciendo valores #########
######################################
print("_________________________________________________")
print("Parte 2: Número de Lucas mas cercano a mil")
print("_________________________________________________")

l02 = 2
l12 = 1
iterador2 = 0
minimo = 0
maximo = 0
c = 0 
while (maximo == 0): 
  iterador2 =  l02 + l12
  l02 = l12 
  l12 = iterador2

  if (iterador2 < 1000): 
      minimo = iterador2
  else:
      maximo = iterador2
  c = c+1

varA = maximo-1000
varB = 1000-minimo
#print("VarA:")
#print(varA)
#print("VarB")
#print(varB)

if ((varA)<(varB)):
  print("Maximo: ")
  print(maximo)
else:
  print("El mas cercano a mil: ")
  print(minimo)


print("_________________________________________________")
print("Parte 3: El primer número de Lucas mayor que 100")
print("_________________________________________________")
l03 = 2
l13 = 1
iterador3 = 0

while(iterador3<=100):
  
  iterador3 = l03+l13
  l03 = l13
  l13 = iterador3
print("El primero mayor que 100 es")  
print(iterador3)


# 
