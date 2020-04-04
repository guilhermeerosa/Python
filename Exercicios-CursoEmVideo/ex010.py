#Converor real para dolar
real = float(input('Quantos reais você possui na carteira? R$ '))
dolar = real / 5.15
print('Você possui R${:.2f}, o que equivale a U${:.2f}.'.format(real, dolar))
