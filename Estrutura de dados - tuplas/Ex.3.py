# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero, até vinte. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {contagem_extenso[numero]}')