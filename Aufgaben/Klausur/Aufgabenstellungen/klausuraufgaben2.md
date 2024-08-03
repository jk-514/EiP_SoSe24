## Aufgabe 1

Eine einfache Funktion zum Warmwerden:
Schreiben Sie eine Funktion, die eine Liste, die Strings enthaelt, uebergeben bekommt und alle Strings auf der Konsole
ausgibt, die mit dem Buchstaben "a" beginnen.

## Aufgabe 2

In dieser Aufgabe wollen wir die Potenz einer gegebenen Zahl berechnen. Offensichtlich sind der **-Operator und
Funktionen, die genau das berechnen, nicht erlaubt. Sie koennen davon ausgehen, dass beide Zahlen, die ihre Funktion bekommt,
positive natuerliche Zahlen sind.

(i) Schreiben Sie eine iterative Funktion, die die Potenz einer gegebenen natuerlichen Zahl n berechnet.

(ii) Schreiben Sie die Funktion aus (i) rekursiv.

Hinweis: Wenn in der Aufgabenstellung steht, dass eine Funktion rekursiv sein soll, bedeutet das, dass es nicht der Sinn
der Aufgabe ist, eine rekursive Hilfsfunktion zu schreiben und die dann aufzurufen.

## Aufgabe 3

In dieser Aufgabe wollen wir Listen umdrehen. Das heisst, die Funktion bekommt eine Liste wie [1, 2, 3] und gibt
manipuliert sie so, dass die Elemente rueckwaerts darin stehen, \
also hier [3, 2, 1]. Offensichtlich sind liste[::-1] und liste.reverse() verboten.

(i) Schreiben Sie die Funktion iterativ.

(ii) Schreiben Sie die Funktion rekursiv.

## Aufgabe 4

In der Datei index.html finden Sie die Struktur einer (sehr simplen) Webseite. Schreiben Sie eine Funktion, die den Dateinamen
uebergeben bekommt und eine Liste zurueckgibt, \
die alle Ueberschriften enthaelt. In html kann man diese folgendermassen erkennen.
Es gibt einen Opening-Tag, dann steht da die Ueberschrift und dann der Closing-Tag.\
Der Opening-Tag steht in <>. Darin steht (in unserem Fall, im Allgemeinen komplexer) erst der Buchstabe h und dann eine Zahl. \
Der Closing-Tag sieht in dem Fall prinzipiell genauso aus, aber hinter dem < ist ein /.
Aus `<h1>Hauptüberschrift</h1>` soll also nur "Hauptüberschrift" extrahiert werden.


## Aufgabe 5

In dieser Aufgabe widmen wir uns dem [Zipfschen Gesetz](https://de.wikipedia.org/wiki/Zipfsches_Gesetz).
Sie haben bereits die Datei faust.txt. Mit dieser wollen wir jetzt weiter arbeiten.

(i) Schreiben Sie eine Funktion, die den Dateinamen als uebergeben bekommt. 
Legen Sie ein Dictionary an, das fuer alle Woerter deren Haufigkeit speichern sollen (Dict[str, int]) \
Die Funktion soll die Datei zeilenweise
einlesen. Ignorieren Sie den Vorspann (Zeilen 1-23). Zunaeachst sollen sie alle Sonderzeichen aus der Zeile entfernen. \
Hinweis: Sie koennen das string-Modul importieren. string.punctuation ist ein String (wow) und enthaelt alle ASCII-Sonderzeichen. \
Ignorieren Sie ferner Gross- und Kleinschreibung.
Die Funktion soll das Dictionary zurueckgeben. \
Bestimmen Sie anschliessend die haeufigsten 100 Woerter und beurteilen Sie, ob das Zipfsche Gesetz zutrifft.
