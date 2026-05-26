#Exercise 4 - Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.groups = {}

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        grouped = {}

        for animal in self.animals:
            letter = animal[0].upper()

            if letter not in grouped:
                grouped[letter] = []

            grouped[letter].append(animal)

        self.groups = grouped
        return grouped

    def get_groups(self):
        if not self.groups:
            self.sort_animals()

        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")


brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")

brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")

brooklyn_safari.get_animals()

brooklyn_safari.sort_animals()

brooklyn_safari.get_groups()