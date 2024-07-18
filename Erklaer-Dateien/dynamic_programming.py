def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def dynamic_fibonacci(n, mem=None):
    if mem is None:
        mem = {}

    if n in mem:
        return mem[n]

    if n <= 1:
        mem[n] = n
        return n

    else:
        f = dynamic_fibonacci(n-1, mem) + dynamic_fibonacci(n-2, mem)
        mem[n] = f
        return f


print(dynamic_fibonacci(100))
