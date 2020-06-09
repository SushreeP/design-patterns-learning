class Dog:
    def __init__(self):
        self.name = None

    def speak(self):
        return "Woof"


class Cat:
    def __init__(self):
        self.name = None

    def speak(self):
        return "Meow"


class Dog_factory:
    def get_pet(self):
        return Dog()

    def get_petfood(self):
        return "Pedigree"


class Petstore:
    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        pet_food = self.pet_factory.get_petfood()

        print(f"Our pet is a {pet}!")
        print(f"It eats {pet_food}.")
        print(f"It says hello like, '{pet.speak()}'!'")


factory = Dog_factory()
shop = Petstore(factory)
shop.show_pet()
