nome = input("qual é o seu nome completo")
separar = nome.split()
nome1 = separar[0]
nome2 = separar[len(separar) - 1]
print("O seu primeiro nome é {} é o ultimo é {} ".format(nome1, nome2))
