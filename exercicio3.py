''''Exercício 3
Implemente um sistema para cadastro de Pets, com as opções Inserir, Excluir, Listar Todos. Utilize um 
arquivo JSON para armazenar as informações. O arquivo JSON deve ter a estrutura abaixo e conforme as 
operações realizadas, o arquivo deve ser modificado.
[
 {
 "tipo": "Cachorro",
 "nome": "Bebel",
 "idade": 4
 },
 {
 "tipo": "Hamster",
 "nome": "Pimpão",
 "idade": 2
 },
 {
 "tipo": "Cavalo",
 "nome": "Trovão",
 "idade": 6
 }
]'''

import os
import json

def inserir():
    try:
        if os.path.exists('pets.json'):         # verifica se oa rquivo ja existe
            with open('pets.json', 'r', encoding='utf-8') as arquivo:
                lista_pets = json.load(arquivo)
        else:
            lista_pets = []

        nome = input('Nome do PET: ')
        tipo = input('Tipo do PET: ')
        idade = int(input('Idade do PET: '))
        pet = {'tipo': tipo,        # cria o dicionario
                'nome': nome, 
                'idade': idade}
        
        lista_pets.append(pet)      # insere o dicionario pet na lista

        # gera o arquivo json
        with open('pets.json', 'w', encoding='utf-8') as arquivo:
            json.dump(lista_pets, arquivo, indent=4, ensure_ascii=False) 
    except FileNotFoundError:
        print('ERRO: Arquivo não localizado.')
    except ValueError:
        print('ERRO: A idade deve ser um numero inteiro.')
    else:
        print('PET cadastrado com sucesso')


def listar():
    try:
        if os.path.exists('pets.json'):
            with open('pets.json', 'r', encoding='utf-8') as arquivo:
                lista_pets = json.load(arquivo)
                if len(lista_pets) == 0:
                    print('Não há PETS cadastrados')
                else:
                    for pet in lista_pets:
                        print('------------------------------')
                        print(f'Nome: {pet["nome"]}')
                        print(f'Tipo: {pet["tipo"]}')
                        print(f'Idade: {pet["idade"]}')
        else:
            print('Não há PETS cadastrados')
    except FileNotFoundError:
        print('ERRO: Arquivo não localizado.')


def excluir():
    try:
        if os.path.exists('pets.json'):         # verifica se oa rquivo ja existe
            with open('pets.json', 'r', encoding='utf-8') as arquivo:
                lista_pets = json.load(arquivo)
        else:
            lista_pets = []

        if len(lista_pets) == 0:
            print('Não há PETS cadastrados')
        else:
            nome = input('Informe o nome do PET que será excluído: ')
            achou = False
            for pet in lista_pets:
                if pet['nome'] == nome:
                    lista_pets.remove(pet)
                    achou = True
                    break
            
            if achou == False:
                print(f'O pet de nome {nome} não está cadastrado')
            else:
                with open('pets.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(lista_pets, arquivo, indent=4, ensure_ascii=False)
                print('PET excluído com sucesso')
    except FileNotFoundError:
        print('ERRO: Arquivo não localizado.')


while True:
    print('\n1 - Inserir')
    print('2 - Excluir')
    print('3 - Listar Todos')
    print('4 - Sair')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            inserir()
        case 2:
            excluir()
        case 3:
            listar()
        case 4:
            print('Fim do Programa')
            break
        case _:
            print('Opção inválida')