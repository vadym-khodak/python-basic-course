# Декоратори
def greeting():
    print("hello world")


greeting()

# Створення простого декоратора
def my_decorator(fn):
    def wrapper():
        print("Do something before the main function")
        fn()
        print("Do something after the main function")
    return wrapper

# Декорування функці декоратором за допомогу передавання функції як аргумент функції-декоратора
decorated_fn = my_decorator(greeting)
decorated_fn()


# Декорування функці декоратором за допомогою символу `@`
@my_decorator
def greeting():
    print("hello world")


greeting()


# Практичне застосування декоратора для збереження логів використання функції
import datetime

from functools import wraps

session = {"user_name": "John Doe", "user_role": "user"}

# Декоратор для збереження аналітики виклику функції
def store_analytic_data(fn):
    @wraps(fn)
    def wrapper():
        fn()
        with open("logs.txt", "a") as f:
            f.write(
                "{} \t User {} called function \t{} \n".format(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    session['user_name'],
                    fn.__name__
                )
            )
    return wrapper


@store_analytic_data
def another_greeting():
    print("hello group")

# Використання одного декоратора для декорування функції
@store_analytic_data
def greeting():
    print("hello world")


another_greeting()
greeting()


# Практичне застосування декоратора для перевірки доступу для виклику функції
def check_admin(fn):
    @wraps(fn)
    def wrapper():
        if session["user_role"] != "admin":
            print(f"User with role {session['user_role']} is not allowed to call {fn.__name__} function")
            raise Exception
        print(f"User with role {session['user_role']} is allowed to call {fn.__name__} function")
        fn()
        print(f"User called this function")

    return wrapper


# Можливість застосовувати декілька декораторів для декорування однієї функції
@store_analytic_data
@check_admin
def greeting():
    print("hello world")


greeting()


# Практичне застосування декоратору для перевірки доступу за ролями
#  Передавання аргументів у декоратор
def check_role(role="admin", is_raise_exception=False):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if session["user_role"] != role:
                print(f"User with role {session['user_role']} is not allowed to call {fn.__name__} function")
                if is_raise_exception:
                    raise Exception
                return
            print(f"User with role {session['user_role']} is allowed to call {fn.__name__} function")
            fn()
            print(f"User called this function")

        return wrapper
    return inner


# Передавання аргументу у декоратор
@check_role(role="user")
def greeting():
    print("hello world")


greeting()


# Домашнє завдання
# Написати декоратор який буде обробляти усі виключення, які відбудуться у функції до якої доданий цей декоратор.
# У разі виникнення виключення декоратор має записувати час коли трапилась помилка та опис помилки у файл `logs.txt`


def error_handling(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
    return wrapper


@error_handling
def divide_nums(a, b):
    return a / b


divide_nums(1, 0)
