dias = int(input("quantos dias voce usou o carro? "))
km = float(input("quantos km vc rodou? "))
dias1 = dias * 60
km2 = km * 0.15
final = dias1 + km2
print("voce usou {} dias e rodou {} km totalizando no valor de {:.2f} reais para ser pago".format(dias, km, final))