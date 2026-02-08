salario = float(input("qual e o seu salario?"))
aumento = salario * 0.15
final = aumento + salario
print("seu salario era {:.2f} mas voce ganhou um aumento e ficou com {:.2f} ".format(salario, final))