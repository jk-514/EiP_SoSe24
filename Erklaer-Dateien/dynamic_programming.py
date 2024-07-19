# Ich erkläre an dieser Stelle noch einmal dynamische Programmierung.
# Die Idee der dynamischen Programmierung ist es, Zwischenergebnisse zu speichern und redundante Rechnungen zu sparen.
# Kurz gesagt wird ein Memory angelegt, also ein Dictionary, das als Keys jeweils n und als Values den Funktionswert von n
# speichert.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Die Fibonacci-Funktion ist recht ineffizient. Beheben wir das mal.


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


# Als Übungsaufgabe kann man die Fibonacci-Funktion iterativ implementieren, was je nach Implementierung sogar noch
# effizienter sein kann.

# Ein anderes Beispiel:


def func(n):
    if n <= 1:
        return 42
    else:
        return max(func(n-2) + 1, func(n-1) + 2)


# Diese Funktion hat keinen tieferen Sinn, aber sie hat offensichtlich Potenzial, verbessert zu werden. Machen wir also
# auch das mit einem Memory.


def dynamic_func(n, mem=None):

    # Dafür sorgen, dass jedes Mal, wenn die Funktion aufgerufen wird, ein neues Memory erstellt wird.
    # Prinzipiell ist es möglich, mem auch ein leeres Dictionary als Standardwert zu geben.
    # Das Problem ist, dass das nicht so funktioniert wie erwartet. Es wird dann nicht jedes Mal, wenn nichts für mem
    # angegeben wird, ein neues Dictionary angelegt, sondern es wird immer dasselbe genommen, sobald es einmal erzeugt wurde.
    # Bei mutablen Datentypen kann dies zu unerwartetem Verhalten führen. In diesem Fall wäre das nicht weiter tragisch,
    # es würde die Funktion bei wiederholter Ausführung sogar schneller machen, aber es ist keine gute Praxis, weil es
    # im Allgemeinen zu unerwartetem Verhalten führt.
    # Wenn hingegen immutable Datentypen verwendet werden, besteht dieses Problem eben nicht.

    # Erinnerung: Strings, Ints, Floats, Complex, Tupel und None sind immutable, während Listen, Sets und Dictionaries mutable sind

    if mem is None:

        # Was ist eigentlich der Unterschied zwischen == und is?
        # == fragt ab, ob zwei Objekte denselben Wert haben, wenn z.B. zwei Variablen x und y beiden den Wert 42 haben, dann
        # würde == True liefern. is fragt ab, ob zwei Objekte denselben Zeiger haben, also auf denselben Ort im Speicher verweisen.
        # Wenn x und y zwei unterschiedliche Variablen sind, liefert das False. Im Fall von None ist der Zeiger leer, daher ist
        # eine gute Praxis is zu nutzen (== geht auch, ist aber unschön)

        mem = {}

    # Es gibt jetzt einen neuen Basisfall für die Funktion, und zwar, dass der Wert bereits berechnet wurde.

    if n in mem:
        return mem[n]

    # Der bereits bestehende Basisfall wird darum ergänzt, dass das Ergebnis ins Memory geschrieben wird.

    if n <= 1:
        mem[n] = 42
        return 42

    else:
        # analog
        mem[n] = max(dynamic_func(n-2, mem) + 1, dynamic_func(n-1, mem) + 2)

        # Da Dicts mutable sind, kann das Memory in den Rekursionsschritten beschrieben werden und muss nicht zurückgegeben werden
        # Siehe auch Referenzsemantik (VL)

        # Wichtig: Den Wert aus dem Memory ausgeben und nicht noch mal berechnen, kostet sonst unnötig Zeit und gerade die
        # wollen wir sparen.
        return mem[n]


# Übungsaufgaben:
# Hier sind (mehr oder weniger sinnvollen) Funktionen gegeben. Verbessern Sie die Laufzeit mit dynamischer Programmierung.


def a(n):
    if n < 10:
        return 0
    else:
        return (a(n-1) * 2 - a(n-2)) + 2


def b(n):
    if n < 10:
        return 1
    else:
        return b(n-1) + b(n-2) + b(n-3)


def c(n):
    if n < 2:
        return n
    else:
        return max(c(n-1), c(n-3) * n)


# Als weitere Übungen können Sie das Knapsack-Problem (siehe Mensapreise-Aufgabe) oder die Tribonacci-Funktion mit
# dynamischer Programmierung lösen.
