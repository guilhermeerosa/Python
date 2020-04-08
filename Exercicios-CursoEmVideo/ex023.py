#Verifica Unidade/Dezena/Centena/Milhar
num = int(input('Digite um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}\nSua unidade é: {}\nSua dezena é: {}\nSua centena é: {}\nSua milhar é: {}'.format(num, u, d, c, m))
