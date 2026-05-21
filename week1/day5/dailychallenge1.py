
words = input("Enter words separated by commas: ")

words_list = words.split(",")

words_list.sort()

result = ",".join(words_list)

print(result)