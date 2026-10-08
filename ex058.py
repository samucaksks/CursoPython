sexo = input('Digite seu sexo (M/F): ').strip().upper()
while sexo not in 'MF':
    sexo = input('Sexo inválido. Por favor, digite M ou F: ').strip().upper()