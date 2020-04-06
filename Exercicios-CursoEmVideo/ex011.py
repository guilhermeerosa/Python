#Calcula m² da parede e quanto de tinta é necessario
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
print('A parede tem {}m de largura, {}m de altura, totalizando {}m².'.format(l, a, area))
print('Sabendo que cada litro de tinta pinta 2m², você precisará de {} litros de tinta.'.format(area / 2))
