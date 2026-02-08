nome = input("qual é o seu nome completo")
print(nome.upper())
print(nome.lower())
divir = nome.split()
divir1 = divir[0]
print("seu nome é",divir[0], "é ele tem {} letras".format(divir1[len(divir1) - 1]))
espaços = (nome.replace(" ", ""))
print(len(espaços))