#Escolha aleatória de 4 alunos com biblioteca random/choice
from random import choice
al1 = input('Nome do primeiro aluno? ')
al2 = input('Nome do segundo aluno? ')
al3 = input('Nome do terceiro aluno? ')
al4 = input('Nome do quarto aluno? ')
escolha = choice([al1, al2, al3, al4])
print('O aluno escolhido foi: {}!'.format(escolha))
