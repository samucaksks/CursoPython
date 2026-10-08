n = int(input("Enter a number: "))
c = n
f = 1
print(f"Calculating the factorial of {n}...")
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f"{f}")