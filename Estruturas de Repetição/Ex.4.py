# Exercício 4: Crie um programa que escreva na tela todos os números pares no intervalo de 1 a 50.

print(' Números Pares Entre 1 e 50')
n = 0
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('FIM')