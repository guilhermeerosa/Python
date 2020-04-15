#Verifica a quantidade de letras "a", a sua primeira e ultima posição
frase = str(input('Digite uma frase: ')).strip()
print('A letra "a" aparece {} vezes.'.format(frase.lower().count('a')))
print('O primeiro "a" está na posição: ', frase.lower().find('a') + 1)
print('O ultimo "a" está na posição: ', frase.lower().rfind('a') + 1)
