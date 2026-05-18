#Exercise 5: For loop 


loop = []
for i in range(1, 21):
    loop.append(i)
print(loop) 



loop = []
for index, value in enumerate(range(1, 21)):
    loop.append(value)
    if value % 2 == 0:
        print(value) 