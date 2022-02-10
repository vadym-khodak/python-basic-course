# Magic/Dunder methods


class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def __str__(self):
        return f"{self.name}, {self.job_title} (salary: {self.salary})"

    def __repr__(self):
        return f"Employee(name='{self.name}', job_title='{self.job_title}', salary={self.salary})"


john = Employee("John", "developer", 3000)
print(john)
print(repr(john))
print(john.__repr__())


# Успадкування
from datetime import date


class MyDate(date):
    month_map = {
        1: "Січень",
        2: "Лютий",
        3: "Березень",
        4: "Квітень",
        5: "Травень",
        6: "Червень",
        7: "Липень",
        8: "Серпень",
        9: "Вересень",
        10: "Жовтень",
        11: "Листопад",
        12: "Грудень",
    }

    def __new__(cls, year, month, day):
        self = super().__new__(cls, year, month, day)
        self.ukraine_month = MyDate.month_map.get(month)
        return self


today = MyDate.today()

print(today)
print(today.ukraine_month)

today.ukraine_month = "February"

print(today.ukraine_month)
print(today)

print(MyDate(2022, 8, 1).ukraine_month)


# Інкапсуляція
from datetime import date, timedelta


class MyDate(date):
    __month_map = {
        1: "Січень",
        2: "Лютий",
        3: "Березень",
        4: "Квітень",
        5: "Травень",
        6: "Червень",
        7: "Липень",
        8: "Серпень",
        9: "Вересень",
        10: "Жовтень",
        11: "Листопад",
        12: "Грудень",
    }

    def get_ukraine_month(self):
        return self.__month_map.get(self.month)


today = MyDate.today()

print(today.get_ukraine_month())

in_month = today + timedelta(days=30)

print(in_month.get_ukraine_month())


# Використання декоратора @property
from datetime import date


class MyDate(date):
    __month_map = {
        1: "Січень",
        2: "Лютий",
        3: "Березень",
        4: "Квітень",
        5: "Травень",
        6: "Червень",
        7: "Липень",
        8: "Серпень",
        9: "Вересень",
        10: "Жовтень",
        11: "Листопад",
        12: "Грудень",
    }

    @property
    def ukraine_month(self):
        return self.__month_map.get(self.month)


today = MyDate.today()

print(today.ukraine_month)

# today.ukraine_month = "January"  # AttributeError: can't set attribute


# Поліморфізм
class Couple:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f"{self.first} and {self.second}"


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.is_couple = False

    def __str__(self):
        return self.name

    def __add__(self, person):
        if self.is_couple or person.is_couple:
            return "You can't have more than one couple."
        if self.gender == person.gender:
            return "You can't create a couple with person with the same gender"
        self.is_couple = person.is_couple = True
        return Couple(self, person)


marry = Person("Marry", "female")
garry = Person("Garry", "male")
print(marry.is_couple, garry.is_couple)

marry_garry = marry + garry

print(marry_garry)
print(marry.is_couple, garry.is_couple)


# Абстракція
from abc import ABC, abstractmethod


class Animal(ABC):
    """This is an Animal class"""

    def __init__(self, name):
        self.name = name

    def description(self):
        print(self.__doc__)

    @abstractmethod
    def say(self, phrase=None):
        pass


class Dog(Animal):
    """This is a Dog class"""

    def say(self, phrase=None):
        if not phrase:
            print("woof")
        else:
            print("woof " * len(phrase.split()))


class Cat(Animal):
    """This is a Cat class"""

    def say(self, phrase=None):
        if not phrase:
            print("purr")
        else:
            print("meow " * len(phrase.split()))


jack = Dog("Jack")

jack.description()
jack.say()
jack.say("Hello people")


asia = Cat("Asia")
asia.description()
asia.say()
asia.say("Hello people")


# classmethod
class Employee:
    __default_salary_raise = 1.2
    __employee_counter = 0

    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        Employee.__employee_counter = Employee.__employee_counter + 1

    def raise_salary(self, amount=None):
        if amount:
            self.salary = self.salary + amount
        else:
            self.salary = self.salary * self.__default_salary_raise

    @classmethod
    def change_default_salary_raise(cls, new_value):
        cls.__default_salary_raise = new_value


will = Employee("will", "Director", 6000)

print(will.salary)

will.raise_salary()

print(will.salary)

Employee.change_default_salary_raise(1.5)

will.raise_salary()

print(will.salary)


# staticmethod
class Date:
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")


date_ = Date("12-01-2022")
dateFromDB = "12/01/2022"
dateWithDash = Date.to_dash_date(dateFromDB)


if date_.get_date() == dateWithDash:
    print("Equal")
else:
    print("Not equal")


# dataclasses
from dataclasses import dataclass, astuple, asdict


@dataclass
class User:
    _id: int
    name: str
    status: str


roy = User(1, "Roy", "active")

print(roy)
print(asdict(roy))
print(astuple(roy))
