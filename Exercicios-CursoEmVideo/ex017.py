#Calcula a Hipotenusa de um triangulo
cateto_oposto = float(input('Digite o valor do Cateto Oposto: '))
cateto_adjacente = float(input('Digite o valor do Cateto Adjacente: '))
h = ((cateto_adjacente ** 2) + (cateto_oposto ** 2)) ** (1/2)
print('O valor da hipotenusa de um triangulo com Catetos {} e {} é {:.2f}!'.format(cateto_oposto, cateto_adjacente, h))
