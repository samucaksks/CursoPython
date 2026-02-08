viagem = int(input("Quantos km vai ter a sua viagem? "))
if viagem <= 200:
    f1 = viagem * 0.50
else:
    f1 = viagem * 0.45
print("a sua passagem custara {}".format(f1))
