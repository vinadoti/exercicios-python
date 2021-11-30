#Exercício 1: Faça um programa em que ele sorteie um número entre 0 e 5. O usuário deverá então adivinhar este número e o programa deverá escrever na tela se ele acertou ou não.


import random
numero_sorteado = random.randint(0, 5)
print("Digite o número escolhido")
numero_escolhido = int(input())
if numero_escolhido == numero_sorteado:
    print ("Parabéns, voce acertou!")
else:
    print ("Que pena, você errou")
print("O número certo era", numero_sorteado)