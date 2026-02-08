peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é sua altura? "))
MCI = peso / (altura ** 2)
if MCI < 18.5:
    print("Você está abaixo do peso! Tome cuidado")
elif MCI >= 18.5 and MCI <= 25:
    print("Vocé está com um peso ideal!!!!")
elif MCI > 25 and MCI <= 30:
    print("Você esta com sobrepeso! Tome cuidado")
elif MCI > 30 and MCI <= 40:
    print("Você está com obesidade! Tome cuidado")
else:
    print("Você está com obesidade mórbida!!! Tente se recuperar")