#Exercício 5: Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor (não utilize as funções built-in max() e min())

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))
maior = x
if y > maior:
    maior = y
if z > maior:
    maior = z
    
menor = x
if y < menor:
    menor = y
if z < menor:
    menor = z

print ("O maior número é", maior, "e o menor número é", menor)