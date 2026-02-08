numero = int(input("Digite o número que você deseja:"))
base = int(input("Qual base vc quer transformar? Binaria (digite 1) octal (digite 2) hexadecimal (digite 3) "))
lista = []
if numero == 0:
    print("0")
    exit()
if base == 1:
    while numero > 0:
        resto = numero % 2
        numero = numero // 2
        lista.append(str(resto))
elif base == 2:
    while numero > 0:
        resto = numero % 8
        numero = numero // 8
        lista.append(str(resto))
elif base == 3:
    while numero > 0:
        resto = numero % 16
        numero = numero // 16
        if resto < 10:
            lista.append(str(resto))
        else:
            hexade = chr(resto + 55)
            lista.append(str(hexade))
else:
    print("essas não é uma das opções")
lista.reverse()
print("".join(lista))


