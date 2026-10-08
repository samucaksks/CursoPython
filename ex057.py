soma_idade = 0
maior = 0
garotas = 0
nome_maior = ''
nome_maior2 = ''
for i in range(1, 6):
    nome = input('qual seu nome ')
    idade = int(input('qual sua idade '))
    sexo = input('qual seu sexo [M/F]: ').upper()
    print('=-'*20)

    soma_idade += idade
    if sexo == 'F' and idade < 20:
        garotas += 1

    if sexo == 'M':
        if nome_maior == '':
            maior = idade
            nome_maior = nome
        else:
            if idade > maior:
                maior = idade
                nome_maior = nome
            if idade == maior:
                nome_maior2 = nome

media = soma_idade / 5
print('A média das idades é {:.1f}'.format(media))
if nome_maior2 != '':
    print(f'os homens com maior idade são {nome_maior} e {nome_maior2}')
else:
    print(f'o homem com maior idade é {nome_maior}')
print(f'a quantidade de mulheres com menos de 20 anos é: {garotas}')
