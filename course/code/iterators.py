# Створення ітератору за допомогою функції iter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_iterator = iter(numbers)

print(numbers_iterator)
print(next(numbers_iterator))


print("before the loop")
for number in numbers_iterator:
    print(number)


# Написання класу ітератора (методи __iter__ та __next__ обов'язкові)
class FileReader:
    def __init__(self, file_name, lines_in_chunk=2):
        self.file_name = file_name
        self.file = open(file_name, "r")
        self.lines_in_chunk = lines_in_chunk

    def __iter__(self):
        return self

    def __next__(self):
        chunk = []
        for _ in range(self.lines_in_chunk):
            line = self.file.readline()
            if not line:
                if chunk:
                    return chunk
                self.file.close()
                raise StopIteration
            chunk.append(line.replace("\n", ''))
        return chunk


file_reader_iterator = FileReader('temp.txt', 2)
print(file_reader_iterator)
print(next(file_reader_iterator))

print("before the loop")
for lines in file_reader_iterator:
    print(lines)


# ДОМАШНЄ ЗАВДАННЯ
# Написати ітератор який буде повертати N чисел послідовності Фібоначчі
# N передається як аргумент під час створення екземпляру цього класу ітератора
