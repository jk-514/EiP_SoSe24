import random

name1 = input("Name 1: ")
name2 = input("Name 2: ")
name3 = input("Name 3: ")

z = random.randint(1, 4)

if z == 1:
    print(f"Hello {name1}")
elif z == 2 or z == 3:
    print(f"Hello {name2}")
else:
    print(f"Hello {name3}")
