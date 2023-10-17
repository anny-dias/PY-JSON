# Gera um arquivo JSON a partir de um dicionario Python

import json

dicionario1 = {'codigo': 123, 'nome': 'Anny Dias', 'idade': 18, 'altura': 1.60, 'notas': [9, 7.5, 8, 10]}
dicionario2 = {'codigo': 587, 'nome': 'Julia', 'idade': 22, 'altura': 1.70, 'notas': [10, 5, 8.5, 0]}

lista = [dicionario1, dicionario2]
with open('dados.json', 'w') as arquivo:
    json.dump(lista, arquivo, indent = 4, sort_keys = True)

