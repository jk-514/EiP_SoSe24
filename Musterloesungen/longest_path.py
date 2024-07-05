def is_valid(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j] == 1
    # Wir testen hier, dass sich die Position (i, j) innerhalb der Matrix befindet. Wenn das der Fall ist, schauen wir
    # noch, dass an dieser Stelle eine 1 steht, was suggeriert, dass wir dieses Feld betreten dürfen.


def get_valid_cells(matrix, i, j):
    # Mal etwas schöner als während der Übungsstunde
    output = []
    # Alle Richtungen als Vektoren
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    # Wir testen für jede Richtung, ob wir dahin gehen können und wenn das der Fall ist, fügen wir es zur Output-Liste
    # hinzu. Auf diese Weise werden nur jene Zellen zurückgegeben, die erlaubt sind, was die is_zulässig-Prüfung in der
    # dfs-Funktion überflüssig macht.
    for vec in directions:
        new_pos = i+vec[0], j+vec[1]
        if is_valid(matrix, *new_pos):
            output.append(new_pos)

    return output


def longest_route(matrix, start, target):
    def dfs(matrix, steps, i, j):
        # Teste, ob das aktuelle Feld nicht betreten werden darf. Ist nur relevant, um auszuschließen, dass der Start
        # bereits nicht erlaubt ist.

        if matrix[i][j] == 0:
            return 0

        # Teste, ob wir fertig sind. Das ist der Fall, wenn der Start gleich dem Ziel ist.
        if (i, j) == target:
            return steps

        next_positions = get_valid_cells(matrix, i, j)

        # next_positions ist jetzt eine Liste, die alle Erweiterungsmöglichkeiten repräsentiert.

        longest_path = 0
        # Der von hier aus längste Pfad zum Ziel wird mit 0 initialisiert, da wir uns bisher nicht bewegt haben.

        matrix[i][j] = 0
        # Das aktuelle Feld darf nicht noch mal betreten werden.

        # for each Erweiterungsmöglichkeit(E)
        for new_pos in next_positions:
            # In dem max finden wir dann den Schritt vervollständige(K)
            longest_path = max(longest_path, dfs(matrix, steps+1, *new_pos))

        # jetzt kommen wir zu mache_rückgängig. Da i, j nicht verändert wurden, müssen wir nur die Markierung wieder
        # aufheben

        matrix[i][j] = 1
        return longest_path

    return dfs(matrix, 0, *start), pred

    # Der Fehler, den ich während der Übung gemacht habe, war, dass ich matrix[i][j] = 0 erst vergessen hatte und dann
    # vergessen hatte, matrix[i][j] = 1 am Ende hinzuzufügen, was dem mache_rückgängig-Schritt entspricht.

    # Daher kamen wir in eine infinite-Recursion, da es von jeder Position aus unendlich viele Pfade gegeben hat. Das
    # tut mir leid. Hab den Fehler literally 2 Minuten nach Ende der Übung gesehen. Das ist etwas blöd gelaufen.


### from here it's just testing
matrix = [
[
    [1,0,0],
    [1,1,1],
    [1,1,1]
],
[
	[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
	[1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
	[1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
],
    [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1], 
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1], 
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], 
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
],
[
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1], 
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1], 
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], 
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
]

start_target = [[(0,0),(2,2)],[(0,0),(5,7)],[(9,8),(0,0)], [(0,0), (8,3)]]
expected = [6, 22, 0, 29]

for ex, st, m in zip(expected, start_target, matrix):
    length, pred = longest_route(m, *st)
    print(f'expected length: {ex}, computed length: {length}, match: {length == ex}')
