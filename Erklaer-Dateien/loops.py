import random

# Python unterscheidet zwischen 2 Arten von Schleifen: for- und while-Schleifen

# While-Schleifen:

# While-Schleifen haben eine Schleifenbedingung. Diese sieht so aus wie bei einem if. Im Gegensatz zu den if-Statements
# führt eine While-Schleife ihren Code so lange aus, wie die Bedingung wahr ist.

# Ein einfaches Beispiel:

i = 0
while i < 10:
    print(i)
    i += 1

# Erwartungsgemäß gibt die Schleife nacheinander die Zahlen 0-9 aus. Wenn das i jedoch nicht erhöht würde, dann wäre
# die Schleife ein infinite loop, da die Bedingung immer wahr sein wird. Ein anderes typisches Beispiel ist das Spiel
# Zahlenraten.


attempts = 0
secret_number = random.randint(1, 100)

while True:
    guess = int(input('Rate eine Zahl zwischen 1 und 100: '))
    attempts += 1
    if guess < secret_number:
        print('Die gesuchte Zahl ist größer.')
    elif guess > secret_number:
        print('Die gesuchte Zahl ist kleiner.')
    else:
        print(f'Du hast die gesuchte Zahl {secret_number} in {attempts} Versuchen erraten.')
        break

# Hier wird das break-Statement verwendet. Sobald der Code diese Stelle erreicht, wird die Schleife, die gerade
# durchlaufen wird, sofort beendet.

# Neben while-Schleifen gibt es noch for-Schleifen. Bisher wurde in der Vorlesung nur behandelt, wie man mit
# for-Schleifen über eine range iteriert. Das will ich hier noch mal erklären.

for i in range(10):
    print(i)

# Analog zur while-Schleife am Anfang dieser Datei gibt diese for-Schleife die Zahlen 0-9 aus. Was passiert hier?
# Hinter dem for wird die Laufvariable bestimmt. In diesem Fall ist das i, prinzipiell kann man die nennen, wie man
# will. range(10) gibt alle Zahlen zwischen 0 und 9 zurück. In der ersten Iteration hat i dann den Wert 0, in der
# zweiten 1 und so weiter. Die 10 ist exklusiv, wird also nicht mehr mitgezählt. Im Schleifenkörper kann man die
# Laufvariable wie eine normale Variable verwenden; man kann z.B. mathematische Operationen damit ausführen. Man sollte
# nur davon absehen, den Wert der Laufvariable zu verändern, da dies zu unerwartetem Verhalten führen kann.

# Wenn man range() zwei Werte übergibt, dann ist der erste Wert der Startwert (inklusiv) und der zweite der Endwert
# (exklusiv).

for i in range(1, 10):
    print(i)

# Gibt dann die Zahlen 1-9 aus.
# Wenn man range() noch eine dritte Zahl übergibt, dann gibt diese an, um wie viel hoch- oder runtergezählt werden soll.
# Standardmäßig wird immer um 1 hochgezählt. Die folgende Schleife zählt um 2 hoch:

for i in range(0, 10, 2):
    print(i)

# Man kann dieses Verhalten der for-Schleifen natürlich auch mit while-Schleifen darstellen. for-Schleifen haben
# aber einige Vorteile zum Beispiel um Umgang mit Listen (nächste Vorlesung).

# Neben break gibt es auch noch continue. Das continue-Statement sorgt dafür, dass
# die aktuelle Iteration übersprungen wird und der Code stattdessen zur nächsten Iteration springt. Ein Beispiel:

for i in range(10):
    if i == 3:
        continue
    print(i)

# Wenn i den Wert 3 annimmt, ist die if-Bedingung wahr und der Code erreicht das continue und überspringt daher
# die aktuelle Iteration. Daher wird die 3 nicht durch das print() ausgegeben.

# Hier ist noch ein Beispiel:

_sum = 0
for i in range(1, 11):
    _sum += i
print(_sum)

# Berechnet die Summe der Zahlen von 1 bis 10

# Hier könnt ihr noch mehr nachlesen:
# For-loops:            https://www.w3schools.com/python/python_for_loops.asp
# While-loops:          https://www.w3schools.com/python/python_while_loops.asp
# Prinzipiell ist es immer ratsam, in der offiziellen Python-Dokumentation zu lesen, aber da werden bei den Schleifen
# Vorkenntnisse zu Listen vorausgesetzt.

# Hier sind noch ein paar YouTube-Videos:
# For-loops:            https://www.youtube.com/watch?v=KWgYha0clzw
# While-loops:          https://www.youtube.com/watch?v=rRTjPnVooxE
# break, continue:      https://www.youtube.com/watch?v=97NdNoA3XUQ
