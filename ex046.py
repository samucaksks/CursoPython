import time
import random
print("-=-" * 10)
print("            JOKENPO DO RONALDO")
print("-=-" * 10)
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
usuario = input("Escolha entre papel, pedra e tesoura").upper().strip( )
computador = random.choice(opcoes)
print("JO...")
time.sleep(0.5)
print("KEN...")
time.sleep(0.5)
print("PO!!!")
if usuario == computador:
    print("Vish, deu \033[1;33mEMPATE")
elif (usuario == "PEDRA" and computador == "TESOURA") or (usuario == "PAPEL" and computador == "PEDRA") or (usuario == "TESOURA" and computador == "PAPEL"):
    print("Vocé \033[1;32mganhou\033[m parabens!!!!!!!")
else:
    print("Vish, você \033[1;31mPERDEU")

