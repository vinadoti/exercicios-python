#Exercício 5: Implemente um programa que tenha como entrada o valor em uma reais e mostre o valor correspondente em dólar.

import requests # ~ include

url = 'https://economia.awesomeapi.com.br/json/last/USD'

resultado = requests.get(url).json()
dolar = float(resultado['USDBRL']['high'])
print(f'A cotação do dolar é de US$ {dolar}.')


reais = float(input('Digite o valor em reais: '))
print(f'{reais} reais corresponde a {reais/dolar:.2f} dolares.')