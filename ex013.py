preço = float(input("me fale o preço do produto que vc quer comprar"))
desconto = preço * 0.05
final = preço - desconto
print("o valor final vai ser de {:.2f}".format(final))