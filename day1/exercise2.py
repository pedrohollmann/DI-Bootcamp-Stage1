#Exercise 2 - Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("David's Dog", 50)
sarahs_dog = Dog("Sarah's Dog", 35)

print(davids_dog.name)
print(davids_dog.height)
print(sarahs_dog.name)
print(sarahs_dog.height)

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger")
else:
    print("Both dogs are the same size")