"""
    Функція з вкладеною функцією для обчислення чисел Фібоначчі з використанням кешу
    з перевіркой чи є значення в кеші, якщо є то бере значення з кешу,
    якщо нема обчислює його рекурсивно та зберігає в кеш.
"""
def caching_fibonacci():
    cache = {0:0, 1:1}
    def fibonacci(n):
        if n in cache: return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci


fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610