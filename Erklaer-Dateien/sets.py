# In dieser Datei soll es um Mengen im mathematischen Sinne gehen. Diese gibt es auch in Python.
# Im Gegensatz zu Listen enthalten Sets keine doppelten Elemente und es gibt keine Reihenfolge. Letzteres hat den Effekt,
# dass man nicht ueber einen Index auf Elemente zugreifen kann.

# Sets werden mit set() initialisiert oder indem man innerhalb von geschweiften Klammern die Elemente hinschreibt. Aber
# Achtung! {} erzeugt ein Dictionary!

my_set = set()
print(type(my_set))
my_dict = {}
print(type(my_dict))

# ----

all_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
even_numbers = {2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}

# Was kann ich diesen Mengen jetzt antun? :)

all_numbers.remove(9)
print(all_numbers)
all_numbers.add(9)
print(all_numbers)

all_numbers2 = set()
all_numbers2.update(even_numbers)
all_numbers2.update(odd_numbers)

# Analog zu update gibt es auch difference_update

print(all_numbers == all_numbers2)

all_numbers2.clear()

# Neben diesen Standardoperationen, die analog zu Dictionaries bzw. Listen (von der Schreibweise her) funktionieren
# (intern nicht), gibt es auch noch Mengenoperationen

print(even_numbers.issubset(all_numbers))  # ist Teilmenge?
print(odd_numbers.isdisjoint(even_numbers))  # ist disjunkt?
print(all_numbers.issuperset(odd_numbers))  # ist Obermenge?

print(even_numbers.union(odd_numbers) == all_numbers)  # Vereinigung
print(even_numbers.intersection(odd_numbers))  # Schnittmenge
print(all_numbers.difference(odd_numbers) == even_numbers)  # Differenzmenge

# Wichtig: Sets beruhen, ebenso wie Dictionaries, auf Hash-Tabellen, d.h. Objekte in Sets sollten eine hash()-Methode
# implementiert haben, um ordentlich hinzugefuegt zu werden.

# Ich habe oben geschrieben, dass sets keine Reihenfolge haben. Beim Printen ist bestimmt aufgefallen, dass die Zahlen
# aber sortiert ausgegeben werden. Das ist ein interessantes Python-Special. Wenn ein Set aber z.B. Strings enthaelt,
# dann sieht man, dass die Reihenfolge jedes Mal zufaellig ist:

print({"a", "b", "c", "d", "e"})
