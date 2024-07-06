class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Dog({self.name})"


class Cat:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Cat({self.name})"

    def __repr__(self) -> str:
        return str(self)


print([Dog("Bello"), Dog("Max"), Dog("Balu"), Dog("Daisy")])
print([Cat("Lotte"), Cat("Frida"), Cat("Nala"), Cat("Leo")])

# Wenn man die __repr__-Methode implementiert, werden die Objekte aus eigenen Klassen in Listen und aehnlichen Datentypen ordentlich angezeigt.
