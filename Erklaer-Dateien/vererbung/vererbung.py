from __future__ import annotations  # für Typehints, könnt ihr ignorieren :)
import os
import shutil  # Erweitert die Moeglichkeiten von os
from sys import platform  # Damit kann man abfragen, ob gerade Windows oder MacOS genutzt wird.
from abc import ABC, abstractmethod

# In diesem Blatt werden wir das Thema Vererbung in Python thematisieren.

# Wann sollte eine Klasse von einer anderen Klasse erben? Sinnvollerweise sollte eine Klasse genau dann von einer
# anderen Klasse erben, wenn sie ein Spezialfall von dieser ist.
# Beispielsweise ist ein Kreis ein Spezialfall einer Ellipse, aber ein Rechteck wohl eher kein Spezialfall eines
# Quadrats.
# Aber Vorsicht! Ein Vektor könnte als Spezialfall einer Liste aufgefasst werden, ist es aber keineswegs! Eine Liste hat
# diverse Eigenschaften, die bei einem Vektor eher weniger sinnvoll wären.

# Vor einigen Wochen hatten wir uns das Modul os angeschaut, mit dem man Dateien verwalten kann. Uebrigens kann os nicht
# alles, es gibt in der Standardbibliothek von Python noch ein anderes Modul names shutil, mit dem man z.B. Dateien
# verschieben kann.
# Ihr muesst jetzt nicht os-Commands lernen, die sollten von ihren Namen her deutlich machen, was passiert.
# Im Zweifelsfall einfach mal einen Command googlen. Wenn man in PyCharm drueberhovert, ist die Doku direkt verlinkt

# However, auch wenn es auf den ersten Blick vielleicht merkwuerdig klingt, sind Dateien und Ordner fast dasselbe.
# Wir koennen beide verschieben, erstellen, loeschen, duplizieren etc.
# In diesem Code soll es darum gehen, auf eine (hoffentlich simple) Weise mit Dateien zu arbeiten, um das Thema Vererbung
# zu lernen. Schreiben wir zuerst eine abstrakte Oberklasse names "FileSystemEntity", von der Ordner und Dateien erben
# sollen.
# Wie gesagt, ist "FileSystemEntity" eine abstrakte Klasse, dh es wird niemals ein Objekt dieser Klasse erzeugt, sondern
# nur von Klassen, die davon erben. Indem wir FileSystemEntity von ABC erben lassen, stellen wir genau das sicher.


class FileSystemEntity(ABC):
    def __init__(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(path)

        self.path: str = path
        self.title: str = self.get_title()

    def get_title(self) -> str:
        if platform == "darwin":
            # Falls die Plattform MacOs ist
            return self.path.split("/")[-1]
        else:
            # Falls es Windows ist, kein Support fuer Linux
            return self.path.split("\\")[-1]

    def __lt__(self, other: FileSystemEntity) -> bool:
        # Sortiert alphabetisch, bei Bedarf kann man hier mehrere Optionen implementieren, z.B. nach dem letzten
        # Aenderungsdatum oder dem Erstellungsdatum
        return self.path.lower() < other.path.lower()

    # Dann haben wir hier noch ein paar abstrakte Methoden. Diese sollen in den Unterklassen ueberladen werden. Es ist
    # trotzdem sinnvoll, sie hier als Platzhalter bereits hinzuschreiben. Mit dem Dekorator abstractmethod aus dem abc-
    # Modul kann man erzwingen, dass sie tatsaechlich ueberladen werden.

    @abstractmethod
    def duplicate(self) -> None:
        pass

    @abstractmethod
    def rename(self, new_name: str) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


# Schreiben wir also eine Klasse fuer Dateien


class File(FileSystemEntity):
    def __init__(self, path: str):
        super().__init__(path)
        self.title_without_suffix: str = "".join(self.title.split(".")[:-1])
        self.suffix: str = self.path.split('.')[-1]

    # Jetzt muessen wir also die drei abstrakten Methoden hier implementieren.

    def __str__(self) -> str:
        return f"File({self.path})"

    def duplicate(self) -> None:
        # Bestimme den neuen Namen z.B. "test.txt" → "test.txt"
        i = 1
        while True:
            path = os.path.join(os.path.dirname(self.path), f"{self.title_without_suffix} {i}.{self.suffix}")
            if not os.path.exists(path):
                shutil.copy2(self.path, path)
                # damit wird die Datei dann tatsaechlich dupliziert
                return
            else:
                i += 1

    def rename(self, new_name) -> None:

        # um zu verhindern, dass der Suffix der Datei verloren geht, fuege ihn im Zweifelsfall wieder hinzu
        if "." not in new_name:
            new_name = f"{new_name}.{self.suffix}"

        new_path = os.path.join(os.path.dirname(self.path), new_name)
        os.rename(self.path, new_path)
        self.path = new_path
        self.title = new_name
        self.title_without_suffix = "".join(self.title.split(".")[:-1])


# Analog geht man bei den Ordnern / Directories vor


class Directory(FileSystemEntity):
    def __init__(self, path: str):
        super().__init__(path)

    def __str__(self) -> str:
        return f"Directory({self.path})"

    def duplicate(self) -> None:
        i = 1
        while True:
            # Unterscheidet sich nur im Pfad vom File-Objekt
            path = os.path.join(os.path.dirname(self.path), f"{self.title} {i}")
            if not os.path.exists(path):
                shutil.copytree(self.path, path)
                return
            else:
                i += 1

    def rename(self, new_name) -> None:

        # Im Gegensatz zu den Dateien muss hier kein Suffix geprueft werden. Der Rest ist analog.

        new_path = os.path.join(os.path.dirname(self.path), new_name)
        os.rename(self.path, new_path)
        self.path = new_path
        self.title = new_name


# Freiwillige Aufgabe: Die Methoden duplicate und rename unterscheiden sich bei Dateien und Ordnern nur minimal.
# Wie koennte man diese Methoden in die Oberklasse auslagern, ohne den Effekt auf Dateien bzw. Ordner zu veraendern?


if __name__ == '__main__':

    if platform == "darwin":
        # Unter MacOS
        file = File("dir/test.txt")
    else:
        # Unter Windows
        file = File("dir\\test.txt")

    file.duplicate()
    print(file)
    file.rename("test123")

    directory = Directory("dir")
    directory.duplicate()
    print(directory)
    directory.rename("my_dir")
