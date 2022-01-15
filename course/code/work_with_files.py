import csv
import json
import random
import pickle
import sys

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


def generate_numbers(with_bool=False):
    import random
    _numbers = []
    for index in range(1, 100):
        _row = {
            "ind": index,
            "negative": random.randint(-1000, 0),
            "positive": random.randint(1, 1000),
        }
        if with_bool:
            _row.update({"is_good": random.choice([True, False])})

        _numbers.append(_row)

    return _numbers


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


with open("temp.csv", "w") as file:
    csv_dict_writer = csv.DictWriter(file, ["ind", "negative", "positive"])
    numbers = generate_numbers()
    print(numbers)
    csv_dict_writer.writerows(numbers)

with open("temp.csv", "r") as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)


with open("temp.json", "w") as file:
    numbers = generate_numbers()
    print(numbers)
    file.write(str(numbers).replace("'", '"'))

with open("temp.json", "r") as file:
    json_text = file.read()
    print(json_text)
    data = eval(json_text)
    print(data)


with open("temp.json", "w") as file:
    numbers = generate_numbers(with_bool=True)
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

with open("image.png", "rb") as file:
    data = file.read()


with open("new_image.png", "wb") as file:
    file.write(data)

with open("data.pickle", "wb") as file:
    numbers = generate_numbers(with_bool=True)
    pickle_data = pickle.dumps(numbers)
    json_data = json.dumps(numbers)
    print(sys.getsizeof(numbers))
    print(sys.getsizeof(pickle_data))
    print(sys.getsizeof(json_data))
    print(pickle_data)
    file.write(pickle_data)

with open("data.pickle", "rb") as file:
    pickle_data = file.read()
    data = pickle.loads(pickle_data)
print(data)

with open("data_1.pickle", "wb") as file:
    pickle.dump(numbers, file)

with open("data_1.pickle", "rb") as file:
    data = pickle.load(file)
print(data)
