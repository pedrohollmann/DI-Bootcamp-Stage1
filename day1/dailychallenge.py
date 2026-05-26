class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, **animals):
        for animal, count in animals.items():
            if animal in self.animals:
                self.animals[animal] += count
            else:
                self.animals[animal] = count

    def get_info(self):
        result = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"

        result += "\n    E-I-E-I-0!"
        return result

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()

        parts = []

        for animal in animal_list:
            if self.animals[animal] > 1:
                parts.append(animal + "s")
            else:
                parts.append(animal)

        animals_str = ", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else parts[0]

        return f"{self.name}'s farm has {animals_str}."


macdonald = Farm("McDonald")

macdonald.add_animal(cow=5, sheep=1, goat=12)
macdonald.add_animal(sheep=1)

print(macdonald.get_info())
print(macdonald.get_short_info())