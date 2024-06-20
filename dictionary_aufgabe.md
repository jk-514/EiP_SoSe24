## Aufgabe: Verwaltung eines Bücherkatalogs

Du sollst ein Programm schreiben, das einen Bücherkatalog verwaltet.
Der Katalog soll als Dictionary implementiert werden, in dem jeder Schlüssel die ISBN-Nummer eines Buches ist und
der Wert ein weiteres Dictionary mit Informationen über das Buch.


### Anforderungen:

- #### Bücher hinzufügen:

    Implementiere eine Funktion add_book(catalog, isbn, title, author, year, copies), die ein Buch mit den gegebenen Informationen zum Katalog hinzufügt.
Wenn das Buch bereits existiert (gleiche ISBN), erhöhe nur die Anzahl der Kopien.


    `catalog = {"123-456-789": {"title": "Never gonna give you up", "author": "Rick Astley", "year": 1987, "copies": 12345}}`


- #### Bücher entfernen:

    Implementiere eine Funktion remove_book(catalog, isbn), die ein Buch anhand der ISBN-Nummer aus dem Katalog entfernt.
Es soll nicht die Anzahl der Kopien gesenkt werden, sondern das Buch soll ganz geloescht werden.


- #### Bücher suchen:

    Implementiere eine Funktion search_by_title(catalog, title), die eine Liste von Büchern zurückgibt, die den gegebenen Titel enthalten (Teilübereinstimmung).
Es soll eine Liste mit Tupeln aus ISBN und Titel zurückgegeben werden.


- #### Bestand überprüfen:

    Implementiere eine Funktion check_copies(catalog, isbn), die die Anzahl der verfügbaren Kopien eines Buches anhand der ISBN-Nummer zurückgibt.


- #### Bücher ausleihen:

    Implementiere eine Funktion borrow_book(catalog, isbn), die die Anzahl der verfügbaren Kopien eines Buches um 1 verringert. Wenn keine Kopien verfügbar sind, gib eine entsprechende Meldung aus.


- #### Bücher zurückgeben:

    Implementiere eine Funktion return_book(catalog, isbn), die die Anzahl der verfügbaren Kopien eines Buches um 1 erhöht.
