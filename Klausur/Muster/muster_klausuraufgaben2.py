from typing import List, Dict
import string

# Aufgabe 1


def print_a_words(array: List[str]) -> None:
    for i in array:
        if i.startswith("a"):
            print(i)


# Aufgabe 2

# die Funktionen berechnen a^b


def pow_iterative(a: int, b: int) -> int:
    p: int = a
    for _ in range(b-1):
        p *= a
    return p


def pow_recursively(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * pow_recursively(a, b-1)


# Aufgabe 3

def reverse_array(array: List[int]) -> List[int]:
    for i in range(len(array)//2):
        array[i], array[-(i+1)] = array[-(i+1)], array[i]
    return array


def reverse_array_recursively(array: List[int], start: int = 0, end: int = -1) -> List[int]:
    if end == -1:
        end = len(array)-1
    if start >= end:
        return array
    array[start], array[end] = array[end], array[start]
    return reverse_array_recursively(array, start+1, end-1)


# Aufgabe 4

def extract_headers(file_name: str) -> List[str]:
    output: List[str] = []
    with open(file_name, "r") as file:
        for line in file:
            edited_line = line.strip()
            if edited_line.startswith("<h"):
                splitted_line = edited_line.split("<")
                header = splitted_line[1].split(">")[1]
                if header:
                    output.append(header)
    return output


# Aufgabe 5

def count_words_from_file(file_name: str) -> Dict[str, int]:
    with open(file_name, "r") as file:

        amount_words: Dict[str, int] = {}

        for index, line in enumerate(file):
            if index < 24:
                continue

            edited_line = line.strip().lower()
            for char in string.punctuation:
                edited_line = edited_line.replace(char, "")
            for word in edited_line.split():
                if word:
                    amount_words[word] = amount_words.get(word, 0) + 1
    return amount_words


def get_most_common_words(amount_words: Dict[str, int]) -> List[str]:
    return sorted(amount_words, key=amount_words.get, reverse=True)[:100]
