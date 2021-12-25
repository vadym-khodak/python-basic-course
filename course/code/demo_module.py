def greet():
    print("Hello World from demo module")


def greet_group():
    print("Hi the awesome group")


greet()


if __name__ == "__main__":
    greet_group()

    print(__name__)
