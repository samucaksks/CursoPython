a = 'S'
cont = soma = maior = menor = 0
while a in 'S':
    n = int(input("Digite um número: "))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    a = input("Deseja continuar? [S/N] ").upper().strip()
med = soma / cont
print(f"Você digitou {cont} números e a média é {med}.")
print(f"O maior número é {maior} e o menor número é {menor}.")
