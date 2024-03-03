
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
    pass


class WaterBirds:
    pass


class Geese(WaterBirds):
    pass


class GreyGeese(Geese):
    pass


# Bar-headed goose
class AnserIndicus(Anser, GreyGeese):
    pass


class AnserRossii(Anser):
    pass
