#Exercício 13: Faça um programa para jogar Jokenpô (clássico pedra, papel e tesoura) com você. Você deverá informar uma das opções, o programa deverá então sortear uma das três opções possíveis e mostrar quem ganhou na tela.

import random
numero = random.randint(0, 2)
jokempo = ('pedra', 'papel', 'tesoura')
print ("Informe sua opção: pedra, papel ou tesoura")
jogador = (input())
print ("Opção do computador:" , jokempo[numero])
if jokempo[numero] == "pedra":
    if jogador == "pedra":
        print ("Empate!")
    elif jogador == "tesoura":
        print("Você perdeu")
    else:
        print("Você ganhou!")
elif jokempo[numero] == "papel":
    if jogador == "pedra":
        print ("Você perdeu")
    elif jogador == "tesoura":
        print("Você ganhou")
    else:
        print("Empate!")
else:
    if jogador == "pedra":
        print ("Você ganhou!")
    elif jogador == "tesoura":
        print("Empate")
    else:
        print("Você perdeu!")