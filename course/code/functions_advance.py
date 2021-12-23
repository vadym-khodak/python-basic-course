# Обробка помилок та виключень
# Синтаксичні помилки
def hello()  # Синтаксична помилка - відсутнє ":"
    print("Hello")

hello()

x, y = 1, 3
if x = y:  # Синтаксична помилка - має бути "==" замість "="
    print("Both numbers are equal")


# Функція підрахунку середнього з послідовності чисел
def avg(*args):
    return sum(args) / len(args)


numbers = [1, 2, 3, 4, 5]
# Розпакування послідовності '*numbers` - це еквівалент наступному запису `print(avg(1, 2, 3, 4, 5))`
print(avg(*numbers))
print(avg())


# Обробка виключення "Ділення на 0"
def avg(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        print("You need to pass at least one number as function argument")


print(avg(1, 2, 3, 4, 5))

print(avg())


# Обробка декількох виключень
def avg(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        print("You need to pass at least one number as function argument")
    except TypeError:
        print("You need to use only numbers as function arguments")


print(avg(1, 2, 3, 4, 5))

print(avg())

print(avg("1", 2, 3, 4, 5))


# Обробка усіх виключень
def avg(*args):
    try:
        return sum(args) / len(args)
    except:
        print("Something went wrong")


print(avg(1, 2, 3, 4, 5))

print(avg())

print(avg("1", 2, 3, 4, 5))


# Обробка усіх виключень з отриманням виключення що виникло
def avg(*args):
    try:
        return sum(args) / len(args)
    except Exception as err:
        print("Something went wrong")
        print(err)


print(avg(1, 2, 3, 4, 5))

print(avg())

print(avg("1", 2, 3, 4, 5))


# Використання блоку `finally` під час обробки виключень
def avg(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        print("You need to pass at least one number as function argument")
    except TypeError:
        print("You need to use only numbers as function arguments")
    finally:
        print("Your function was ended anyway")


print(avg(1, 2, 3, 4, 5))

print(avg())

print(avg("1", 2, 3, 4, 5))


# Використання блоку `else` під час обробки виключень
def avg(*args):
    average = None
    try:
        average = sum(args) / len(args)
    except ZeroDivisionError:
        print("You need to pass at least one number as function argument")
    except TypeError:
        print("You need to use only numbers as function arguments")
    else:
        print("This code will be run only if there is no exceptions")
    finally:
        print("Your function was ended anyway")
    return average


print(avg(1, 2, 3, 4, 5))

print(avg())

print(avg("1", 2, 3, 4, 5))


# Використання `raise` під час обробки виключень
def avg(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        raise ValueError("You need to pass at least one number as function argument")
    except TypeError:
        raise TypeError("You need to use only numbers as function arguments")


print(avg(1, 2, 3, 4, 5))

print(avg())

print(avg("1", 2, 3, 4, 5))


# Використання custom exceptions під час обробки виключень
class NoArguments(Exception):
    """You need to pass at least one number as function argument"""


class WrongArguments(Exception):
    """You need to use only numbers as function arguments"""


def avg(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        raise NoArguments("You need to pass at least one number as function argument")
    except TypeError:
        raise WrongArguments("You need to use only numbers as function arguments")


print(avg(1, 2, 3, 4, 5))

print(avg())

print(avg("1", 2, 3, 4, 5))


# Функція 3 * x * x + 5
def f(x):
    return 3 * x ** 2 + 5


print(f(2))


def f(x): return 3 * x ** 2 + 5


print(f(2))


# Анонімна lambda функція рівняння 3 * x * x + 5 = 0
f = lambda x: 3 * x ** 2 + 5


print(f(2))

print((lambda x: 3 * x ** 2 + 5)(2))


# Функція квадратного рівняння
def square_equation(a, b, c):
    def f(x):
        return a * x ** 2 + b * x + c
    return f


f = square_equation(2, 3, 5)
print(f(4))
print(f(0))
print(f(1))
print(f(-1))


# Функція квадратного рівняння з використанням lambda
def square_equation(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = square_equation(2, 3, 5)
print(f(4))
print(f(0))
print(f(1))
print(f(-1))


# Використання lambda функції як аргумент для іншої функції
names = [
    "Isaac Newton",
    "Leonhard Euler",
    "Charles-Augustin de Coulomb",
    "Amedeo Avogadro",
    "Michael Faraday",
    "Johann Josef Loschmidt",
    "Johann Jakob Balmer",
    "Joseph Stefan",
    "Ludwig Boltzmann",
    "Johannes Robert Rydberg",
    "Joseph John Thomson",
    "Max Planck",
    "Wilhelm Wien",
    "Owen Willans Richardson",
    "Otto Sackur",
    "Niels Bohr",
    "Edwin Hubble",
    "Hugo Tetrode",
    "Douglas Hartree",
    "Enrico Fermi",
    "Roger Apéry",
    "Brian Josephson",
    "Klaus von Klitzing",
    "Albert Einstein",
    "Marie Curie",
    "Charles Darwin",
    "Nikola Tesla",
    "Galileo Galilei",
    "Ada Lovelace",
]

names.sort()
print(names)


names.sort(key=lambda name: name.split(" ")[-1])
print(names)


# Рекурсивні функції
# Функція розрахунку факторіалу числа
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))


# Функція розрахунку факторіалу числа з використанням рекурсії
def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# Функція отримання послідовності Фібоначчі
def fibonacci(n):
    nums = []
    if n == 1:
        nums.append(1)
    elif n >= 2:
        nums.extend([1, 1])
    if n > 2:
        for i in range(2, n):
            nums.append(nums[-1] + nums[-2])
    return nums


print(fibonacci(15))


# Рекурсивна функція отримання n-го числа послідовності Фібоначчі
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# Рекурсивна функція отримання n-го числа послідовності Фібоначчі з використанням кешу
cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1:
        cache[n] = 1
        return cache[n]
    elif n == 2:
        cache[n] = 1
        return cache[n]
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]


print(fibonacci(856))


# Рекурсивна функція для видалення непотрібних ключів зі словника
from copy import deepcopy
from pprint import pprint


def clean_dict_by_template(data, template):
    clean_dict = deepcopy(template)
    for k, v in template.items():
        if isinstance(v, dict):
            clean_dict.update({k: clean_dict_by_template(data.get(k, {}), v)})
        else:
            clean_dict.update({k: data.get(k) if data else None})
    return clean_dict


user = {
    "id": 1,
    "name": "Vadym Khodak",
    "first_name": "Vadym",
    "last_name": "Khodak",
    "accounts": {
        "github": {
            "username": "vadym-khodak",
            "repos": [
                "python-basic-course",
                "python-basic-course-hw",
            ],
        },
        "discord": {
            "username": "Vadym Khodak",
            "id": "ifheine382r418e1",
        },
        "gmail": {
            "email": "vadymkhodak.pythonanywhere@gmail.com",
        },
        "zoom": {
            "username": "Vadym Khodak",
            "link": "https://zoom.us/profile",
            "id": 23567297265427,
        },
    },
    "status": "active",
    "role": "admin",
    "address": {
        "country": "Ukraine",
        "city": "Khmelnytskyi"
    }
}

user_template = {
    "id": None,
    "name": None,
    "accounts": {
        "github": {"username": None},
        "discord": {"username": None},
        "gmail": {"email": None},
        "zoom": {"username": None},
    },
}


cleaned_user = clean_dict_by_template(user, user_template)

pprint(user)
pprint(cleaned_user)

assert cleaned_user.keys() == user_template.keys()
