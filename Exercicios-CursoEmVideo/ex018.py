#Calcula o cosseno, seno e tangente de um angulo
from math import cos, sin, tan, radians
angulo = int(input('Qual é o angulo? '))
c = cos(radians(angulo))
s = sin(radians(angulo))
t = tan(radians(angulo))
print('O angulo {}º tem cosseno {:.2f}, seno {:.2f} e tangente {:.2f}.'.format(angulo, c, s, t))
