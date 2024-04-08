import unittest


class LivingThing:
    pass


class RunningThing:
    pass


class Producer:
    pass


class Plant(LivingThing, Producer):
    pass


class Animal(LivingThing, RunningThing):
    pass


class Vertebrate(Animal):
    pass


class Tree(Plant):
    pass


class Grass(Plant):
    pass


class Mammal(Vertebrate):
    pass


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


class TestClassInheritance(unittest.TestCase):
    def test_plant_inheritance(self):
        self.assertTrue(issubclass(Tree, Plant))
        self.assertTrue(issubclass(Grass, Plant))

    def test_animal_inheritance(self):
        self.assertTrue(issubclass(Mammal, Animal))
        self.assertTrue(issubclass(Dog, Animal))
        self.assertTrue(issubclass(Cat, Animal))
        self.assertTrue(issubclass(Vertebrate, Animal))

    def test_mammal_inheritance(self):
        self.assertTrue(issubclass(Dog, Mammal))
        self.assertTrue(issubclass(Cat, Mammal))

    def test_deep_inheritance(self):
        self.assertTrue(issubclass(Dog, Mammal))
        self.assertTrue(issubclass(Mammal, Vertebrate))
        self.assertTrue(issubclass(Vertebrate, Animal))
        self.assertTrue(issubclass(Animal, LivingThing))

    def test_multi_inheritance(self):
        self.assertTrue(issubclass(Plant, (LivingThing, Producer)))
        self.assertTrue(issubclass(Animal, (LivingThing, RunningThing)))


if __name__ == '__main__':
    unittest.main()
