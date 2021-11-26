x = 1
z, y = 2, 5
s = y + z / x
print(x, y, z, s)

first_name = "John"
lastName = "Doe"
BASIC_GREETING_PHRASE = "Hello"

phrase = input("Input greeting phrase: ") or BASIC_GREETING_PHRASE

print(phrase + " " + first_name)

print(id(BASIC_GREETING_PHRASE))


if __name__ == "__main__":
    pass
