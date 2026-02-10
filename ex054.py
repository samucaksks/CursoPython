fras = input('frase: ').strip().upper()
palavras = fras.split()
junto = "".join(palavras)
inv = ''
for letra in range(len(junto)-1, -1, -1):
    inv += junto[letra]
if inv == junto:
    print('{} é um palíndromo'.format(fras))
else:
    print('{} não é um palíndromo'.format(fras))
