dishes = [('Wedges', 4.5, 105), ('Kartoffeln', 2, 72), ('Buntes Gemüse', 1.5, 72), ('Gemüsesuppe', 2, 72), ('Hausgemachte Käsespätzle', 5, 306), ('Tagesmenü', 4, 378), ('Hausgemachter Weißer Bohneneintopf', 2.5, 222), ('Gebratenes Seelachsfilet', 0, 374), ('Auswahl an angemachten Salaten', 1.7, 89)]

#dishes = sorted(dishes, key=lambda x: x[2])

g = [dish[1] for dish in dishes]
p = [dish[2] for dish in dishes]

def R(i: int, P: int) -> float:
    if P == 0 or i == 0:
        return 0
    elif p[i - 1] > P:
        return R(i - 1, P)
    return max(R(i - 1, P), R(i - 1, P - p[i - 1]) + g[i - 1])
    # Laufzeit in O(2^n), wobei n = Anzahl Gerichte -> exponentielle Laufzeit


n = len(dishes)
P_max = 500

print(f"Rekursiv: {R(n, P_max)}")



# c)
def R_dynamic(i: int, P_max: int):
    R = [[0 for col in range(P_max + 1)] for row in range(i + 1)]

    for j in range(1, i + 1):
        for P in range(1, P_max + 1):
            if p[j - 1] > P:
                R[j][P] = R[j - 1][P]
            else:
                R[j][P] = max(R[j - 1][P], R[j - 1][P - p[j - 1]] + g[j - 1])

    return R[i][P_max], R
    # Laufzeit in O(i * P_max) -> pseudopolynomielle Laufzeit


max_g, R = R_dynamic(n, P_max)

print(f"Dynamisch: {max_g}")

indices_best_dishes = []
row = n
col = P_max
current = R[row][col]

while current != 0:
    if current == R[row-1][col]:
        row -= 1
        current = R[row][col]
    else:
        current -= g[row-1]
        row -= 1

        indices_best_dishes.append(row)

        for i in range(len(R[row])):
            if R[row][i] == current:
                col = i
                break


best_dishes = [dishes[i] for i in indices_best_dishes]
costs = sum([dish[2] for dish in best_dishes])

print(f"Optimale Auswahl: {best_dishes}")
print(f"Kosten: {costs}")





