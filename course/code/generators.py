# Створення генератора за допомогою generator comprehension
import sys

names = ["max", "rob", "bill", "john", "dan"]

names_generator = (name.title() for name in names)

print(names_generator)
print(sys.getsizeof(names))
print(sys.getsizeof(names_generator))
# Використання функції next() для отримання чергового елементу генератора
print(next(names_generator))

# Ітерування по генератору за допомогою циклу
print("before the loop")
for name in names_generator:
    print(name)


# # Створення генератора за допомогою функції та yield
def generator(iterable):
    for item in iterable:
        yield item.title()


names_generator = generator(names)

print(names_generator)

# Використання функції next() для отримання чергового елементу генератора
print(next(names_generator))

# Ітерування по генератору за допомогою циклу
print("before the loop")
for name in names_generator:
    print(name)


# Нескінченний генератор
def generator_random_int(start=-1000, end=1000):
    import random

    while True:
        yield random.randint(start, end)
        print("After yield")


gen = generator_random_int(start=-10, end=10)

print(gen)
print(next(gen))
print(next(gen))

counter = 0
for i in gen:
    if counter > 10:
        break
    print(i)
    counter += 1


# Використання функції генератора для читання файлу частинами
def get_chunk_of_lines(file_name: str, lines_in_chunk: int = 1):
    chunk = []
    with open(file_name, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            chunk.append(line.replace("\n", ""))
            if len(chunk) == lines_in_chunk:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


gen = get_chunk_of_lines("temp.txt", 2)
for i in gen:
    print(i)


# ДОМАШНЄ ЗАВДАННЯ
# Написати нескінченний генератор для генерації послідовності Фібоначчі
