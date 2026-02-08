import random
alunos = input("Qual é o nome do primeiro aluno? ")
aluno2 = input("Do segundo? ")
aluno3 = input("do terceiro? ")
aluno4 = input("do quarto? ")
lista = [alunos, aluno2, aluno3,aluno4]
sorteio = random.choice(lista)
print("O {} vai apagar a lousa".format(sorteio))