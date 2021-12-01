# Exercício 5: Faça um programa que leia um número inteiro e mostre na tela se é ou não um número primo.

while True:

  numero = int(input('Digite um número: '))

  if numero % 2 !=0: 

    print('É um número primo')
    break

  elif numero == 2: 

    print('É um número primo')  
    break
  else: 

    print('Não é um número primo')

    break