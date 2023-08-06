import math

class Pizza:
    base_sous = 'pepperoni'

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.sous = ""

    def __repr__(self):
        return f'Pizza({self.ingredients!r}  == Sous({self.sous}))'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    @staticmethod
    def circle_area(r):  #have no access to instance self and cls
        return r**2*math.pi

    def addSous(self, newSous = ""):
        self.sous = self.__class__.base_sous + str(newSous)

def test_classVSinstance():
    print(Pizza.margherita())
    print(Pizza.prosciutto())

    margarita = Pizza.margherita()
    my_pizza = Pizza('blue cheese, mozzarella, pear, bazilic')
    my_pizza.addSous()
    print(my_pizza)