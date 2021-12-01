# Exercício 3: Faça um programa que leia um número inteiro N e mostre na tela os N primeiros números da Sequência de Fibonacci.
# Input: 7
# Output: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

num = int(input('Digite um número de termo para sequência Fibonacci: '))

cont = 1

anterior = 0
proxima = 1
soma = 1

while cont <= num:
     print(anterior, end='-')
     cont += 1
     soma = proxima + anterior
     anterior = proxima
     proxima = soma
print('Fim')