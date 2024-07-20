catalog = {'123': {'title': 'Test1', 'author': 'Test-Autor', 'year': 2000, 'copies': 10},
           '345': {'title': 'Test2', 'author': 'Test-Autor2', 'year': 2001, 'copies': 5},
           '323': {'title': 'Test3', 'author': 'Test-Autor3', 'year': 1999, 'copies': 1}}


def add_book(catalog, isbn, title, author, year, copies):
    if isbn in catalog:
        catalog[isbn][copies] += copies
    else:
        catalog[isbn] = {"title": title, "author": author, "year": year, "copies": copies}


def remove_book(catalog, isbn):
    del catalog[isbn]


def search_by_title(catalog, title):
    return [(isbn, info["title"]) for isbn, info in catalog.items() if title in info["title"]]


def check_copies(catalog, isbn):
    return catalog[isbn]["copies"]


def borrow_book(catalog, isbn):
    if catalog[isbn].get("copies", 0) == 0:
        raise ValueError("The book cannot be borrowed")
    else:
        catalog[isbn]["copies"] -= 1


def return_book(catalog, isbn):
    catalog[isbn]["copies"] += 1


def print_catalog(catalog):
    for key, value in catalog.items():
        print(key, value)
