#Exercício 12: Crie um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento:

# à vista no dinheiro ou cheque: 10% de desconto;
# à vista no cartão: 5% de desconto;
# em até 2x no cartão: preço normal;
# em 3x no cartão: 20% de juros.

print ("Informe o preço do produto")
preco = int(input())
cond = ('1) à vista no dinheiro ou cheque', '2) à vista no cartão', '3) em até 2x no cartão', '4) em 3x no cartão') 
print ("Informe a condição de pagamento", cond)
pgto = int(input())
if pgto == 1:
    valor_final = 0.9 * preco
elif pgto == 2:
    valor_final = 0.95 * preco
elif pgto == 3: 
    valor_final = preco
else:
    valor_final = 1.2 * preco
    
print("O valor final a ser pago é R$", valor_final)