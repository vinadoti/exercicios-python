#Exercício 7: Faça um programa que leia o preço de um produto e mostre o valor com 5% de desconto.

produto = float(input('Digite o valor do produto: R$'))
desconto = produto * 0.05
valor_final = produto - desconto
print ("O valor final com 5% de desconto é: R${}".format(valor_final))