# Exercício 9: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens:

# O primeiro valor é maior.
# O segundo valor é maior.
# Os valores são iguais.

print("Informe o primeiro número")
valor_um = int(input())
print("Informe o segundo número")
valor_dois = int(input())
if valor_um > valor_dois:
 print("O primeiro valor é maior")
elif valor_um == valor_dois:
 print("Os valores são iguais")
else: 
 print("O segundo valor é maior")