import random
numero_escolhido = random.randint(1, 10)
print("eu acabei de escolher um numero entre 1 e 10 tente adivinha-lo")
escolha = int(input("me fale o numero que vc acha que escolhi: "))
c = 0
while escolha != numero_escolhido:
    c += 1
    escolha = int(input("errado, vamos tentar denovo.\nme fale o numero que vc acha que escolhi: "))
print(f"Parabéns! Você acertou o número em {c} tentativas.")