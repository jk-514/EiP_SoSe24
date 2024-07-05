import os

# Diese Datei soll den Umgang mit dem os-Modul erklären.
# Ich werde im Folgenden auf die Funktionen aus der Vorlesung eingehen und anhand von Beispielen erklären, wofür sie
# gut sind.

# Als erstes gibt es die Funktion getcwd (kurz für "get current working directory"). Sie gibt also das aktuelle Arbeits-
# verzeichnis zurück. Das ist der Ordner, mit dem das Programm aktuell arbeitet. Solange man das nicht mauell ändert,
# ist es der Ordner "how_to_os", in dem diese Datei liegt.

print(os.getcwd())
# /Users/jonahkraft/PycharmProjects/EIP_SoSe24/how_to_os

# Der Output wird auf jedem Gerät anders aussehen, da es sich um einen absoluten Pfad handelt

# Mit der Funktion chdir (kurz für "change directory") kann man das aktuelle Arbeitsverzeichnis ändern.
# In diesem Order existiert es Subordner names "sub_dir". Den will ich jetzt als Arbeitsverzeichnis auswählen.
# Hierfür reicht ein relativer Pfad aus

os.chdir("sub_dir")
print(os.getcwd())
# /Users/jonahkraft/PycharmProjects/EIP_SoSe24/how_to_os/sub_dir

# Eine weitere Funktion ist listdir ("list directory"). Sie gibt alle Dateien und Order zurück, die sich im übergebenen
# Ordner (als Pfad) befinden. Der Rückgabewert ist dabei eine Liste. Wenn man als Ordner das aktuelle Arbeitsverzeichnis
# verwenden will, kann man die Klammern leer lassen.

print(os.listdir())

# ['file2.txt', 'file3.txt', 'file1.txt']
# Offensichtlich sind die files nicht sortiert. Da die Liste Strings enthält, kann man das bei Bedarf mit der sort()-Methode
# machen.

# Dann gibt es die Funktion os.path.isfile()
# Diese gibt gibt einen booleschen Wert zurück, ob am übergebenen Pfad eine File zu finden ist oder nicht.
# Auch hier reicht ein relativer Pfad. Da das aktuelle Arbeitsverzeichnis nach wie vor "sub_dir" ist, reicht hier der
# Dateiname aus.

print(os.path.isfile("file1.txt"))      # True
print(os.path.isfile("dir"))            # False

# Analog funktioniert os.path.isdir()

# Dann gibt es noch os.path.exists(). Die Funktion gibt erwartungsgemäß zurück, ob ein Pfad existiert. Das ist nützlich,
# wenn Dateien vom Programm erstellt werden, um zu vermeiden, dass sie geöffnet werden, bevor sie existieren.

print(os.path.exists("file1.txt"))      # True
print(os.path.exists("file4.txt"))      # False

# Mit os.mkdir() kann man am übergebenen Pfad einen Order erzeugen.

os.mkdir("dir2")
# Dieser Code fügt dann im aktuellen Arbeitsverzeichnis (sub_dir) einen Ordner names dir2 hinzu. Alternativ kann man
# das auch mit os.mkdir("sub_dir/dir2") machen, wenn man das Arbeitsverzeichnis nicht auf "sub_dir" verändert hat.
# Die Funktion funktioniert nur, wenn der Ordner noch nicht existiert.

# Mit os.makedirs() kann man mehrere Ordner auf einmal erzeugen.

os.makedirs("dir3/sub")
# Erzeugt im aktuellen Arbeitsverzeichnis (da kein anderes angegeben) einen Ordner names dir3 und in dem einen Ordner
# names sub

# Analog kann man mit os.rmdir() einen Ordner löschen. Das ist sehr gefährlich, da es keinen "Papierkorb" oder so gibt,
# der Ordner ist sofort dauerhaft gelöscht.
# os.remove() macht dasselbe mit einzelnen Dateien. Meistens reicht es aber aus, diese zu überschreiben!

os.rmdir("dir2")

# Einen gewissen Sicherheitsmechanismus hat rmdir() aber schon. Man kann nur leere Ordner löschen! Wenn man einen
# nicht leeren Order löschen will, muss man also erst die Dateien darin löschen. dir3 kann man auf die Art also nicht löschen

# Abschließend gibt es noch os.replace(). Der übergibt man einen alten und neuen Namen für eine Datei oder einen Ordner.

os.replace("dir3", "test_name")
# dir3 heißt jetzt "test_name". Der Inhalt des Ordners bleibt unverändert.