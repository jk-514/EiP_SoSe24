from __future__ import annotations
from typing import Optional, Dict, List, Tuple
from datetime import date


# Aufgabe 1

def count_steps(n: int, memory: Optional[Dict[int, int]] = None) -> int:

    if memory is None:
        memory = {}

    if n in memory:
        return memory[n]

    elif n < 2:
        memory[n] = n
        return n

    else:
        memory[n] = min(count_steps(n-1, memory), count_steps(n-2, memory), count_steps(n//2, memory)) + 1
        return memory[n]


def count_steps_iterative(n: int, memory: Optional[Dict[int, int]] = None) -> int:
    if memory is None:
        memory = {}

    for i in range(n+1):
        if i < 2:
            memory[i] = i
        else:
            memory[i] = min(count_steps(i - 1, memory), count_steps(i - 2, memory), count_steps(i // 2, memory)) + 1

    return memory[n]


# Aufgabe 2

# i


def filter_even(l: List[int]) -> List[int]:
    return [digit for digit in l if (digit // 2) * 2 == digit]


# ii


def count_digits(n: int) -> int:
    counter = 0
    while n > 0:
        n //= 10
        counter += 1
    return counter


# iii


def count_digits_recursive(n: int) -> int:
    if n < 10:
        return 1
    return count_digits_recursive(n//10) + 1


# iv


def count_long_words(l: List[str]) -> int:
    return len([word for word in l if len(word) > 5])


# v


def count_fancy_long_words(l: List[str]) -> int:
    return len([word for word in l if len(word) > 5 and "e" in word.lower()])

# vi


def count_divisible_by_3_or_5(nums: List[int]):
    return len([num for num in nums if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0)])


# vii

def split_into_sublists(nums: List[int], n: int) -> List[List[int]]:
    sublists = []
    current_sublist = []
    current_sum = 0

    for num in nums:
        if current_sum + num <= n:
            current_sublist.append(num)
            current_sum += num
        else:
            sublists.append(current_sublist)
            current_sublist = [num]
            current_sum = num

    if current_sublist:
        sublists.append(current_sublist)

    return sublists


# Aufgabe 3

# i

def read_file(path: str) -> List[Dict[str, str]]:
    return [
        {key: value for key, value in zip(["date", "open", "high", "low", "close", "adj close", "volume"],
                                          line.strip().split(","))} for index, line in enumerate(open(path)) if index > 0
    ]


# ii

def analyze_open_stats(content: List[Dict[str, str]]) -> Tuple[float, float, float]:
    open_prices = [float(line["open"]) for line in content]
    min_price = round(min(open_prices), 2)
    max_price = round(max(open_prices), 2)
    avg_price = round(sum(open_prices) / len(open_prices), 2)

    return min_price, max_price, avg_price


# iii


def greatest_gap(content: List[Dict[str, str]]) -> str:
    prices: List[Tuple[float, float]] = list(zip([float(line["high"]) for line in content],
                                                 [float(line["low"]) for line in content],
                                                 [line["date"] for line in content]))
    return max(prices, key=lambda x: abs(x[0]-x[1]))[2]


# iv


def sum_profitable_days(content: List[Dict[str, str]]) -> int:
    return len([line for line in content if float(line["open"]) < float(line["close"])])


# v

def avg_growth(content: List[Dict[str, str]]) -> float:
    growth = [float(line["close"])/float(line["open"]) for line in content]
    return sum(growth) / len(growth)


# Aufgabe 5

# i


class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand: str = brand
        self.model: str = model
        self.year: int = year

    def get_brand(self) -> str:
        return self.brand

    def get_model(self) -> str:
        return self.model

    def get_year(self) -> int:
        return self.year

    def set_brand(self, brand: str) -> None:
        self.brand = brand

    def set_model(self, model: str) -> None:
        self.model = model

    def set_year(self, year: int) -> None:
        self.year = year

    # ii

    def calculate_age(self) -> int:
        return int(str(date.today()).split("-")[0]) - self.year

    # iii

    def __str__(self) -> str:
        return f"Car({self.brand}, {self.model}, {self.year})"

    def __repr__(self) -> str:
        return str(self)

    # iv

    def __lt__(self, other: Car) -> bool:
        return self.year < other.get_year()

# v


class Garage:
    def __init__(self) -> None:
        self.cars: List[Car] = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
        self.cars.remove(car)

    def oldest_car(self) -> Car:
        return min(self.cars)

    def __str__(self) -> str:
        return "Garage" + str(self.cars)
