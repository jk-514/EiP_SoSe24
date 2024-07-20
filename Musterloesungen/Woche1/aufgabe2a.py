import random

name1 = input("Name 1: ")
name2 = input("Name 2: ")

# Möglichkeit 1

z = random.randint(0, 1)

if z == 0:
    print(name1)
else:
    print(name2)

# Möglichkeit 2

print(random.choice((name1, name2)))

