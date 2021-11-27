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

# Поєднання списків методом додавання
chars = chars + new_chars
print(chars)


# tuple
user_statuses = ("active", "inactive", "pending")
new_user_statuses = "active", "inactive", "pending"
statuses = ["active", "inactive", "pending"]
new_statuses = tuple(statuses)

# set
users = {"bob", "bill", "max"}
users_new = ["bob", "bill", "max", "bob"]
unique_users = set(new_users)