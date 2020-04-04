#Calcula média de duas notas
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Você tirou {:.1f} na primeira nota e {:.1f} na segunda nota.\nSua média foi {:.1f}.'.format(n1, n2, m))