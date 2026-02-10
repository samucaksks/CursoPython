import datetime
contador = 0
contador1 = 0
for i in range(1,8):
    a = int(input('\033[mqual seu ano de nascimento? '))
    idade = datetime.date.today().year - a
    if idade >= 18:
        print('\033[32mmaior de idade\033[m')
        contador += 1
    elif idade >= 0:
        print('\033[031mmenor de idade\033[m ')
        contador1 += 1
    else:
        print('\033[031minválido\033[m ')
print('\n\033[m{} pessoas são maiores de idade'.format(contador))
print('{} pessoas não são maiores de idade'.format(contador1))



