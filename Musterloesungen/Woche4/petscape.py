import random

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Speichere alle Richtungen als Vektoren
results = []

for n in range(5, 26):
    escape_counts = 0
    total_steps = 0
    total_perimeter = 0
    simulations = 1000

    for _ in range(simulations):
        x, y = n // 2, n // 2
        visited = [(x, y)]
        steps = 0
        min_x = max_x = x
        min_y = max_y = y
        escaped = False

        while True:

            # Dieser Code läuft bis das Haustier entkommt oder sich nicht mehr bewegen kann.

            possible_moves = [(x + dx, y + dy)
                              for dx, dy in directions
                              if (x + dx, y + dy) not in visited]
            # Wenn ihr nicht versteht, was hier genau passiert, ist das nicht schlimm.
            # Ich habe eine Datei list_comprehension.py, in der ich das erkläre

            if len(possible_moves) == 0:
                break
                # Haustier kann sich nicht mehr bewegen

            x, y = random.choice(possible_moves)
            visited.append((x, y))
            steps += 1
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

            if x < 0 or x >= n or y < 0 or y >= n:
                # Sobald das Haustier die auf der x- oder y-Achse -1 oder n erreicht, hat es die Stadt verlassen
                escaped = True
                break

        if escaped:
            escape_counts += 1
            total_steps += steps
            total_perimeter += 2 * ((max_x - min_x) + (max_y - min_y))

    escape_prob = escape_counts / simulations
    avg_steps = total_steps / escape_counts if escape_counts else 0
    avg_perimeter = total_perimeter / escape_counts if escape_counts else 0
    # Liest sich so: avg_perimeter bekommt den Wert total_perimeter / escape_counts, falls escape_counts den booleschen Wert
    # True zurueckgibt (das tut es, wenn die Zahl nicht 0 ist). Ansonsten wird avg_perimeter auf 0 gesetzt.

    results.append(f"{n}\t{escape_prob:.4f}\t{avg_steps:.2f}\t{avg_perimeter:.2f}")

with open("petscape.txt", "w") as file:
    file.write("n\tescape_probability\taverage_steps\taverage_perimeter\n")
    for result in results:
        file.write(result + "\n")
