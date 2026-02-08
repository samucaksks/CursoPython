numero = int(input("digite um numeros: "))
numero1 = int(input("digite outro numeros: "))
numero2 = int(input("digite outro numeros: "))
if numero > numero1 > numero2:
    print("{} > {} > {}".format(numero, numero1, numero2))
if numero1 > numero2 > numero:
    print("{} > {} > {}".format(numero1, numero2, numero))
if numero > numero2 > numero1:
    print("{} > {} > {}".format(numero, numero2, numero1))
if numero1 > numero > numero2:
    print("{} > {} > {}".format(numero1, numero2, numero))
if numero2 > numero > numero1:
    print("{} > {} > {}".format(numero2, numero, numero1))
if numero2 > numero1 > numero:
    print("{} > {} > {}".format(numero2, numero1, numero))
