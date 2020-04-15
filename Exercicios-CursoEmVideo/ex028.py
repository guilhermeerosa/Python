#Jogo de tentar adivinhar
from random import randint
from time import sleep

#Cabeçalho
print('-=-'*19)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*19)

#Escolha do jogador
escolha = int(input('Escolha um numero: '))
print('PROCESSANDO...')
sleep(2)

#Escolha do computador
comp = randint(0,5)

#Apresentação
print('Você escolheu o numero {}.'.format(escolha))
print('Eu escolhi o numero {}'.format(comp))

#Ganhou ou perdeu
if escolha == comp:
    print('Parabéns, você ganhou!')
else:
    print('Que pena, você perdeu!')
