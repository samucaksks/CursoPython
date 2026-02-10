from time import sleep
a = float(input("Quanto é o tamanho do primeiro segmento? "))
b = float(input("Qual é o tamanho do segundo segmento? "))
c = float(input("Qual é o tamnho do terceiro segmento? "))
if a + b > c and a + c > b and b + c > a:
    print("Eles formam um triangulo")
    if a == b and b == c:
        print("O triangulo é um EQUILATERO")
    elif a != b and b != c and a != c:
        print("O triangulo é um ESCALENO")
    else:
        print("O triangulo é um ISÓSCELES")
else:
    print("Com esse conjunto de segmentos não é possivel criar um triangulo")
sleep(2)
input("Pressione ENTER para sair")