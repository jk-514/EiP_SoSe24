import random
import time


def timeit(f, n_elems, max_elem):
    acc = 0
    l = random.sample(range(max_elem), n_elems)
    start = time.time()
    f(l)
    acc +=  time.time() - start
    return acc

def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def countingsort(l):
    k = max(l)
    c = [0] * (k+1)
    # count elements
    for num in l:
        c[num] += 1

    # calculate prefix sum (the index of first element of greater value)
    for i in range(1,len(c)):
        c[i] += c[i-1] 

    l4 = [-1] * len(l)

    for v in l:
        # get the last position of the element of value v
        l4[c[v]-1] = v
        # decrease for the next element of value v
        c[v] -= 1
    return l4


def quicksort(l):
    if len(l) <= 1:
        return l
    return quicksort([x for x in l[1:] if x <= l[0]]) + [l[0]] + quicksort([x for x in l[1:] if x > l[0]])

max_elem = 2**19
for i in range(10, 15):
    print(f'----------- N = {2**i} ----------')
    print(f'Quicksort: {timeit(quicksort, 2**i, max_elem)}s')
    print(f'Bubblesort: {timeit(bubblesort, 2**i, max_elem)}s')
    print(f'Countingsort: {timeit(countingsort, 2**i, max_elem)}s')

