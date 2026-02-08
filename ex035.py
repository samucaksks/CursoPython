salario = float(input("Digite o seu salario: "))
if salario >= 1250:
    aumento = salario * (10 / 100)
    novo = salario + aumento
    print("O seu salario erá de \033[31m{:.2f}\033[m e agora será de \033[32m{:.2f}".format(salario, novo))
if salario < 1250:
    aumento = salario * (15 / 100)
    novo = salario + aumento
    print("Os seu salario é de \033[31m{:.2f}\033[m, mas agora será de \033[32m{:.2f}".format(salario, novo))
