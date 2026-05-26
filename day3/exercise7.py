#Exercise 7 - Faker Module

from faker import Faker

fake = Faker()

def add_users(number_of_users):
    users = []

    for _ in range(number_of_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

    return users


users = add_users(5)

for user in users:
    print(user)