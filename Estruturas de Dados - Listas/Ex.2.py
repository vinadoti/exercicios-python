# Exercicio 2: Faça um programa que carregue duas listas com dez elementos numéricos cada uma e mostre um vetor resultante com os 20 elementos. Altere a primeira lista com os novos valores.

from random import sample
import numpy as np

lista1 = sample(range(0, 100), 10)
lista2 = sample(range(0, 100), 10)
print(lista1)
print(lista2)

lista1.extend(lista2)
# lista1 = np.array(lista1)

print(lista1)