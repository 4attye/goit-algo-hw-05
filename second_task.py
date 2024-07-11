from typing import Callable
import  re

"""
    Функція генератор, що отримує числа з тексту з використанням регулярного виразу
    й повертає їх по одному перетворюючи у тип float
"""
def generator_numbers(text_to_process: str) -> float:
    for revenue in re.findall(r"\d+.\d+", text_to_process):
        yield float(revenue)

"""
    Функція що підраховує суму чисел знайдених в тексті
    з використанням функції-генератора для їх отримання
"""
def sum_profit(text_to_process: str, func: Callable) -> float:
    return sum(func(text_to_process))


text = ("Загальний дохід працівника складається з декількох частин:"
        " 1000.01 як основний дохід, доповнений додатковими надходженнями:"
        " 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")