#Exercise 2: cinemax #2

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name} pays: ${price}")
    total_cost += price

print(f"Total cost: ${total_cost}")



#Bonus 

family = {}
total_cost = 0

num_members = int(input("How many family members? "))

for i in range(num_members):
    name = input("Name: ")
    age = int(input("Age: "))
    family[name] = age

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name} pays: ${price}")
    total_cost += price

print(f"Total cost: ${total_cost}")