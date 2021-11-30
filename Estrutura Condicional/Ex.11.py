#Exercício 11: Faça um programa que leia o comprimento de três lados de um triângulo (válido), indicando que tipo de triângulo será formado:

# Equilátero: todos os lados são iguais; ou
# Isósceles: dois lados são iguais; ou
# Escaleno: todos os lados são diferentes.

l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if  abs(l2 - l3) > l1 or l1  > (l2 + l3) or abs(l1 - l3) > l2 or l2 > (l1 + l3) or abs(l1 - l2) > l3 or l3 > (l1 + l2):
    print ("Não pode ser um triangulo")
elif l1 == l2 == l3:
    print ("Equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print ("Isósceles")
else:
    print ("Escaleno")