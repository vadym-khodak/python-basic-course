# Функції вищого порядку

# Зведення у другу ступінь кожного числа з послідовності за допомого циклу for
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = []
for number in numbers:
    result.append(number ** 2)

print(result)


# Зведення у другу ступінь кожного числа з послідовності
# за допомого циклу for та винесенням частини логіку у окрему функцію
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def pow_number(x):
    return x ** 2


result = []
for number in numbers:
    result.append(pow_number(number))

print(result)


# Зведення у другу ступінь кожного числа з послідовності
# за допомого циклу for та винесенням частини логіку у окрему lambda функцію
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def pow_number(x):
    return x ** 2


result = []
result_lambda = []
for number in numbers:
    result.append(pow_number(number))
    result_lambda.append((lambda x: x ** 2)(number))

print(result)


# Зведення у другу ступінь кожного числа з послідовності за допомого функції map()
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = list(map(lambda x: x ** 2, numbers))


print(result)


# Фільтрування послідовності чисел для отримання тільки парних чисел за допомогою циклу з умовою
import sys
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

filtered_numbers = []
for number in numbers:
    if number % 2 == 0:
        filtered_numbers.append(number)


result = list(map(lambda x: x ** 2, filtered_numbers))


print(sys.getsizeof(filtered_numbers))
print(result)

# Фільтрування послідовності чисел для отримання тільки парних чисел за допомогою функції filter()
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
print(sys.getsizeof(filtered_numbers))
print(sys.getsizeof(list(filtered_numbers)))

result = list(map(lambda x: x ** 2, filtered_numbers))


print(result)


# Фільтрування послідовності чисел, використання функцій map() та filter() у одному рядку
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))


print(result)


# Отримання суми квадратів парних чисел пурших десяти чисел з послідовності Фібоначчі
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

sum_ = 0
for number in result:
    sum_ += number

print(sum_)

# Отримання суми квадратів парних чисел пурших десяти чисел з послідовності Фібоначчі за допомогою функції reduce()
from functools import reduce

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(result)


# Отримання факторіалу числа за допомогою функції reduce()
from functools import reduce

numbers = range(1, 10)


def f(x, y):
    return x * y


result = reduce(f, numbers)

result_lambda = reduce(lambda x, y: x * y, numbers)


print(result)
print(result_lambda)
