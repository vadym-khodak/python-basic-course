# Робота з реляційними даними

# Робота за базаю даних MongoDB
# pip install pymongo
import datetime
import random
from pprint import pprint

import faker
from pymongo import MongoClient  # https://pymongo.readthedocs.io/en/stable/tutorial.html

client = MongoClient("mongodb://localhost:27017/")
db = client.blog
posts_collection = db.posts

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


document = posts_collection.find_one({"_id": post_id})
print(document)


documents = posts_collection.find()
print(documents)
pprint(list(documents))

pymongo_posts = posts_collection.find({"tags": ["pymongo"]})
pprint(list(pymongo_posts))

result = posts_collection.update_one({"_id": post_id}, {"$set": {"title": "Updated title", "is_published": True}})
print(result)
updated_document = posts_collection.find_one({"_id": post_id})
print(updated_document)

print(posts_collection.count_documents({}))
posts_collection.delete_one({"tags": ["python"]})
print(posts_collection.count_documents({}))
posts_collection.delete_many({"tags": ["pymongo"]})
print(posts_collection.count_documents({}))
posts_collection.delete_many({})
print(posts_collection.count_documents({}))

client.close()

if __name__ == "__main__":
    pass
