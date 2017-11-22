class Animal(object):
    owner = "jack"

    def __init__(self, name):
        self._name = name

    @classmethod
    def get_owner(cls):
        return cls.owner

    @staticmethod
    def order_animal_food():
        print("ording...")
        print("ok")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(self.name + " is making sound wang wang wang wang...")


class Cat(Animal):
    def make_sound(self):
        print(self.name + " is making sound miu miu miu miu...")


animals = [Dog("旺财"), Cat("Kitty"), Dog("来福"), Cat("Betty")]

for animal in animals:
    print("Animal\'s name is: " + animal.name)
    print("Owner is: " + animal.get_owner())
    animal.make_sound()
    print("Start order animal food: ")
    animal.order_animal_food()
    print("=" * 45)
