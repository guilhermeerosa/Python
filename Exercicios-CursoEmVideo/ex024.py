#Verifica se o nome da sua cidade começa com Santo
local = str(input('Digite o nome do local: ')).strip().split()
print(local[0].lower() == 'santo')