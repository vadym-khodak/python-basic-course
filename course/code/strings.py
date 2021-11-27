# str - рядок, послідовність символів

# Ініціалізація змінних типу str
message_1 = "Men's brain"
message_2 = '"1984" George Orwell. It\'s a cool book.'
message_3 = """
Dear friend.        I hope you are doing well.  
Warm regards,
Your friend
"""
message_4 = '''
Dear friend,
I hope you are doing well.
Warm regards,
Your friend
'''

# Перевірка типу
print(type(message_1))
print('"' in message_2)
print(message_1 == message_2)
print(message_3 == message_4)
print("Ab" > "Aa")

# Отримання довжини рядка
print(len(message_1))

# Отримання елемента рядка за індексом
# першого
print(message_1[0])  # надрукує літеру "M"

# останнього
print(message_1[len(message_1) - 1])  # надрукує літеру "n"
print(message_1[-1])  # надрукує літеру "n"

# Отримання зрізу рядка (елементи з індексом від 2 включно до 5 виключно)
print(message_1[2:5])  # надрукує частину рядка (зріз) "n's"

# від елементу з індексом 6 до кінця рядку включно
print(message_1[6:])  # надрукує частину рядка (зріз) "brain"

# від елементу з індексом 6 до останньої літери виключно
print(message_1[6:-1])  # надрукує частину рядка (зріз) "brai"

# від елементу з індексом 0 до 5 виключно
print(message_1[:5])  # надрукує частину рядка (зріз) "Men's"

# від початку рядка до кінця з кроком 2 (0, 2, 4, 6, 8, 10)
print(message_1[::2])  # надрукує частину рядка "Mnsban"

# від кінця рядка до початку з кроком -1
print(message_1[-1::-1])  # надрукує частину рядка "niarb s'neM"

# Переглянути усі атрибути типу str
print(dir(str))
print(dir(""))
print(dir(message_1))

# Переглянути довідку по типу str
print(help(str.capitalize))
print(help(""))
print(help(message_1))

# Робота з методами типу str
# Порахувати кількість літер "о"
print(message_3.count("o"))

# Знайти індекс першої літери "о" з ліва направо
print(message_3.find("o"))

# Знайти індекс першої літери "о" з права наліво
print(message_3.rfind("o"))

# Знайти індекс першої літери "о" з ліва направо (помилка якщо така літера відсутня)
print(message_3.index("o"))

# Знайти індекс першої літери "о" з права наліво (помилка якщо така літера відсутня)
print(message_3.rindex("o"))

# Методи для роботи регістру
print(message_1.upper())  # "MEN'S BRAIN"
print(message_1.lower())  # "men's brain"
print("hello world".capitalize())  # "Hello world"
print("hello world".title())  # "Hello World"
print(message_2.swapcase())  # '"1984" gEORGE oRWELL. iT\'S A COOL BOOK.'

# Перевірка рядка
print("vadym.khodak@gmail.com".startswith("vadym"))  # True
print("vadym.khodak@gmail.com".startswith("Vadym"))  # False
print("vadym.khodak@gmail.com".endswith("gmail.com"))  # True
print("vadym.khodak@gmail.com".endswith("ukr.net"))  # False
print("khodak" in "vadym.khodak@gmail.com")  # True
print("   vadym.khodak@gmail.com   " == "vadym.khodak@gmail.com")  # False

# Видалення пробільних символів
print("   vadym.khodak@gmail.com   ".strip())   # "vadym.khodak@gmail.com"
print("   vadym.khodak@gmail.com   ".rstrip())  # "   vadym.khodak@gmail.com"
print("   vadym.khodak@gmail.com   ".lstrip())  # "vadym.khodak@gmail.com   "

print(message_3.replace("Dear friend", "Hello").swapcase()[-1::-1])
print(id(message_3))

message_3 = message_3.replace("Dear friend", "Hello")
print(id(message_3))
message_3 = message_3.swapcase()
print(id(message_3))

message_3 = message_3[-1::-1]
print(id(message_3))

# Поєднання рядків методом додавання
print("Hello" + " " + "World" + "!")

# Поєднання рядків методом join
names = ["max", "bob", "john"]
print(", ".join(names))

# Форматування рядків
print("Hello %s %s %d" % ("World!", "HI", 5678))  # python2
print("Hello {1} {0}".format("Doe", "John"))
print("Hello {first_name} {last_name}".format(last_name="Doe", first_name="John!"))
name = "John!"
print(f"Hello {name + ' ' + 'Doe'}")
print(r"hello\nworld")

# Розділення рядків
print("max, bob, john".split(", "))
for name in "max bob john".split(" "):
    print(name)


if __name__ == "__main__":
    pass
