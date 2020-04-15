#Verifica se um numero é par ou impar

#Cabeçalho
print('-=-'*5)
print('Par ou Impar?')
print('-=-'*5)

#Escolha do numero
num = int(input('Escolha um numero inteiro: '))

#Verifica se o numero é par ou impar
div = num % 2
if div == 0:
    print('O numero escolhido foi {} e ele é PAR!'.format(num))
else:
    print('O numero escolhido foi {} e ele é IMPAR!'.format(num))
