#Exercício 8: Faça um programa para aprovar o empréstimo bancário para a compra de uma casa. O usuário deverá informar o valor da casa, a quantidade de parcelas que deseja pagar e seu salário. O empréstimo deverá ser negado caso o valor da parcela exceda 30% do salário.

print ("Digite o valor do imóvel")
valor_imovel = int(input())
print ("Digite a quantidade de parcelas")
qtd_parcelas = int(input())
print("Informe seu salário")
salario = int(input())
if (valor_imovel / qtd_parcelas) > (0.3 * salario):
    print ("Empréstimo negado!")
else:
    print ("Empréstimo aprovado!")