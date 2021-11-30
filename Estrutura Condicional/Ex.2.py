#Exercício 2: Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

print("Digite o número")
numero_inserido = int(input())
if numero_inserido % 2 == 0:
    print ("Número é par!")
else:
    print ("Número é impar")