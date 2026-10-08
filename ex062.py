pt = int(input("primeiro termo: "))
r = int(input("razão: "))
c = 10
while c > 0:
    print(f"{pt}", end=' -> ')
    pt += r
    c -= 1
print("FIM")