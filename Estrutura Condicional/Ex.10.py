#Exercício 10: Faça um program que leia o ano de nascimento de uma pessoa e informe se ele ainda vai se alistar ao serviço militar ou se ele está no período de se alistar ou se ele perdeu o prazo para se alistar. Além disso, mostre também a quantidade de anos que falta para se alistar ou que passou do prazo.

print("Digite o ano de nascimento")
ano = int(input())
if (2021 - ano) < 18:
    restante = 18 - (2021 - ano)
    print("Faltam", restante, "anos para você se alistar")
elif (2021 - ano) == 18:
    print ("Você está no período de se alistar")
else:
    sobra = (2021 - ano) - 18
    print ("Você passou", sobra, "anos do prazo de se alistar")