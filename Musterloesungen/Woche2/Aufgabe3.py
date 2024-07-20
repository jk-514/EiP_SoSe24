# a

n = 12345612
p = 2

print(f"Primfaktorzerlegung von {n}:")

while n > 1:
    if n % p == 0:
        print(p)
        n //= p
    else:
        p += 1

# b

n = 496

acc = 0
for i in range(1,n):
    if n % i == 0:
        acc += i

print()
if n == acc:
    print(f"{n} ist perfekt")
else:
    print(f'{n} ist nicht perfekt')
