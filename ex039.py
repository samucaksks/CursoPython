n1 = int(input("Me fale o primerio numero"))
n2 = int(input("Me fale o segundo numero"))
if n1 > n2:
    print("O número \033[0;32m{}\033[m é maior do que o numero \033[0;31m{}\033[m".format(n1, n2))
elif n2 > n1:
    print("O número \033[0;32m{}\033[m é maior do que o número \033[0;31m{}\033[m".format(n2, n1))
else:
    print("os números são iguais nao tem diferença entre \033[0;32mmaior\033[m ou \033[0;31mmenor")
