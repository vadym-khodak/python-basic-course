# Зведення у другу ступінь кожного числа з послідовності за допомого функції map()
import random

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = list(map(lambda x: x ** 2, numbers))
print(result)


# Зведення у другу ступінь кожного числа з послідовності за допомого циклу for
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = []
for num in numbers:
    result.append(num ** 2)
print(result)


# Зведення у другу ступінь кожного числа з послідовності за допомого list comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num ** 2 for num in numbers]
print(result)


# Фільтрування послідовності чисел для отримання тільки парних чисел за допомогою функції filter()
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)

# Фільтрування послідовності чисел для отримання тільки парних чисел за допомогою циклу for
filtered_numbers = []
for num in numbers:
    if num % 2 == 0:
        filtered_numbers.append(num)
print(filtered_numbers)

# Фільтрування послідовності чисел для отримання тільки парних чисел за допомогою list comprehension з умовою if
filtered_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print(filtered_numbers)


# Отримання суми квадратів парних чисел пурших десяти чисел з послідовності Фібоначчі за допомогою функції reduce()
from functools import reduce
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

# Отримання суми квадратів парних чисел пурших десяти чисел з послідовності Фібоначчі за допомогою циклу for
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num ** 2)
result = sum(result)
print(result)

# Отримання суми квадратів парних чисел пурших десяти чисел з послідовності Фібоначчі за допомогою list comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = sum(num ** 2 for num in numbers if num % 2 == 0)
print(result)


# Приведення списку ряків з ім'ями до нормального виду за допомогою циклу for
names = ["   John     dOe  ", "  maRk           SMITH   ", "john doe"]
new_names = []
for name in names:
    new_names.append(" ".join(name.title().split()))
print(new_names)


# Приведення списку ряків з ім'ями до нормального виду за допомогою list comprehension
names = ["   John     dOe  ", "  maRk           SMITH   ", "john doe"]
new_names = [" ".join(name.title().split()) for name in names]
print(new_names)


# Приведення списку ряків з ім'ями до нормального виду та видалення дублікатів за допомогою set comprehension
names = ["   John     dOe  ", "  maRk           SMITH   ", " john   doe  "]
new_names = {" ".join(name.title().split()) for name in names}
print(new_names)


# Створення dict of dicts з list of dicts для більш ефективного пошуку
from pprint import pprint
from time import time

from faker import Faker

fake = Faker()


def get_people(number):
    """Функція генерації випадкових даних"""
    _people = []
    for i in range(1, number + 1):
        _people.append({"id": i, "name": fake.name(), "email": fake.email(), "is_active": random.choice([True, False])})
    return _people


people = get_people(100000)
pprint(people)

# Створення dict of dicts з list of dicts для більш ефективного пошуку за допомогою циклу for
person_by_id = {}
for person in people:
    person_by_id[person["id"]] = person

# Створення dict of dicts з list of dicts для більш ефективного пошуку за допомогою list comprehension
person_by_id_new = {person["id"]: person for person in people}

pprint(person_by_id)

# Використання бібліотеки time для визначення часу витраченого на пошук необхідної персони у списку словників
start = time()
for person in people:
    if person["id"] == 99567:
        print(person)
        print(time() - start)

# Використання бібліотеки time для визначення часу витраченого на пошук необхідної персони у словнику словників
start = time()
print(person_by_id.get(99567))
print(time() - start)



# Домашнє завдання
# Написати функцію, що приймає один порядковий аргумент `emails` який є списком рядків,
# та два іменованих аргументи `domain` типу str, який за замовчуванням має значення `gmail.com`,
# та `deduplicate` типу bool, який за замовчуванням має значення False.
# Функція повертає список нормалізованих (видалені зайві пробіли, та приведено до нижнього регістру) імейлів
# відфільтрованих за доменом та у випадку коли `deduplicate` дорівнює True видаляє однакові імейлию
