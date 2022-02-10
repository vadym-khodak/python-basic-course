# Імпортування необхідних модулів
import csv
import json
import random
import pickle
import sys


# Відкриття файлу у режимі запису/write данних
file = open("temp.txt", "w")
file.write("Hello World!")
file.close()

# Відкриття файлу у режимі читання/read даних
file = open("temp.txt", "r")
text = file.read()
print(text)
file.close()

# Відкриття файлу у режимі додавання/append даних
file = open("temp.txt", "a")
file.write("\n")
file.write("Hello Group!")
file.close()

file = open("temp.txt", "r")
text = file.read()
print(text)
file.close()


# Запис списку рядків у текстовий файл
# Використання with виразу для відкриття файлу
with open("temp.txt", "w") as file:
    numbers = []
    for _ in range(5):
        numbers.append(str(random.randint(-1000, 1000)) + "\n")
    print(numbers)
    file.writelines(numbers)
    # Те саме що і writelines
    # for item in numbers:
    #     file.write(item)

with open("temp.txt", "r") as file:
    lines = file.readlines()
    print(lines)


with open("temp.txt", "r") as file:
    text = file.read()
    print(text)


# Робота з csv файлами - Coma Separated Values
with open("temp.csv", "w") as file:
    numbers = ["ind,negative,positive\n"]
    for i in range(1, 11):
        numbers.append(f"{i},{random.randint(-1000, 0)},{random.randint(1, 1000)}\n")
    print(numbers)
    file.writelines(numbers)

with open("temp.csv", "r") as file:
    lines = file.readlines()
    print(lines)
    file_data = []
    for i, line in enumerate(lines):
        items = line.strip().split(",")
        if i == 0:
            header = items
            continue
        row_data = {}
        for j, value in enumerate(items):
            row_data[header[j]] = value
        file_data.append(row_data)

print(file_data)


# Допоміжна функція для генерації тестових даних для запису у файл
def generate_numbers(with_bool=False):
    _numbers = []
    for index in range(1, 11):
        _row = {
            "ind": index,
            "negative": random.randint(-1000, 0),
            "positive": random.randint(1, 1000),
        }
        if with_bool:
            _row.update({"is_good": random.choice([True, False, None])})

        _numbers.append(_row)

    return _numbers


print(generate_numbers())
print(generate_numbers(with_bool=True))


# Використання модуля csv для роботи з csv файлами
with open("temp.csv", "w") as file:
    csv_dict_writer = csv.DictWriter(file, ["ind", "negative", "positive"])
    numbers = generate_numbers()
    print(numbers)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(numbers)

with open("temp.csv", "r") as file:
    csv_dict_reader = csv.DictReader(file)
    print(list(csv_dict_reader))
    for row in csv_dict_reader:
        print(row)


# Робота з форматом json - JavaScrypt Object Notation
with open("temp.json", "w") as file:
    numbers = generate_numbers()
    print(numbers)
    file.write(str(numbers).replace("'", '"'))

with open("temp.json", "r") as file:
    json_text = file.read()
    print(json_text)
    data = eval(json_text)
    print(data)


# Використання модулю json для конвертації Python об'єкту у json рядок та назад
with open("temp.json", "w") as file:
    numbers = generate_numbers(with_bool=True)
    print(numbers)
    file.write(json.dumps(numbers))

with open("temp.json", "r") as file:
    json_text = file.read()
    print(json_text)
    data_loads = json.loads(json_text)
    print(data_loads)

with open("temp.json", "r") as file:
    data = json.load(file)
    print(data)


# Використання відкриття файлу на читання/запис у режимі bytes
with open("example.pdf", "rb") as file:
    data = file.read()


with open("new_example.pdf", "wb") as file:
    file.write(data)


# Використання методів dumps та loads модулю/бібліотеки pickle для конвертації Python об'єкту у bytes
with open("data.pickle", "wb") as file:
    numbers = generate_numbers(with_bool=True)
    pickle_data = pickle.dumps(numbers)
    print(pickle_data)
    file.write(pickle_data)

# Порівняння розміру Python об'єкту, json рядку, та bytes рядку
json_data = json.dumps(numbers)
print(sys.getsizeof(numbers))
print(sys.getsizeof(pickle_data))
print(sys.getsizeof(json_data))

with open("data.pickle", "rb") as file:
    pickle_data = file.read()
    data = pickle.loads(pickle_data)
print(data)


# Використання методів dump та load модулю/бібліотеки pickle
with open("data_1.pickle", "wb") as file:
    pickle.dump(numbers, file)

with open("data_1.pickle", "rb") as file:
    data = pickle.load(file)
print(data)


# Домашнє завдання
# Звичайний рівень
# Написати функцію, яка приймає назву текстового файлу (file_name: str) та текст (text: str) та робить наступні дії:
# - створє новий текстовий файл з отриманою назвою file_name
# - записує у цей файл отриманий текст text
# - додає у цей файл рядок з випадковим цілим позитиним числом (n: int) від 1-10 включно.
# - читає файл та вибирає з тексту файлу це ціле число.
# - створює новий файл з назвою file_name та префіксом new_
# - записує у новий файл текст text n разів
# - читає цей новий файл та повертає tuple, де першим елементом є n, а другим текст нового файлу.
#
# Ускладнений рівень
# Написати клас Converter
# Який може конвертувати дані з csv, json, pickle форматів у csv, json, pickle формати.
# Клас приймає назву файлу при ініціалізації та має наступні методи:
# - to_csv конвертує переданий файл у формат csv, якщо переданий файл вже у форматі csv то друкує про це повідлмлення
# - to_json конвертує переданий файл у формат json, якщо переданий файл вже у форматі json то друкує про це повідлмлення
# - to_pickle конвертує переданий файл у формат pickle, якщо переданий файл вже у форматі pickle то друкує про це повідлмлення
