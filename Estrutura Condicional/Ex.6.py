# Exercício 6: Escreva um programa que leia o salário de um funcionário e calcule o seu aumento. Caso o salário atual seja superior a R$ 1.000,00 calcule um aumento de 10%, caso contrário, calcule um aumento de 15%.

print ("Digite o valor do salário")
salario = int(input())
if salario >= 1000:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
    
print("Seu aumento é de R$", aumento)
