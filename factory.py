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


def get_pet(pet="dog"):
    ''' depending on the input the petshop dictionary will return the pet object'''

    pet_shop = {"dog": Dog(), "cat": Cat()}

    return pet_shop[pet]


d = get_pet("dog")

print(d.speak())

c = get_pet("cat")
print(c.speak())
