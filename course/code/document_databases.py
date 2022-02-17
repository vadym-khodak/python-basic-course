# -*- coding: utf-8 -*-
# Початок роботи
# Створення клієнта для підключення до бази даних

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Створення Python об’єктів для роботи з базою даних та коллекціями
blog_db = client.blog
posts_collection = blog_db.posts

# Робота з документами бази даних (CRUD - create read update delete)
# Додавання одного документу
import datetime

post = {
    "title": "How to use MongoDB in Python using pymongo",
    "author": {
        "full_name": "John Doe",
        "email": "john@email.com",
        "job_title": "Senior Data Engineer",
    },
    "tags": ["python", "mongodb", "databases", "pymongo"],
    "created_at": datetime.datetime.now(),
}

post_id = posts_collection.insert_one(post).inserted_id
print(post_id)

another_post = {
    "name": "How to use MongoDB in Python using pymongo",
    "author": "John Doe",
    "published": True,
    "date": datetime.datetime.now(),
}
another_post_id = posts_collection.insert_one(another_post).inserted_id
print(another_post_id)
print(type(another_post_id))


# Додавання декількох документів одночасно
import random
import faker

posts = []
fake = faker.Faker()
for _ in range(10):
    posts.append(
        {
            "title": fake.sentence(),
            "author": {
                "full_name": fake.name(),
                "email": fake.email(),
                "job_title": fake.job(),
            },
            "tags": [random.choice(["python", "mongodb", "databases", "pymongo"])],
            "created_at": datetime.datetime.now(),
        }
    )

inserted_ids = posts_collection.insert_many(posts).inserted_ids
print(inserted_ids)


# Отримання усіх документів з коллекції
from pprint import pprint
#
documents = posts_collection.find(
    {},
    {"title": 1, "tags": 1, "_id": 0}  # Вказання полів які повинні бути у відповіді від бази даних
)
print(documents)
pprint(list(documents))


# Отримання декількох документів з коллекції фільтруючи по значенню поля
pymongo_posts = posts_collection.find({"tags": ["pymongo"], "author.full_name": 'Mary Johnson'})
pprint(list(pymongo_posts))

# Отримання одного документу з коллекції
document = posts_collection.find_one({"_id": post_id})
pprint(document)

pymongo_document = posts_collection.find_one({"tags": ["pymongo"]})
pprint(pymongo_document)

# Оновлення одного документу у коллекції
result = posts_collection.update_one(
    {"_id": post_id},
    {"$set": {"title": "Updated title", "is_published": True}}
)

print(result)
updated_document = posts_collection.find_one({"_id": post_id})
pprint(updated_document)

# Оновлення декількох документів у коллекції
result = posts_collection.update_many(
    {"tags": ["databases"]},
    {"$unset": {"tags": ""}, "$set": {"updated": True}}
)
print(result)
updated_documents = posts_collection.find()
pprint(list(updated_documents))

# Оновлення усіх документів у коллекції
result = posts_collection.update_many(
    {},
    {"$set": {"is_published": False}}
)
print(result)
updated_documents = posts_collection.find()
pprint(list(updated_documents))


# Отримання кількості усіх документів у коллекції
documents_counter = posts_collection.count_documents({})
print(documents_counter)

# Видалення одного документу з коллекції
posts_collection.delete_one({"tags": ["python"]})
print(posts_collection.count_documents({}))

# Видалення декількох документів з коллекції
posts_collection.delete_many({"tags": ["pymongo"]})
print(posts_collection.count_documents({}))

# Видалення усіх документів з коллекції
posts_collection.delete_many({})
print(posts_collection.count_documents({}))


# Завершення роботи з клієнтом бази даних
# Видалення коллекції
blog_db.drop_collection("posts")

# Видалення бази даних
client.drop_database("blog")
# Закриття підключення до бази даних
client.close()


if __name__ == "__main__":
    pass
