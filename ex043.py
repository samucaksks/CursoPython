a = float(input("Quanto é o tamanho do primeiro segmento? "))
b = float(input("Qual é o tamanho do segundo segmento? "))
c = float(input("Qual é o tamnho do terceiro segmento? "))
if a + b > c and a + c > b and b + c > a:
    print("Eles fromam um triangulo")
    if a == b and b == c:
        print("O triangulo é um \033[1;32mEQUILATERO")
    elif a != b and b != c and a != c:
        print("O triangulo é um \033[1;32mESCALENO")
    else:
        print("O triangulo é um \033[1;32mISÓSCELES")
else:
    print("Com esse conjunto de segmentos não é possivel criar um triangulo")
