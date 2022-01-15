import random

file = open("temp.txt", "w")
file.write("Hello World!")
file.close()

file = open("temp.txt", "r")
text = file.read()
print(text)
file.close()

file = open("temp.txt", "a")
file.write("\n")
file.write("Hello Group!")
file.close()

file = open("temp.txt", "r")
text = file.read()
print(text)
file.close()


with open("temp.txt", "w") as file:
    numbers = []
    for _ in range(5):
        numbers.append(str(random.randint(-1000, 1000)) + "\n")
    print(numbers)
    file.writelines(numbers)

with open("temp.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open("temp.txt", "r") as file:
    text = file.read()
    print(text)


with open("temp.csv", "w") as file:
    numbers = ["ind,negative,positive\n"]
    for i in range(1, 11):
        numbers.append(f"{i},{random.randint(-1000, 0)},{random.randint(1, 1000)}\n")
    print(numbers)
    file.writelines(numbers)

with open("temp.csv", "r") as file:
    lines = file.readlines()
    print(lines)
    file_data = []
    for i, line in enumerate(lines):
        items = line.strip().split(",")
        if i == 0:
            header = items
            continue
        row_data = {}
        for j, value in enumerate(items):
            row_data[header[j]] = value
        file_data.append(row_data)

print(file_data)

import csv

with open("temp.csv", "w") as file:
    csv_dict_writer = csv.DictWriter(file, ["ind", "negative", "positive"])
    numbers = []
    for i in range(1, 11):
        numbers.append({"ind": i, "negative": random.randint(-1000, 0), "positive": random.randint(1, 1000)})
    print(numbers)
    csv_dict_writer.writerows(numbers)

with open("temp.csv", "r") as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)


with open("temp.json", "w") as file:
    numbers = []
    for i in range(1, 11):
        numbers.append({"ind": i, "negative": random.randint(-1000, 0), "positive": random.randint(1, 1000)})
    print(numbers)
    file.write(str(numbers).replace("'", '"'))

with open("temp.json", "r") as file:
    json_text = file.read()
    print(json_text)
    data = eval(json_text)
    print(data)


import json

with open("temp.json", "w") as file:
    numbers = []
    for i in range(1, 11):
        numbers.append(
            {
                "ind": i,
                "negative": random.randint(-1000, 0),
                "positive": random.randint(1, 1000),
                "is_good": random.choice([True, False])
            }
        )
    print(numbers)
    file.write(json.dumps(numbers))

with open("temp.json", "r") as file:
    json_text = file.read()
    print(json_text)
    data_loads = json.loads(json_text)
    print(data_loads)

with open("temp.json", "r") as file:
    data = json.load(file)
    print(data)
