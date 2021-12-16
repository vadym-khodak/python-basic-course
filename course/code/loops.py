# Цикли

name = None
counter = 1
while not name:
    print(counter)
    name = input("Enter your name: ")
    print("I'm in a loop")
    counter += 1

print(f"Hello {name}")


counter = 0
numbers = []
while counter < 5:
    num = int(input("Enter integer number: "))
    numbers.append(num)
    counter += 1

print(sum(numbers))


result = 0
for number in range(5):
    print(number)
    num = int(input("Enter integer number: "))
    result += num

print(result)


names = ["max", "bob", "rob"]
for index in range(len(names)):
    print(index)
    print(f"Hello {names[index]}")


names = ["max", "bob", "rob"]
for name in names:
    print(f"Hello {name}")


username_by_id = {1335: "max", 2335: "bob", 324343: "rob"}
for user_id, name in username_by_id.items():
    print(user_id, name)
    print(f"Hello {name}")


username_by_id = {1335: "max", 2335: "bob", 324343: "rob"}
for name in username_by_id.values():
    if name == "bob":
        continue
    print(f"Hello {name}")


result = 0
while True:
    num = int(input("Enter number: "))
    result += num
    if result < 100:
        continue
    break

print(result)


name = ""
counter = 0
while not name:
    if counter > 0:
        print(f"You have {3 - counter} attempts")
    name = input("Enter your name: ")
    counter += 1
    if counter > 2:
        print(f"You made {counter} attempts")
        break

else:
    print(f"Hello {name}")
