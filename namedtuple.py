from collections import namedtuple
from sys import getsizeof
import json

#improved named tuple
from typing import NamedTuple

Car1 = namedtuple('Car1', 'color miliage value')

Car = namedtuple('Car', ['color', 'miliage'])

ElectricCar = namedtuple('ElectricCar',Car._fields + ('charge',))


# typing.NamedTuple



class MyCarWithMethods(Car):
    def hexColor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


# new tuple
class CarNew(NamedTuple):
    name : str
    miliege : float
    automatic : bool

def test_namedtuple():
    my_car1 = Car1('red', 456.77, 10)
    print(my_car1)

    my_car = Car('red', 456.77)
    color, millieage = my_car
    # my_car_shallowcopy = namedtuple(my_car)
    # my_car_shallowcopy[0] = 'blue'
    print(my_car)
    print(*my_car) #unpacking tuple
    print(getsizeof(my_car))
    # print(my_car_shallowcopy)

    c = MyCarWithMethods('yellow', 1234)
    print(c.hexColor())

    elCar = ElectricCar('white', 33.44, '90%' )
    print(elCar)
    print(getsizeof(elCar))

    print("Json: \n" + json.dumps(elCar._asdict()))

    #shallow copy and replace the value
    print(my_car._replace(color='Blue'))

    print("Create CarNew NamedTuple:")
    car_new1 = CarNew('Buggatti', 123454.55, True)
    print("{}".format(car_new1))




