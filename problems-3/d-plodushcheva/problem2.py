import unittest


class Eukaryote:
    pass


class Animalia(Eukaryote):
    pass


class Chordata(Animalia):
    pass


class Aves(Chordata):
    pass


class Anseriformes(Aves):
    pass


class Anatidae(Anseriformes):
    pass


class Anser(Anatidae):
    def fly(self):
        return f"{self.__class__.__name__} is flying."


class WaterBirds:
    def __init__(self, location="Water"):
        self.location = location

    def swim(self):
        return f"{self.__class__.__name__} is swimming."


class Geese(WaterBirds):
    pass


class GreyGeese(Geese):
    pass


# Bar-headed goose
class AnserIndicus(Anser, GreyGeese):
    pass


class AnserRossii(Anser):
    pass


class TestInheritance(unittest.TestCase):
    def test_anser_fly(self):
        anser = AnserIndicus()
        assert anser.fly() == "AnserIndicus is flying."

    def test_water_birds_swim(self):
        water_bird = WaterBirds()
        assert water_bird.swim() == "WaterBirds is swimming."

    def test_geese_swim(self):
        geese = Geese()
        assert geese.swim() == "Geese is swimming."


if __name__ == '__main__':
    unittest.main()
