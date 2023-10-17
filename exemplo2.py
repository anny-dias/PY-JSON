import json 

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    lista = json.load(arquivo)

for item in lista:
    if item['nome'] == 'Anny Dias':
        print('Encontrado')