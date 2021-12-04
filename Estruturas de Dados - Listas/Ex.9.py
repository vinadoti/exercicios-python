# Exercicio 9: Faça um programa que leia 10 números inteiros. Em seguida, processe a lista e remova os números repetidos. No final, mostre essa nova lista.

lista_numeros = []
lista_repetidos = []

while len(lista_numeros) < 5:
  numero = int(input('Insira um número inteiro: '))
  lista_numeros.append(numero)

for repetido in lista_numeros:
  if repetido not in lista_repetidos:
    lista_repetidos.append(repetido)

print(lista_numeros)
print(lista_repetidos)