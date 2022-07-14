tabela = ('Palmeiras', 'Corinthians', 'Inter', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'São Paulo',
          'Santos', 'Flamengo', 'Botafogo', 'Red Bull Bragantino', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG',
            'Avaí', 'Ceará', 'Atlético-GO', 'Juventude', 'Fortaleza')

print(f'Os 5 primeiros colocados da tabela do brasileirão são: {tabela[0:5]}')
print(f'Os 4 últimos {tabela[16:]}')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('Flamengo está na {} posição '.format(tabela.index('Flamengo')+1))

#print(tabela.index('Flamengo'))


