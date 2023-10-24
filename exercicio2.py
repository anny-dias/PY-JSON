'''Exercício 2 
Considere o arquivo “foods.CSV”, com três colunas, no formato abaixo, onde cada linha representa um 
indivíduo com suas respectivas informações. 
NAME,ID,FAVORITE FOOD
Implemente um programa que a partir do arquivo indicado gere um arquivo JSON no formato:
{
 "1": {
 "nome": "John Doe",
 "food": "pizza"
 },
 "2": {
 "nome": "Jane Smith",
 "food": "sushi"
 },
 "3": {
 "nome": "Michael Johnson",
 "food": "steak"
 }
}
'''

import json 

with open('foods.csv', 'r', encoding='utf-8') as arquivo:
    dicionario = {}
    conta_linha = 1
    for linha in arquivo:
        if conta_linha > 1:                 #ignora a primeira linha do arquivo csv
            lista = linha.split(';')

            #armazena dados no dicionario
            dicionario[lista[1]] = {'nome': lista[0], 'food': lista[2].replace('\n', '')}
        conta_linha += 1

#cria arquico json
with open('food.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)