#Exercise 4: Disney characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1
char_to_index = {name: i for i, name in enumerate(users)}
print(char_to_index)

# 2
index_to_char = {i: name for i, name in enumerate(users)}
print(index_to_char)

# 3
sorted_users = sorted(users)
sorted_dict = {name: i for i, name in enumerate(sorted_users)}
print(sorted_dict)