from datetime import date
anos = int(input("Digite o seu ano de nascimento: "))
idade = date.today().year - anos
if idade <= 9:
    print("como você tem {} anos, a sua categoria é \033[1;32mMIRIM".format(idade))
elif idade <= 14:
    print("como você tem {} anos, a sua categoria é \033[1;32mINFANTIL".format(idade))
elif idade <= 19:
    print("como você tem {} anos, a sua categoria é \033[1;32mJUNIOR".format(idade))
elif idade <= 20:
    print("como você tem {} anos, a sua categoria é \033[1;32mSENIOR".format(idade))
else:
    print("como você tem {} anos, a sua categoria é \033[1;32mMASTER".format(idade))
