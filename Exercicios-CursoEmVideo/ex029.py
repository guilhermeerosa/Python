#Verifica se a velocidade está acima da permitida e calcula o valor da multa

#Cabeçalho
print('-=-'*6)
print('CALCULO DE MULTA')
print('-=-'*6)

#Recebe o valor da velocidade
vel = float(input('Digite a velocidade do carro em Km/h: '))

#Caso acima da velocidade permitida
if vel >= 80:
    print('Você estava acima da velocidade permitida de 80Km/h e você foi multado!')
    print('A sua multa é de R${:.2f}!'.format((vel - 80) * 7))

#Caso dentro da velocidade permitida
else:
    print('Você estava na velocidade permitada, boa viagem!')
