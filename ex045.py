
preço = float(input("qual é o preço do produto que vc quer comprar? "))
forma = input("Qual é a forma de pagamento.Sendo elas: Cartão, cheque ou dinheiro").upper()
if forma in ("CHEQUE", "DINHEIRO"):
    porcentagem = preço * 0.10
    novo = preço - porcentagem
    print("como você vai pagar com {} você pagara {:.2f}, pois está com 10% de desconto".format(forma, novo))

elif forma in ("CARTÃO", "CARTAO"):
    àvista = input("Sera á vista ou parcelado? ").upper()

    if àvista in ("À VISTA", "AVISTA", "ÀVISTA", "ÁVISTA", "À VISTA"):
        porcentagem = preço * 0.05
        novo = preço - porcentagem
        print("como você está comprando no cartão à vista, você pagará {:.2f}, pois está com 5% de desconto".format(novo))
    elif àvista == "PARCELADO":
        parcelado = input("Sera parcelado em quantas vezes? ").upper()

        if parcelado == "2" or parcelado == "2X":
                valor_parcela = preço / 2
                print("Você pagará 2 parcelas de {:.2f} reais cada, totalizando {:.2f} reais".format(valor_parcela, preço))
        else:
                juros = preço * 0.20
                novo = preço + juros
                valor_parcela = novo / int(parcelado)
                print("Você pagará {:.2f} reais ao todo, com 20% de juros".format(novo))
                print("Serão {} parcelas de {:.2f} reais cada".format(parcelado, valor_parcela))
else:
    print("Essa forma de pagamento não existe")


