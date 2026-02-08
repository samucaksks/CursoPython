a = int(input("Qual é o valor da primeira seta?: "))
b = int(input("Qual é o valor da segunda seta?: "))
c = int(input("Qual é o valor da terceira seta?: "))
if a + b > c:
    if a + c > b:
        if c + b > a:
            print("As suas setas formam um triangulo")
        else:
            print("As setas que vc citou não formam um triangulo")
    else:
        print("As setas que vc citou não formam um triangulo")
else:
    print("As setas que vc citou não formam um triangulo")
