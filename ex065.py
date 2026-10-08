a = soma = cont = 0
a = int(input("Enter a number: "))
while a != 999:
    cont += 1
    soma += a
    a = int(input("Enter a number: "))
print(f"FIM! You entered {cont} numbers and the sum of them is {soma}.")