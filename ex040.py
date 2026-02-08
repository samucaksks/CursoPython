from datetime import date
data_de_hoje = date.today().year
nascimento = int(input("Qual é o ano do seu nascimento? "))
idade = data_de_hoje - nascimento
militar = input("Você ja serviu ao exercito? RESPONDA COM SIM OU NÃO ").upper()
if idade < 18:
    falta = 18 - idade
    print("Por sorte vc AINDA não tem idade para se alistar ao exercito, ainda falta {} anos".format(falta))
elif idade == 18 and (militar == "NÃO" or "NAO"):
    print("Você está pronto para se alistar no exercito \033[0;32mboa sorte\033[m")
elif idade >= 18 and militar == "SIM":
    print("Bom, você já serviu ao exercito, não precisa se alistar denovo ")
    print("\033[0;33mParabens")
elif idade > 18 and (militar == "NÃO" or "NAO"):
    falta = idade - 18
    print("Você ainda \033[0;31mNÃO\033[m seriu o exercito com essa idade, caramba, enfim você passou do prazo por \033[0;31m{}\033[m ANOS".format(falta))
