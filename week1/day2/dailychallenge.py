#Daily Challenge



#Exercise 1

number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

result = []

for i in range(1, length + 1):
    result.append(number * i)

print(result)

#Exercise 2

word = input("Enter a word: ")

result = ""

for char in word:
    if len(result) == 0 or char != result[-1]:
        result += char

print(result)