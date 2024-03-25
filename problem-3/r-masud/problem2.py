import unittest

class Living:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def reproduce(self):
        return f"{self.name} is reproducing"


class Animal(Living):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        return f"{self.name} is moving"


class Vertebrate(Animal):
    def __init__(self, name):
        super().__init__(name)

    def backbone(self):
        return f"{self.name} has a backbone"


class Mammal(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

    def feed_milk(self):
        return f"{self.name} feeds milk to its young"


class Carnivore(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def hunt(self):
        return f"{self.name} is hunting for prey"


class Lion(Carnivore):
    def __init__(self, name):
        super().__init__(name)


class Human(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} can speak"


class TestLivingHierarchy(unittest.TestCase):
    def setUp(self):
        self.lion = Lion("Lion")
        self.human = Human("Human")

    def test_lion(self):
        self.assertEqual(self.lion.eat(), "Lion is eating")
        self.assertEqual(self.lion.move(), "Lion is moving")
        self.assertEqual(self.lion.hunt(), "Lion is hunting for prey")

    def test_human(self):
        self.assertEqual(self.human.eat(), "Human is eating")
        self.assertEqual(self.human.move(), "Human is moving")
        self.assertEqual(self.human.speak(), "Human can speak")


if __name__ == "__main__":
    unittest.main()
