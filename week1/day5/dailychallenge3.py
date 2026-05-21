import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

pairs = []

for i in range(len(list_of_numbers)):
    for j in range(i, len(list_of_numbers)):
        if list_of_numbers[i] + list_of_numbers[j] == target_number:
            pairs.append((list_of_numbers[i], list_of_numbers[j]))

print(pairs)