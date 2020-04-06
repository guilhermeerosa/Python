#Calcula valor do aluguel do carro
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)
print('O valor total a ser pago é R${:.2f}!'.format(total))
