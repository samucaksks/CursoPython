casa = float(input("Digite o valor da casa que o senhor(a) deseja "))
salario = float(input("Digite o quanto vc ganha por mes "))
anos = int(input("Digite até quantos anos vc pagará pela casa "))

meses = anos * 12
prestacao =  casa / meses
porcentagem = salario * (30 / 100)
if prestacao <= porcentagem:
    print("vc podera pagar")
else:
    print("Foi recusado vc nao podera pagar a casa")
