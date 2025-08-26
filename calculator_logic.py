def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a + b


def subtruct(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a - b


def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a * b


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return a / b