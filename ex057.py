soma_idade = 0
maior = 0
menor = 0
mujeres = 0
nome_maior = ''
for i in range(1, 6):
    nome = input('qual seu nome')
    idade = int(input('qual sua idade'))
    sexo = input('qual seu sexo [M/F]: ').upper()

    soma_idade += idade
    if sexo == 'F' and idade < 20:
        mujeres += 1

    if sexo == 'M':
        if nome_maior == '':
            maior = idade
            nome_maior = nome
        else:
            if idade > maior:
                maior = idade
                nome_maior = nome

media = soma_idade / 5
print('A média das idades é {:.2f}'.format(media))
print('o homem com maior idade é {}'.format(nome_maior))
print('a quantidade de mulheres com menos de 20 anos é: {}'.format(mujeres))
