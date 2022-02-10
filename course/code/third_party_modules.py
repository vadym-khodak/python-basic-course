# Бібліотека для відправлення HTTP запитів та обробки відповідей
import requests
import pprint


url = "https://api.fbi.gov/wanted/v1/list"
response = requests.get(url, params={"field_offices": "miami"})
data = response.json()
print(data["total"])
pprint.pprint(data["items"][0])


# Бібліотека для генерації тестових (фейкових даних)
from faker import Faker

fake = Faker()

print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())
