# Використання власних модулей
# Імпортування пакету
import test_package

print(dir(test_package))
print(test_package.test_module.TEST_CONSTANT)


# Імпортування модуля
from test_package import test_module

print(dir(test_module))
print(test_module.TEST_CONSTANT)
print(test_module.test_variable)
test_module.test_function()
test_module.test_function("Vadym")

import demo_module

print(__name__)


# Імпортування функції
from test_package.test_module import test_function

print(test_function)
test_function()
test_function("Vadym")


# Імпортування функції з псевдонімом
from test_package.test_module import test_function
from test_package.another_test_module import test_function as another_test_function

print(test_function)
test_function()
test_function("Vadym")

print(another_test_function)
another_test_function()
another_test_function("Vadym")


# Імпортування змінної/константи
from test_package.test_module import TEST_CONSTANT, test_variable
print(TEST_CONSTANT)
print(test_variable)


# Імпортування всього
from test_package.test_module import test_function
print(test_function)
test_function()
test_function("Vadym")

from test_package.another_test_module import *
print(test_function)
test_function()
test_function("Vadym")


# Використання вбудованих бібліотек
# Бібліотека os
import os

for attr in dir(os):
    if not attr.startswith("_"):
        print(attr)

print(help(os.getcwd))
print(os.getcwd())
print(os.listdir())
os.mkdir("temp")
print(os.listdir())
os.chdir("temp")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
print(os.listdir())
os.rmdir("temp")
print(os.listdir())
os.system("ls")


# Бібліотека sys
import sys

for attr in dir(sys):
    if not attr.startswith("_"):
        print(attr)

print(help(sys))

print(sys.argv)
print(sys.path)
print(sys.platform)
print(sys.version)
print(sys.getsizeof("String"))
print(sys.getsizeof(list("String")))
print(sys.getsizeof(tuple("String")))
print(sys.getsizeof(set("String")))


# Бібліотека itertools
import itertools

for attr in dir(itertools):
    if not attr.startswith("_"):
        print(attr)

print(help(itertools))


# itertools.groupby
users = [
    {"name": "max", "status": "active"},
    {"name": "bob", "status": "inactive"},
    {"name": "bill", "status": "pending"},
    {"name": "john", "status": "pending"},
    {"name": "brian", "status": "inactive"},
    {"name": "dan", "status": "active"},
    {"name": "will", "status": "active"},
    {"name": "jack", "status": "inactive"},
]

users.sort(key=lambda i: i["status"])

for grouper, group in itertools.groupby(users, key=lambda i: i["status"]):
    print(grouper)
    for item in group:
        print(item)


# itertools.cycle
counter = 0
from_zero_to_ten = range(11)

for i in itertools.cycle(from_zero_to_ten):
    if counter > 25:
        break
    print(i)
    counter += 1


# Бібліотека collections
import collections

for attr in dir(collections):
    if not attr.startswith("_"):
        print(attr)

print(help(collections))


