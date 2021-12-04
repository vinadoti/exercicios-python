# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre:

# Apenas os 5 primeiros colocados
# Os 4 últimos colocados na tabela
# Classificação dos times
# Uma lista com os times em ordem alfabética
# Em que posição na tabela está o time do São Paulo.
# Dica: Procure por "Tabela Campeonato Brasileiro de Futebol" no Google.

times = ('Flamengo','Palmeiras','Santos','Corinthians','Internacional', \
         'São Paulo','Grêmio','Bahia','Atlético PR',
             'Atlético Mineiro','Botafogo','Goiás','Vasco da Gama','Ceará',\
         'Fortaleza','Fluminense','Cruzeiro','CSA','Avaí','Chapecoense')

opcao = int(input('''
[ 1 ] Imprimir os 5 primeiros colocados.
[ 2 ] Imprimir os 4 ultimos colocados.
[ 3 ] Imprimir Classificação dos times.
[ 4 ] Imprimir os times em ordem alfabética.
[ 5 ] Posição do time São Paulo.
Escolha uma Opção: '''))

if opcao == 1:  #Apenas os 5 primeiros colocados
    for time in range(0, 5):
        print(f'{time+1}º {times[time]}')
elif opcao == 2:  #Os 4 últimos colocados na tabela
    for time in range(16, 20):
        print(f'{time + 1}º {times[time]}')
elif opcao == 3:  # Classificação dos times
    for time in range(0, 20):
        print(f'{time + 1}º {times[time]}')
elif opcao == 4: #Uma lista com os times em ordem alfabética
    print(f'Times em ordem alfabética: {sorted(times)}')
elif opcao == 5: #Em que posição na tabela está o time do São Paulo.
    print(f'São Paulo está na {times.index("São Paulo")+1} posição.')
else:
    print('Opção Inválida.')