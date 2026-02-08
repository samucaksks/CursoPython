import random
aluno1 = input("me fale um nome")
aluno2 = input("me fale outro")
aluno3 = input("me fale outro")
aluno4 = input("me fale outro")
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print("a sequencia sera assim")
print(lista)