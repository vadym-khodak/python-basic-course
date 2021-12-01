# set - набір унікальних значень (елементами сету можуть бути тільки незмінювані типи даних)
# Ініціалізація змінних типу list
users = {"will", "brian", "jack"}
new_users = ["bob", "bill", "will", "bob"]

unique_users = set(new_users)
print(unique_users)

empty_set = set()
print(empty_set)





















# Переглянути усі атрибути типу set
print(dir(set))
print(dir(unique_users))

# Переглянути довідку по типу set
print(help(set))
print(help(unique_users))





















# Додавання елементу до set
print(unique_users)
unique_users.add("max")
print(unique_users)
unique_users.add("max")
print(unique_users)




















# Отримання різниці між двома sets
print(unique_users)
print(users)
print(unique_users.difference(users))
print(unique_users - users)

# Отримання перехрещення двох sets
print(unique_users.intersection(users))

# Отримання перехрещення двох sets
print(unique_users.symmetric_difference(users))



























# Видалення та повернення випадкового елементу з set
print(unique_users.pop())
print(unique_users)

# Видалення елементу з set
unique_users.remove("bill")
print(unique_users)

# Видалення елементу з set
unique_users.discard("bill")
print(unique_users)




















# Поєднання двох sets та повернення результату як новий set
print(unique_users.union(users))

# Оновлення set
unique_users.update(users)
print(unique_users)

# Створення неглибокої копії set
copied_set = unique_users.copy()
print(copied_set)
print(id(unique_users))
print(id(copied_set))





















# Очищення set
print(unique_users)
unique_users.clear()
print(unique_users)




















if __name__ == "__main__":
    pass
