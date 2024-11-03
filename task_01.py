def caching_fibonacci():
    # Створюємо порожній словник для зберігання обчислених значень
    cache = {}

    # Внутрішня рекурсивна функція для обчислення числа Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Перевірка, чи є результат у кеші
        if n in cache:
            return cache[n]
        
        # Обчислення числа Фібоначчі та збереження його в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повернення внутрішньої функції fibonacci
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(17))  # Виведе 610
