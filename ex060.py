n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
c = 0
while c != 5:
    print('[1]somar \n[2]subtrair \n[3]maior número \n[4]digitar novos numeros \n[5]sair')
    c = int(input("Enter the option: "))
    if c == 1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif c == 2:
        print(f"{n1} - {n2} = {n1-n2}")
    elif c == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n2 > n1:
            print(f"{n2} é maior que {n1}")
        else:
            print("Os números são iguais.")
    elif c == 4:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter a number: "))
    elif c > 5:
        print("Opção inválida, tente novamente.")
    elif c < 1:
        print("Opção inválida, tente novamente.")
print("Saindo do programa...")