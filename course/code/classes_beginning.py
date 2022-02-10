# Введення в об'єктно орієнтовне прогрпмування (ООП)
# Створення пустого класу
class Unit:
    pass


first_unit = Unit()
second_unit = Unit()

print("first_unit instance:", first_unit)
print("second_unit instance:", second_unit)
print("Unit class:", Unit)
print("type of first_unit:", type(first_unit))
print("type of second_unit:", type(second_unit))
print("type of Unit class:", type(Unit))


# Створення атрибутів класу
# Класи в Python динамічні
class Unit:
    pass


first_unit = Unit()

first_unit.id = 1
first_unit.name = "Test Unit"


def print_name_id(self):
    print(f"({self.id}) {self.name}")


setattr(Unit, "print_name_id", print_name_id)


first_unit.print_name_id()


# Ініціалізація класу за допомогою метода __init__() (конструктора)
class Unit:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_name_id(self):
        print(f"{self.name} ({self.id})")


some_unit = Unit(2, "Another Unit")
another_unit = Unit(4, "Unit 4")

print(some_unit)
print(another_unit)
some_unit.print_name_id()
another_unit.print_name_id()


# Доступ до атрибутів класу
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


gog = Animal("dog", 3)
cat = Animal("cat", 2)

print(gog.name, gog.age)
print(cat.name, cat.age)


# # Методи класу та доступ до них
class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def raise_salary(self, amount):
        self.salary = self.salary + amount


rob = Employee("rob", "Developer", 3000)

print(rob.salary)

rob.raise_salary(300)

print(rob.salary)


# Змінні класу
class Employee:
    DEFAULT_SALARY_RAISE = 1.2
    employee_counter = 0

    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        Employee.employee_counter += 1

    def raise_salary(self, amount=None):
        if amount:
            self.salary = self.salary + amount
        else:
            self.salary = self.salary * self.DEFAULT_SALARY_RAISE


print(Employee.employee_counter)
rob = Employee("rob", "Developer", 3000)
rob_dict = dict(name="rob", salary=3000)
print(rob)
print(rob_dict)
print(Employee.employee_counter)
will = Employee("will", "Director", 6000)
print(Employee.employee_counter)

print(rob.salary)
print(will.salary)

rob.raise_salary(600)
will.raise_salary()

print(rob.salary)
print(will.salary)


# Наслідування
class Person:
    location = "Ukraine"

    def __init__(self, name):
        self.name = name

    def person_method(self):
        print("It is a method of Person class", self.name)


class Student(Person):
    def __init__(self, first_name, last_name, group):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group

    def student_method(self):
        print("It is a method of Student class", self.name)


class User(Person):
    def __init__(self, name, status):
        super().__init__(name)
        self.status = status


class Teacher(User):
    def teacher_method(self):
        print("It is a method of Teacher class", self.name)


bob = Person("Bob")
roy = Student("Roy", "Smith", 1121)
jack = User("Jack", "active")
dan = Teacher("Dan", "active")

print(bob)
print(roy)
print(jack)
print(dan)
print(type(bob))
print(type(roy))
print(type(jack))
print(type(dan))
print(isinstance(bob, Person))
print(isinstance(bob, User))
print(isinstance(roy, Person))
print(isinstance(roy, Student))
print(isinstance(roy, User))
print(isinstance(dan, Person))
print(isinstance(dan, User))
print(isinstance(dan, Teacher))
