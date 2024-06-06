import random


def my_abs(n: int) -> int:
    if n < 0:
        return -n
    return n


def manhattan_norm(x: int, y: int) -> int:
    return my_abs(x) + my_abs(y)


def my_zip(a: list, b: list) -> list[tuple]:
    if len(a) < len(b):
        n = len(a)
    else:
        n = len(b)

    out = []
    for i in range(n):
        out.append((a[i], b[i]))
    return out


def my_map(f, l: list) -> list:
    out = []
    for i in l:
        out.append(f(i))
    return out


l1 = [random.randint(-10, 10) for _ in range(10)]
l2 = [random.randint(-10, 10) for _ in range(10)]
