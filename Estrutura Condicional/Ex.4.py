#Exercício 4: Crie um programa que calcule o preço a ser pago por um serviço computacional. O usuário deverá informar a quantidade de horas utilizada. Será cobrado R$ 0,50 por hora para consumo de até 10 horas, R$ 0,45 por hora para consumo entre 10 e 20 horas e R$ 0,40 por hora para consumo maior de 20 horas.

print("Informe a quantidade de horas utilizada")
hr_utilizada = int(input())
if hr_utilizada <= 10:
    valor_pago = 0.5 * hr_utilizada
elif 10 < hr_utilizada < 20:
    valor_pago = 0.45 * hr_utilizada
else: 
    valor_pago = 0.4 * hr_utilizada

print("O valor a ser pago é: R$", valor_pago)