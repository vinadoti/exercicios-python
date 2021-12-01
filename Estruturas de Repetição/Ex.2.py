# Exercício 2: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# Input: 5
# Output: 120

num = int(input("Digite um Numero para fatoriar: "))
cont = num
fatorial = 1
while cont > 0:
  print(f"{cont} x {fatorial}")
  fatorial *= cont
  cont -= 1
print(f"O fatorial de {num} é {fatorial}")