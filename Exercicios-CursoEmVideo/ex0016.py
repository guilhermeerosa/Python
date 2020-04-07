#Verifica a parte inteira do numero decimal
from math import trunc
num = float(input('Digite um numero decimal: '))
int = trunc(num)
print('A parte inteira de {} é {}.'.format(num, int))
