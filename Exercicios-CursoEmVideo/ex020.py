#Sorteia uma ordem dos nomes apresentados
from random import shuffle
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
ordem = [al1, al2, al3, al4]
shuffle(ordem)
print('A ordem de apresentação será: {}!'.format(ordem))
