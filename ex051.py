soma = 0
cont = 0
for i in range(1, 7):
    a = int(input('digite o numero {}'.format(i)))
    if a % 2 == 0:
        soma += a
        cont += 1
print('vc informou {} números pares e a soma deles é: {}'.format(cont, soma))

