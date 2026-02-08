from datetime import date
ano = int(input("me fale o ano que vc quer analisar, sé quiser o seu ano tecle 0  " ))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O anos {} não é bissexto".format(ano))
