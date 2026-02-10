maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi {}'.format(maior))
print('o menor peso lido foi {}'.format(menor))