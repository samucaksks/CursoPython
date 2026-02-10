num = int(input('digite um número: '))
tot = 0
for i in range(1, num +1):
    if num % i == 0:
        print('\033[33m ', end='')
        tot += 1
    else:
        print('\033[31m ', end='')
    print('{}'.format(i), end ='')
print('\n\033[mo número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('ele é primo')
else:
    print('não é primo')