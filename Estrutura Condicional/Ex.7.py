#Exercício 7: Condição de existência de um triângulo: Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência, isto é, para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas [Brasil Escola, 2019].

# | b - c | < a < b + c

# | a - c | < b < a + c

# | a - b | < c < a + b

# Com base nesta condição, crie um programa que leia o comprimento de três retas e escreva na tela se estas retas podem ou não formar um triângulo.

l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if  abs(l2 - l3) > l1 or l1  > (l2 + l3) or abs(l1 - l3) > l2 or l2 > (l1 + l3) or abs(l1 - l2) > l3 or l3 > (l1 + l2):
    print ("Não pode ser um triângulo")
else:
    print ("Podem formar triângulo")