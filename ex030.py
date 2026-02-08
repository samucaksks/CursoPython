vel = int(input("Qual a sua velocidade, em km/h? "))
mais = vel - 80
multa = mais * 7
if vel > 80:
    print("vc foi multado por estar dirigindo em {} km/h".format(vel))
    print("vc pagara R${}".format(multa))
else:
    print("parabens vc está andando na velocidade indicada")
