# Робота з реляційними базами даними

# Робота за базою даних SQLite3
import sqlite3  # https://docs.python.org/3/library/sqlite3.html

connector = sqlite3.connect("db.sqlite3")
cursor = connector.cursor()

# Створення нової таблиці
cursor.execute("CREATE TABLE IF NOT EXISTS test (id int, name text)")
connector.commit()

# Додавання запису в базу даних
cursor.execute("INSERT INTO test (id, name) VALUES (?, ?)", (1, "First"))
connector.commit()

# Читання данних з бази даних
result = cursor.execute("SELECT * from test")
print(result)
# cursor.execute() не повертає дані, а повертає об'єкт cursor

# Для отримання даних необхідно викликати cursor.fetchall()
result = cursor.fetchall()
print(result)

test_list = [
    (2, "Second"),
    (3, "Third"),
    (4, "Fourth"),
]
# Додавання декількох рядків одразу
cursor.executemany("INSERT INTO test VALUES (?, ?)", test_list)
connector.commit()

# Оновлення рядків з визначеним id
cursor.execute("UPDATE test SET name = 'Updated Second' WHERE id=:id", {"id": 2})
print(cursor.fetchall())

# Отримання рядків з визначеним id
cursor.execute("SELECT * FROM test WHERE id=:id", {"id": 2})
print(cursor.fetchall())

# Видалення рядків з визначеним id
cursor.execute("DELETE FROM test WHERE id=:id", {"id": 3})
connector.commit()

cursor.execute("SELECT * FROM test WHERE name =:name", {"name": "First"})
print(cursor.fetchone())

connector.close()


# Робота з PostgreSQL за допомогою модуля psycopg2
# pip install psycopg2-binary
import psycopg2  # https://www.psycopg.org/docs/index.html

connector = psycopg2.connect(dsn="postgresql://localhost:5432/postgres")
cursor = connector.cursor()

# Створення нової таблиці з автолічільником у полі id
cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name text)")
connector.commit()

# Додавання запису в базу даних
cursor.execute("INSERT INTO test (name) VALUES (%s)", ("First",))
connector.commit()

# Читання данних з бази даних
cursor.execute("SELECT name from test")

# Для отримання даних необхідно викликати cursor.fetchall()
result = cursor.fetchall()
print(result)

test_list = [
    ("Second",),
    ("Third",),
    ("Fourth",),
]
# Додавання декількох рядків одразу
cursor.executemany("INSERT INTO test (name) VALUES (%s)", test_list)
connector.commit()

# Оновлення рядків з визначеним id
cursor.execute("UPDATE test SET name = 'Updated Second' WHERE id = %s", (2,))

# Отримання рядків з визначеним id
cursor.execute("SELECT * FROM test WHERE id = %s", (2,))
print(cursor.fetchall())

# Видалення рядків з визначеним id
cursor.execute("DELETE FROM test WHERE id = %s", (3,))
connector.commit()

cursor.execute("SELECT * FROM test WHERE name = %s", ("First",))
print(cursor.fetchone())

# Агрегація даних
# Отримання максимального значення
cursor.execute("SELECT MAX(id) from test")
print(cursor.fetchone())

# Отримання мінимального значення
cursor.execute("SELECT MIN(id) from test")
print(cursor.fetchone())

# Отримання кількості записів
cursor.execute("SELECT COUNT(id) from test")
print(cursor.fetchone())

# Отримання унікальних записів
cursor.execute("SELECT DISTINCT(name) from test")
print(cursor.fetchone())

connector.close()

if __name__ == "__main__":
    pass
