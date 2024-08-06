def func1(a: int, b: int) -> int:
    c = 1
    while a < b:
        if a % 2 == 0:
            c += 1
        else:
            c *= 2
        a += 1

    return c


def func2(a: int, b: int, c: int) -> int:
    while a < b:
        a += 1
        if a % 2 == 0:
            c += 1
        else:
            c *= 2

    return c


def func3(a: int, b: int, c: int) -> int:
    if a > b:
        return c
    if a + b > c:
        c += 1
    else:
        c *= 2

    c *= 3
    return c - a + b
