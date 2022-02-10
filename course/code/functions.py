# Проста функція
def greet_world():
    print("Hello World!")


print("Run greet_world first time")
greet_world()
print("Run greet_world second time")
greet_world()
print("Run greet_world third time")
greet_world()


# Функція що приймає аргумент
def greet_person(name, part_of_day):
    phrase_by_part_of_day = {
        "morning": "Good morning",
        "day": "Good afternoon",
        "evening": "Good evening",
    }
    greeting_phrase = phrase_by_part_of_day.get(part_of_day, "Hello")
    print(f"{greeting_phrase} {name}!")


greet_person("Max", "morning")


# Функція що повертає None
def greet_person(name, part_of_day):
    phrase_by_part_of_day = {
        "morning": "Good morning",
        "day": "Good afternoon",
        "evening": "Good evening",
    }
    greeting_phrase = phrase_by_part_of_day.get(part_of_day, "Hello")
    full_phrase = f"{greeting_phrase} {name}!"
    if "Bob" == name:
        print("Hi")
        return None
    print(full_phrase)


none = greet_person("Max", "morning")
print(none)


# Функція що повертає значення
def greet_person(name, part_of_day):
    phrase_by_part_of_day = {
        "morning": "Good morning",
        "day": "Good afternoon",
        "evening": "Good evening",
    }
    greeting_phrase = phrase_by_part_of_day.get(part_of_day, "Hello")
    full_phrase = f"{greeting_phrase} {name}!"
    if "Bob" == name:
        return "Hi"
    return full_phrase


phrase = greet_person("Max", "morning")
print(phrase)


# Порядкові аргументи функції
def greet_person(name, part_of_day):
    phrase_by_part_of_day = {
        "morning": "Good morning",
        "day": "Good afternoon",
        "evening": "Good evening",
    }
    greeting_phrase = phrase_by_part_of_day.get(part_of_day, "Hello")
    name = name.title().strip()
    full_phrase = f"{greeting_phrase} {name}!"
    if "Bob" == name:
        return "Hi"
    return full_phrase


phrase = greet_person("    maX smIth          ", "morning").lower().replace("!", ".")
print(phrase)


# Іменовані аргументи функції
print("Hello", end=" ")  # 'end' - є іменованим аргументом функції 'print'
print("World")


def greet_person(name, part_of_day="day"):
    phrase_by_part_of_day = {
        "morning": "Good morning",
        "day": "Good afternoon",
        "evening": "Good evening",
    }
    greeting_phrase = phrase_by_part_of_day.get(part_of_day, "Hello")
    full_phrase = f"{greeting_phrase} {name}!"
    return full_phrase


phrase = greet_person("Max", part_of_day="morning")
print(phrase)

phrase = greet_person("Rob")
print(phrase)


# Виклик функцій в середені інших функцій
def a():
    print("a() starts")
    b()
    d()
    print("a() returns")


def b():
    print("b() starts")
    c()
    print("b() returns")


def c():
    print("c() starts")
    print("c() returns")


def d():
    print("d() starts")
    print("d() returns")


a()


# # Використання локальних глобальних змінних
# Локальні змінні
def multiply(number):
    multiplier = 3
    return number * multiplier


print(multiply(4))
# print(multiplier)  # Цей код видасть помилку


# Глобальні змінні
multiplier = 3


def multiply(number):
    print(multiplier)

    return number * multiplier


print(multiply(4))


# Зміна значення глобальної змінної в середені функції
connection = None


def get_connection():
    print("Start using global variable in get_connection function")
    global connection
    if not connection:
        print("Start getting connection")
        connection = "I'm a connection"
        return connection
    print("Connection already exists")
    return connection


conn = get_connection()
print(id(connection))
print(id(conn))
conn = get_connection()
print(id(connection))
print(id(conn))


# Локальні та глобальні змінні з однаковим ім'ям
def spam():
    eggs = "spam local"
    print(eggs)  # prints 'spam local'


def bacon():
    eggs = "bacon local"
    print(eggs)  # prints 'bacon local'
    spam()
    print(eggs)  # prints 'bacon local'


eggs = "global"
bacon()
print(eggs)  # prints 'global'


# args and kwargs
# Використання не визначеної кількості позиційних аргументів
def avg(*args):
    print(type(args), args)
    total = 0
    for i in args:
        total += i
    return total / len(args)


print(avg(0.41, 2.5, 3))
print(avg(0.1, 2, 3, 4, 5))
# print(avg())  # Цей код видасть помилку через ділення на 0


# Використання не визначеної кількості іменованих аргументів
PI = 3.14


def test_kwargs(index, *args, name=None, **kwargs):
    print(type(index), index)
    print(type(args), args)
    print(type(name), name)
    print(type(kwargs), kwargs)
    print(PI)


test_kwargs(1, "smith", 4, {"name": "bob"}, first_name="Max", age=39)


def change_pi(radius):
    return 2 * PI * radius


change_pi(2)
