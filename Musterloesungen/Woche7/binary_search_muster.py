def binary_search_rec(lst, x, l, r):
    if l == r:
        return l if x == lst[l] else -1
    m = (l+r)//2
    if x == lst[m]:
        return m
    if x < lst[m]:
        return binary_search_rec(lst, x, l, m)
    return binary_search_rec(lst, x, m+1, r)

l = [7,9,11,13,15,17,19,22,25]
# print(all(binary_search_rec(l,x, 0, len(l)-1) != -1 for x in l))
# print(binary_search_rec(l, 15, 0, len(l)-1))
