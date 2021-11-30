#Exercício 3: Escreva um programa que leia a velocidade de um carro. Se esta velocidade for maior que 80Km/h o programa deverá escrever uma mensagem na tela avisando que o usuário levou uma multa e o valor a ser pago. Considere R$ 7 reais por cada Km acima do limite.

print("Qual a velocidade do carro?")
velocidade_carro = int(input())
if velocidade_carro > 80:
    multa = 7* (velocidade_carro - 80)
    print("Você levou uma multa no valor de R$", multa)
else:
    print("Siga em frente!")