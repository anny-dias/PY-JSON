'''Exercício 1 
Considere que o arquivo “notas.CSV” apresenta uma listagem com os dados dos alunos de uma turma. 
Cada linha do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Implemente um programa que leia este arquivo e gere um novo arquivo JSON no formato:
{
 "2101254": {
 "nome": "Benicio Pires",
 "notas": [
 3.6,
 10.0,
 8.5,
 7.0
 ]
 },
 "2101624": {
 "nome": "Bruna Goncalves",
 "notas": [
 9.5,
 8.0,
 6.0,
 5.5
 ]
 }
}
'''