import math

# a

k0 = 1000
k = 2000
n = 5

p = (k/k0)**(1/n) - 1
print(p)

# b

k0 = 2000
n = 10

k = k0 * (1+p)**n
print(round(k, 2))

# c

k0 = 10_000
k = 1_000_000

n = math.log(k/k0, 1+p)
print(math.ceil(n))
