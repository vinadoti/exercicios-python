# Exercicio 1:Faça um programa que crie uma lista com 9 números inteiros, compute e mostre os números primos e suas respectivas posições.

import random
numeros = random.sample(range(2,101),9)
print(numeros)
for i in numeros:
  primo = True
  for inteiro in range(2,i):
    if i % inteiro == 0:
      primo = False
  if primo:
    print(f'{i} - Posição:{numeros.index(i)}')