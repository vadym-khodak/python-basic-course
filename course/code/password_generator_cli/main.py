# Імпортування необхідних модулів
import math
import random


def generate_chars(length):
    # Отримання усіх символів латинського алфавіту у верхньому та нижньому регістрах
    chars = [chr(ch) for ch in list(range(65, 65 + 26)) + list(range(65 + 32, 65 + 32 + 26))]
    # Створення змінної для літер, які будуть використані для створення паролю
    chars_for_password = []
    for _ in range(length):
        # Додавання до змінної password випадкових літер стількі разів скільки є значення аргументу length
        chars_for_password.append(random.choice(chars))
    return chars_for_password


def generate_password(
        length: int = 8,
        use_numbers: bool = False,
        use_special_chars: bool = False,
        special_characters: str = "-@_.*!",
) -> str:
    """
    Функція яка приймає аргументи CLI додатку та генерує пароль
    на підставі отриманих аргументів

    """
    numbers_and_special_chars_percentage = 10
    numbers_and_special_chars_length = math.ceil(length * numbers_and_special_chars_percentage / 100)

    # Генерація випадкових чисел від 0 до 9
    numbers_for_password = [
        str(random.randint(0, 9)) for _ in range(numbers_and_special_chars_length) if use_numbers
    ]
    # Генерація випадкових спеціальних символів
    special_chars_for_password = [
        random.choice(special_characters) for _ in range(numbers_and_special_chars_length) if use_special_chars
    ]

    # Виклик функції для генерації літер для паролю,
    # зменшивши довжину на кількість сгенерованих чисел та спеціальних символів
    chars_for_password = generate_chars(length - len(numbers_for_password) - len(special_chars_for_password))

    # Поєднання літер чисел та спеціальних символів, які будуть використані для створення паролю
    all_chars_for_password = chars_for_password + numbers_for_password + special_chars_for_password

    # Використання функції shuffle p модуля random для того щоб перемішати усі символи,
    # які використовуються для генерації паролю
    random.shuffle(all_chars_for_password)

    # Конвертація списку символів у рядок з паролем
    password = "".join(all_chars_for_password)
    return password
