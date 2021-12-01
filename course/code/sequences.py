# list - рядок, послідовність символів

# Ініціалізація змінних типу list
names = ["john", "rob", "bill"]
chars = list("hello")
new_chars = ['h', 'e', 'l', 'l', 'o']
new_users = []
numbers = list(range(1, 11))

























# Перевірка типу
print(type(names))
# Перевірка змінної типу list
print("rob" in names)
print(chars == new_chars)






















# Отримання довжини списку
print(len(names))

# Отримання елемента списку за індексом
# першого
print(names[0])  # надрукує рядок "john"

# останнього
print(names[0])  # надрукує рядок "john"
print(names[-1])  # надрукує рядок "bill"

# Отримання зрізу списку (елементи з індексом від 1 включно до 5 виключно)
print(numbers[1:5])  # надрукує частину списку (зріз) [2, 3, 4, 5]
# від елементу з індексом 6 до кінця списку
print(numbers[6:])  # надрукує частину списку (зріз) [7, 8, 9, 10]
# від елементу з індексом 6 до останньої літери виключно
print(numbers[6:-1])  # надрукує частину списку (зріз) [7, 8, 9]
# від елементу з індексом 0 до 5 виключно
print(numbers[:5])  # надрукує частину списку (зріз) [1, 2, 3, 4, 5]
# від початку списку до кінця з кроком 2 (0, 2, 4, 6, 8, 10)
print(numbers[:5])  # надрукує частину списку [1, 2, 3, 4, 5]
# від кінця списку до початку з кроком -1
print(numbers[-1::-1])  # надрукує частину рядка "niarb s'neM"





























# Переглянути усі атрибути типу list
print(dir(list))
print(dir([]))
print(dir(names))

# Переглянути довідку по типу list
print(help(list))
print(help([]))
print(help(names))





























# Робота з методами типу list
# Порахувати кількість елементів "l"
print(new_chars.count("l"))
# Знайти індекс першої літери "l" з ліва направо
print(new_chars.index("l"))






















# Додавання елементу у кінець списку
print(names)
names.append("jason")
print(names)

# Додавання елементу у вказану позицію
print(names)
names.insert(2, "max")
print(names)

# Заміна елемента у списку
print(names)
names[1] = "brian"
print(names)

# Видалення елементу зі списку
names.remove("brian")
print(names)

# Видалення та повернення елементу зі списку
name = names.pop(3)
print(names)
print(name)





















# Поєднання списків методом додавання
sum_chars = chars + new_chars
print(sum_chars)
# Розширення існуючого списку
chars.extend(new_chars)
print(chars)



















# Сортування списку
names.sort()
print(names)

# Сортування від більшого до меншого
names.sort(reverse=True)
print(names)

names.reverse()
print(names)




















# Створення неглибокої копії списку
additional_names = ["joey", "bred"]
names.append(additional_names)
copied_names = names.copy()
print(copied_names)
print(id(names))
print(id(copied_names))
print(id(copied_names[-1]))
print(id(additional_names))

additional_names.append("jeremy")
print(additional_names)
print(copied_names[-1])





















# Очищення списку
names.clear()
print(names)



















# Робота із вкладеними списками

matrix = [
    [1, 3, 4],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix)

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][0])




















# tuple - кортеж, незмінювана послідовність об'єктів
# Ініціалізація змінних типу tuple
user_statuses = ("active", "inactive", "pending")
new_user_statuses = "active", "inactive", "pending"
statuses = ["active", "inactive", "pending"]
new_statuses = tuple(statuses)
new_chars = tuple(new_chars)
print(statuses)
print(new_statuses)


















# Переглянути усі атрибути типу tuple
print(dir(tuple))
print(dir(()))
print(dir(new_statuses))

# Переглянути довідку по типу tuple
print(help(tuple))
print(help(()))
print(help(new_statuses))





















# Робота з методами типу tuple
# Порахувати кількість елементів "l"
print(new_chars.count("l"))
# Знайти індекс першої літери "l" з ліва направо
print(new_chars.index("l"))




















if __name__ == "__main__":
    pass
