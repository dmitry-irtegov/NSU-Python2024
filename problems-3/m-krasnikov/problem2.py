import unittest


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} can move"

    def eat(self):
        return f"{self.name} can eat"

    def reproduce(self):
        return f"{self.name} can reproduce"


class Chordates(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bones(self):
        return f"{self.name} has bones"


class Mammal(Chordates):
    def __init__(self, name):
        super().__init__(name)

    def feed_milk(self):
        return f"{self.name} can feed milk"


class Predator(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def hunt(self):
        return f"{self.name} can hunt"


class Bearish(Predator):

    def __init__(self, name):
        super().__init__(name)

    def bear(self):
        return f"{self.name} is a bear"


class Bear(Bearish):
    def __init__(self, name):
        super().__init__(name)


class Human(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} can speak"


class TestLivingHierarchy(unittest.TestCase):
    def setUp(self):
        self.bear = Bear("Bear misha")
        self.human = Human("Human sasha")

    def test_lion(self):
        self.assertEqual(self.bear.move(), "Bear misha can move")
        self.assertEqual(self.bear.eat(), "Bear misha can eat")
        self.assertEqual(self.bear.reproduce(), "Bear misha can reproduce")
        self.assertEqual(self.bear.bones(), "Bear misha has bones")
        self.assertEqual(self.bear.feed_milk(), "Bear misha can feed milk")
        self.assertEqual(self.bear.bear(), "Bear misha is a bear")

    def test_human(self):
        self.assertEqual(self.human.move(), "Human sasha can move")
        self.assertEqual(self.human.eat(), "Human sasha can eat")
        self.assertEqual(self.human.reproduce(), "Human sasha can reproduce")
        self.assertEqual(self.human.bones(), "Human sasha has bones")
        self.assertEqual(self.human.feed_milk(), "Human sasha can feed milk")
        self.assertEqual(self.human.speak(), "Human sasha can speak")


if __name__ == "__main__":
    unittest.main()
