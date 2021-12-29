
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = []
for number in numbers:
    result.append(number ** 2)

print(result)




































numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def pow_number(x):
    return x ** 2


result = []
for number in numbers:
    result.append(pow_number(number))

print(result)





































numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = []
for number in numbers:
    result.append((lambda x: x ** 2)(number))

print(result)

























numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = map(lambda x: x ** 2, numbers)


print(result)



























numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

filtered_numbers = []
for number in numbers:
    if number % 2 == 0:
        filtered_numbers.append(number)
result = list(map(lambda x: x ** 2, filtered_numbers))


print(result)


























numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

filtered_numbers = filter(lambda x: x % 2 == 0, numbers)

result = list(map(lambda x: x ** 2, filtered_numbers))


print(result)


























numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))


print(result)





























numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

sum_ = 0
for number in result:
    sum_ += number

print(sum_)































from functools import reduce

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


result = reduce(lambda x, y: x + y, list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))))



print(result)





























from functools import reduce

numbers = range(1, 10)


result = reduce(lambda x, y: x * y, numbers)


print(result)



