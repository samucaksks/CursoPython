temperatura = float(input("Me fale uma temperatura em graus "))
f = temperatura * 1.8 + 32
k = temperatura + 273
print("vc escolheu {:.2f} graus, em Fahrenheit fica {:.2f}F e em kelvin fica {:.2f}K".format(temperatura, f, k))