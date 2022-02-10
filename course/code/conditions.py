# Умови

# Перевірити чи відноситься число до позитивних чи негативних чисел або чи дорівнює воно "0"
number = int(input("Введіть будь ласка число: "))
if number > 0:
    print("Ви ввели позитивне число")
elif number < 0:
    print("Ви ввели негативне число")
else:
    print("Ви ввели нуль")


# Перевірка довжини спуску, елемента за індексом, та наявності елементу в списку
names = ["max", "bob", "bill", "jane"]
if len(names) >= 4 and (names[3] == "max" or "bob" in names):
    print("Розмір списку імен більше '4' та (або 'max' є елементом з індексом 3 або 'bob' є в цьому списку) ")
else:
    print("Або розмір списку менше '4' або (і елементом з індексом 3 не є 'max' і 'bob' відсутній у цьому списку")

# Запис результату логічного виразу у змінну
is_positive = number > 0
print(is_positive)

# Тринарний оператор
is_zero = "Істина" if number == 0 else "Не Істина"
print(is_zero)

#  Те саме що й у попередньому блоку, але звичайною умовою
if number == 0:
    is_zero = "Істина"
else:
    is_zero = "Не Істина"
print(is_zero)

# Перевірити чи належить число до проміжку
if 10 <= number < 50:
    print(True)

# Порівняння tuples
point = (0, 0)
point_2 = (0, 3)
if point > point_2:
    print("point more than point_2")
else:
    print("point less than point_2")

# Порівняння рядків
andriy = "андрій"
khrystyna = "Христина"
if khrystyna > andriy:
    print("khrystyna more than andriy")
else:
    print("khrystyna less than andriy")

# Конвертація стандартних типів даних у bool
# Усі зазначені нижче значення змінних повернуть False при конвертації у bool

# Нульові значення числових типів даних
int_zero = 0
float_zero = 0.0
complex_zero = 0j

# Пусті послідовності
empty_str = ""
empty_list = []
empty_tuple = ()
empty_set = set()

# Пусті словники
empty_dict = {}

# Об'єкт NoneType
none = None

# Насправді дійсної конвертації не відбувається
some_str = "something"
result = empty_str or some_str
print(result)

# Для дійсної конвертації використовуйте функцію bool()
result = bool(empty_str) or bool(some_str)
print(result)


if int_zero or float_zero or complex_zero or empty_str or empty_list or empty_tuple or empty_set or empty_dict or none:
    print(True)
else:
    print(False)


# Використання конструкції match-case для розгалудження логіки програми
part_of_day = input("Введіть будь ласка час доби (ранок, день, вечір, не знаю): ")
match part_of_day:
    case "ранок":
        print("Добрий ранок")
    case "день":
        print("Добрий день")
    case "вечір":
        print("Добрий вечір")
    case _:
        print("Бажаю здоров'я")

# Та сама логіка, але з використанням if-elif-else конструкції
part_of_day = input("Введіть будь ласка час доби (ранок, день, вечір, не знаю): ")
if part_of_day == "ранок":
    print("Добрий ранок")
elif part_of_day == "день":
    print("Добрий день")
elif part_of_day == "вечір":
    print("Добрий вечір")
else:
    print("Бажаю здоров'я")
