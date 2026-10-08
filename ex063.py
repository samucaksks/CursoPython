pt = int(input("primeiro termo: "))
r = int(input("razão: "))
c = 10
while c > 0:
    print(f"{pt}", end=' -> ' if c > 1 else '\n')
    pt += r
    c -= 1
a = int(input("Quantos termos você quer mostrar a mais? "))
while a > 0:    
    print(f"{pt}", end=' -> ')
    pt += r
    a -= 1
print("FIM")