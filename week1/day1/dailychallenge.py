#Daily Challenge: Build up a string

# user = 'one to ten'

# if len(user) > 10:
#    print('too long')
# elif len(user) < 10:
#    print('too short')
# else:
#    print('perfect')



# text = input('write a word')
# print(text[0])
# print(text[-1])

# text = input('write a word')
# result = ''

# for i in text:
#     result = result + i
#     print(result)


import random

text = input("What's your name? ")

lista = list(text)

random.shuffle(lista)

result = "".join(lista)

print(result)