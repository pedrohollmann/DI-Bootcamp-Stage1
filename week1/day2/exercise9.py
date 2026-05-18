#Exercise 9: Cinemax Tickets

total = 0
while True:
    age = input("What is your age? (or 'quit') ? ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

        total = total + price

print(total)

    