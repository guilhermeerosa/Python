#Conversor de metros para centimentros e milimetros
m = float(input('Digite o valor em metros: '))
cm = m * 100
mm = m * 1000
print('Você escolheu {}m, o que equivale a {:.0f}cm ou {:.0f}mm.'.format(m, cm, mm))
