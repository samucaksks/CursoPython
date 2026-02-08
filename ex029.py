import random
numero_escolhido = random.randint(1, 5)
print("eu acabei de escolher um numero entre 1 e 5 tente adivinha-lo")
escolha = int(input("me fale o numero que vc acha que escolhi: "))
if escolha == numero_escolhido:
    print("voce acertou, parabens")
else:
    print("voce errou, eu escolhi o número {}".format(numero_escolhido))
