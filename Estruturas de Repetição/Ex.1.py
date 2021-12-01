# Exercício 1: Faça um programa que cadastre o estado civil de uma pessoa, entretanto, o programa deve continuar perguntando enquanto o valor informado for diferente de "solteiro" ou "casado".

while True:
  estado_civil = input('Digite o seu estado civil: ')
  if estado_civil.lower() == 'solteiro' or estado_civil.upper() == 'CASADO':      #.lower() serve para tranformar tudo em minusculo
    break                                                                         #.upper() serve para transformar tudo em maiusculo

print('Seu estado civil é:',estado_civil) 