# collections.Counter
some_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris feugiat pulvinar aliquam. Duis ac consectetur lectus. Curabitur interdum, justo vitae convallis pharetra, tortor quam rhoncus ipsum, a sagittis lectus ipsum a orci. Donec non orci tellus. Curabitur volutpat consectetur ante id ornare. Maecenas et lorem vitae massa tincidunt volutpat in in tortor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Quisque a nibh vitae velit convallis interdum a at felis. Fusce id dolor egestas, maximus orci a, sodales nisi.
Duis semper erat ut nibh dictum finibus. Aliquam eget accumsan neque. Nullam volutpat, dolor in aliquet aliquam, ante lectus dignissim erat, in egestas mauris tellus eu tortor. Ut non varius sem, ut commodo nisi. Donec tellus nibh, varius vel nibh ac, auctor laoreet sem. Proin non venenatis nisl. Integer rutrum, urna vel suscipit euismod, sapien lacus feugiat sapien, a congue nunc dui ac ante. Phasellus vel tellus dictum leo aliquam faucibus. Fusce elementum, orci sed gravida dapibus, nisl ante bibendum mi, nec sollicitudin ante nisi in lacus.
Suspendisse potenti. Maecenas tristique posuere purus, ac sollicitudin justo tempus vitae. Morbi nec euismod tellus. Curabitur urna purus, commodo at porttitor ut, mattis nec quam. In congue vel metus id pellentesque. Praesent tristique mi sed interdum laoreet. Quisque quis enim eu lacus tincidunt sagittis non nec urna. Aenean scelerisque nec justo vel efficitur.
Aenean quis rutrum nisl. Maecenas pharetra tortor scelerisque, aliquet lacus eget, posuere elit. In dapibus porta nulla. Nulla gravida accumsan augue, nec vulputate metus tempor in. Praesent nec leo odio. Sed risus tortor, eleifend quis euismod vel, malesuada scelerisque lectus. Donec eget iaculis elit. Nullam nibh nunc, ullamcorper ornare eros eget, vehicula ornare ex. Vestibulum non eros aliquet, ullamcorper turpis eu, blandit arcu. Nunc tincidunt, purus et fermentum ullamcorper, elit arcu gravida sapien, placerat malesuada mauris turpis eu nunc. Nulla eu nisl quis tortor dictum aliquet ac vel metus. Curabitur augue lacus, scelerisque in arcu egestas, vulputate accumsan dui. Donec viverra arcu scelerisque quam ullamcorper euismod. Nunc molestie metus ut urna venenatis, sit amet posuere metus tincidunt. Duis vel augue lacus.
Pellentesque maximus molestie aliquet. Sed laoreet dui massa, a accumsan felis dapibus at. Nullam vel fermentum sapien, in luctus sem. Nam at ligula purus. Quisque id lacus eu est congue ornare a sit amet ipsum. Suspendisse ac leo non felis venenatis laoreet eu non augue. Praesent sollicitudin erat sit amet mi convallis cursus. Vestibulum neque diam, congue id lobortis rutrum, volutpat a nibh. Donec vel fringilla tellus, vel rutrum mauris. Duis efficitur nisi ac lacus gravida, sit amet iaculis lacus mollis. In hac habitasse platea dictumst."""

counter = collections.Counter(some_text.replace(",", "").replace(".", "").replace("\n", " ").split(" "))
for word, times in counter.items():
    print(f"Word '{word}' appears {times} times.")


# collections.defaultdict
users = [
    {"name": "max", "status": "active"},
    {"name": "bob", "status": "inactive"},
    {"name": "bill", "status": "pending"},
    {"name": "john", "status": "pending"},
    {"name": "brian", "status": "inactive"},
    {"name": "dan", "status": "active"},
    {"name": "will", "status": "active"},
    {"name": "jack", "status": "inactive"},
]

users_by_status = collections.defaultdict(list)
for user in users:
    users_by_status[user["status"]].append(user)

print(users_by_status)


# Бібліотека datetime
import datetime

for attr in dir(datetime):
    if not attr.startswith("_"):
        print(attr)

print(help(datetime.datetime))


for attr in dir(datetime.datetime):
    if not attr.startswith("_"):
        print(attr)
print(help(datetime.datetime))


for attr in dir(datetime.date):
    if not attr.startswith("_"):
        print(attr)
print(help(datetime.date))

for attr in dir(datetime.time):
    if not attr.startswith("_"):
        print(attr)
print(help(datetime.time))


# datetime.datetime
now = datetime.datetime.now()
utcnow = datetime.datetime.utcnow()
new_year = datetime.datetime(2022, 1, 1, 0, 0, 0)

print(now)
print(utcnow)
print(new_year)

print(new_year - now)


# datetime.datetime.strftime and datetime.datetime.strptime

now = datetime.datetime.utcnow()
now_str = now.strftime("%d %b %Y %H hours %M minutes %S seconds (%A)")
print(now_str)

new_year_str = "January, 1, 2022"
new_year = datetime.datetime.strptime(new_year_str, "%B, %d, %Y")
print(new_year)


# datetime.date and datetime.timedelta

today = datetime.date.today()

print(today)
print(today.ctime())

new_year = datetime.date(2022, 1, 1)
print(new_year)
print(new_year.strftime("%A"))
print(new_year.isoweekday())
print(new_year.weekday())

day_after_new_year = new_year + datetime.timedelta(days=2)
print(day_after_new_year)
print(day_after_new_year.strftime("%A"))
print(day_after_new_year.isoweekday())
print(day_after_new_year.weekday())


# Бібліотека time
import time

start = time.time()
print(start)
time.sleep(6)
print(time.time() - start)
print(time.localtime())
